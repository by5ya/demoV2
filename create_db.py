import psycopg2 as pg
from config import creds

con = pg.connect(**creds)
cur = con.cursor()

with open("sql.sql", "r") as f :
    sql = f.read()

cur.execute(sql)
con.commit()
cur.close()