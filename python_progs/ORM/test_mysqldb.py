#!/usr/bin/python3
'''
Learning to use mysqldb the ALX way
'''
import MySQLdb

db = MySQLdb.connect(host='localhost', user='koby', passwd='Kw@5a9ng', db='my_self')
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS member (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256), age INT UNSIGNED)")
members = ('Kwabena Sapong', 'Alice Sapong', 'Afrakoma Sapong')
for member in members:
    cur.execute("INSERT INTO member (name) VALUES (%s)", (member,))
    print("ID: %s" % cur.lastrowid)
cur.execute("INSERT INTO personal (name, age) values ('Alice Sapong', 33)")

cur.execute("SELECT * FROM member")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print("{}".format(col))
    print('----')

cur.execute("SELECT * FROM personal WHERE id = 1")
row = cur.fetchone()
print("id: {}, name: {}, age: {}".format(row[0], row[1], row[2]))
cur.close()
db.commit()
db.close()
