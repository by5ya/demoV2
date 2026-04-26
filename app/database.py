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