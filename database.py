import cx_Oracle

conn = cx_Oracle.connect(user = 'ADMIN1',password = 'admin1',dsn = 'xe')
cur=conn.cursor()
cur.execute("create table USER_REG ( )")
conn.close()