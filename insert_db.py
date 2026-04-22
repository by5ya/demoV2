import psycopg2 as pg
from config import creds
import pandas as pd

con = pg.connect(**creds)
cur = con.cursor()

address_df = pd.read_excel("./import/Пункты выдачи_import.xlsx")
orders_df = pd.read_excel("./import/Заказ_import.xlsx")
users_df = pd.read_excel("./import/user_import.xlsx")
product_df = pd.read_excel("./import/Tovar.xlsx")

address_list = [row["Адрес"] for _, row in address_df.iterrows()]

def addresses():
    for _, row in address_df.iterrows():
        cur.execute('insert into address (name) values (%s)', (row["Адрес"],))
    con.commit()


def users():
    for _, row in users_df.iterrows():
        cur.execute('''insert into users (role, name, login, password) values (%s, %s, %s, %s)''', (row['Роль сотрудника'], row['ФИО'], row['Логин'], row['Пароль'],))

    con.commit()

def products():
    for _, row in product_df.iterrows():
        photo = row['Фото'] if not pd.isna(row['Фото']) else "picture.png"

        cur.execute('''insert into products (
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
        ''', (row['Наименование товара'], row['Артикул'], row['Единица измерения'],row['Цена'],row['Поставщик'],row['Производитель'],row['Категория товара'],row['Действующая скидка'],row['Кол-во на складе'],row['Описание товара'],photo))
    con.commit()

def orders():
    for _, row in orders_df.iterrows():
        date_order = pd.to_datetime(row['Дата заказа'], errors='coerce')
        date_deliv = pd.to_datetime(row['Дата доставки'], errors='coerce')

        if pd.isna(date_order) or pd.isna(date_deliv):
            print("skip")
            continue

        address_name = address_list[int(row['Адрес пункта выдачи']) - 1]
        cur.execute('select id from address where name = %s', (address_name, ))
        address_id = cur.fetchone()[0]
        cur.execute('select id from users where name = %s', (row['ФИО авторизированного клиента'], ))
        user_id = cur.fetchone()[0]
        articul = row['Артикул заказа']
        cur.execute('''insert into orders (
        articul ,
    date_order ,
    date_delivery ,
    address_id ,
    user_id ,
    code ,
    status 
        ) values (%s, %s, %s, %s, %s, %s, %s) returning id''', (articul, date_order, date_order, address_id, user_id, row['Код для получения'], row['Статус заказа']))

        order_id = cur.fetchone()[0]
        parts = [part.strip() for part in str(articul).split(',')]
        for i in range(0, len(parts), 2):
            cur.execute('select id from products where articul = %s', (parts[i], ))
            product_id = cur.fetchone()[0]
            cur.execute('insert into order_items (order_id, product_id, quantity) values (%s, %s, %s)', (order_id, product_id, int(parts[i+1])))

        con.commit()

if __name__=='__main__':
    # addresses()
    # users()
    # products()
    orders()
