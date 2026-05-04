import psycopg2 as pg
from config import creds
import pandas as pd


class Database():
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        con = pg.connect(**creds)
        if con:
            return con
        else:
            print("ошибка подключения")

    def login_user(self, login, password):
        query = 'select id, role, name from users where login = %s and password = %s'
        cur = self.conn.cursor()

        cur.execute(query, (login, password,))
        result = cur.fetchone()
        if result:
            return {
                "id": result[0],
                "role": result[1],
                "fio": result[2]
            }
    def get_products(self,  sort=None, filt="", search=""):
        query = '''
        select 
        id,
        name ,
        articul ,
        unit ,
        price ,
        seller ,
        producer ,
        category ,
        discount ,
        quantity ,
        description ,
        photo from products
        '''
        where_conds = []
        params = []
        if filt.strip() and filt != "":
            params.append(filt.strip())
            where_conds.append(' seller = %s ')

        if search.strip() and search != "":
            pattern = f"%{search.strip()}%"
            where_conds.append('''(
            name like %s
            or articul like %s
            or unit like %s
            or seller like %s
            or producer like %s
            or category like %s
            or description like %s
            )''')
            params.extend([pattern]*7)

        if where_conds:
            query += " WHERE " + " AND ".join(where_conds)

        if sort:
            query+= " ORDER by quantity asc"
        elif sort == False:
            query+= " ORDER by quantity desc"


        cur  =self.conn.cursor()
        cur.execute(query, params)
        result = cur.fetchall()
        if result:
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "articul": row[2],
                    "unit": row[3],
                    "price" : row[4],
                    "seller": row[5],
                    "producer" : row[6],
                    "category" : row[7],
                    "discount" : row[8],
                    "quantity" : row[9],
                    "description" : row[10],
                    "photo": row[11]
                }
                for row in result
            ]

    def get_distinct(self, field, table):
        query = f'select distinct on({field}) {field} from {table}'
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if result:
            return [row[0] for row in result]

    def update_product(self, product, product_id):
        query = '''update products set 
        name = %s,
        articul = %s,
        unit = %s,
        price = %s,
        seller = %s,
        producer = %s,
        category = %s,
        discount = %s,
        quantity = %s,
        description = %s,
        photo = %s
        where id = %s
        '''
        params = [product['name'], product['articul'],product['unit'],product['price'],product['seller'],product['producer'],product['category'],product['discount'],product['quantity'],product['description'],product['photo'], product_id]
        cur = self.conn.cursor()
        cur.execute(query, params)
        cur.close()
        self.conn.commit()


    def create_product(self, product):
        query = '''insert into products (
        name ,
        articul ,
        unit ,
        price ,
        seller ,
        producer ,
        category ,
        discount ,
        quantity ,
        description ,
        photo 
        ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        cur = self.conn.cursor()
        params = [product['name'], product['articul'],product['unit'],product['price'],product['seller'],product['producer'],product['category'],product['discount'],product['quantity'],product['description'],product['photo']]
        cur.execute(query, params)
        cur.close()
        self.conn.commit()


    def check_product(self, product_id):
        query = 'select id from order_items where product_id = %s'
        cur = self.conn.cursor()
        cur.execute(query, (product_id,))
        result = cur.fetchall()
        if result:
            return False
        return True

    def delete_product(self, product_id):
        query = 'delete from products where id = %s'
        cur = self.conn.cursor()
        cur.execute(query, (product_id,))
        cur.close()
        self.conn.commit()

    def get_orders(self):
        query = 'select o.id, o.articul, o.date_order, o.date_delivery, ad.name, o.status from orders o left join address ad on ad.id = o.address_id'
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if result:
            return [
                {
                    "id": row[0],
                    "articul": row[1],
                    "date_order": row[2],
                    "date_deliv": row[3],
                    "address": row[4],
                    "status": row[5]
                }
                for row in result
            ]

    def get_order_items(self, order_id):
        query = "select oi.id, oi.quantity, p.name, p.articul, p.id from order_items oi left join products p on p.id = oi.product_id where oi.order_id = %s"
        cur = self.conn.cursor()
        cur.execute(query, (order_id,))
        result = cur.fetchall()
        if result:
            return [
                {
                    "id": row[0],
                    "quantity": row[1],
                    "product_name": row[2],
                    "product_articul": row[3],
                    "product_id": row[4],
                    "flag": "exist"
                }
                for row in result
            ]
    def create_order_item(self, order_item, order_id):
        cur = self.conn.cursor()
        cur.execute('insert into order_items (order_id, product_id, quantity) values (%s, %s, %s)', (order_id, order_item['product_id'], order_item['quantity'],))
        self.conn.commit()

    def delete_order_item(self, id):
        cur = self.conn.cursor()
        cur.execute('delete from order_items where id =  %s', (id,))
        self.conn.commit()
    def update_order_item(self, order_item, id):
        cur = self.conn.cursor()
        cur.execute('update order_items set quantity = %s where id = %s', (order_item['quantity'], id,))
        self.conn.commit()

    def create_order(self, order, user):
        cur = self.conn.cursor()
        address_id  = self.get_or_create(order['address'])
        cur.execute('''insert into orders (
        articul ,
        date_order ,
        date_delivery ,
        address_id ,
        user_id ,
        code ,
        status 
        ) values (%s, %s, %s, %s, %s, %s, %s) returning id''', (order['articul'], order['date_order'], order['date_delivery'], address_id, user['id'], "000", order['status'],))

        order_id = cur.fetchone()[0]
        self.conn.commit()
        return  order_id

    def get_or_create(self, name):
        cur = self.conn.cursor()
        cur.execute('select id from address where name = %s', (name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            cur.execute('insert into address (name) values (%s) returning id', (name,))
            result = cur.fetchone()[0]
            self.conn.commit()
            return result

    def update_order(self, order, order_id):
        cur = self.conn.cursor()
        address_id  = self.get_or_create(order['address'])
        cur.execute('''update orders set
        articul = %s ,
        date_order = %s,
        date_delivery = %s ,
        address_id = %s,
        status = %s where id = %s''',(order['articul'], order['date_order'], order['date_delivery'], address_id,  order['status'], order_id,))
        self.conn.commit()

    def delete_order(self, order_id):
        cur = self.conn.cursor()
        cur.execute('''delete from orders where id = %s''',(order_id,))
        self.conn.commit()