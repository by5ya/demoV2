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
    def get_products(self):
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

        cur  =self.conn.cursor()
        cur.execute(query)
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