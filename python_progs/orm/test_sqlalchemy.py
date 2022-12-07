#!/usr/bin/python3
'''
Learning to use sqlalcemy the ALX way

import MySQLdb
from sys import argv

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
'''

import sqlalchemy
import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


#if __name__ == "__main__":
'''connecting to the mysql'''
#url = "mysql+mysqldb://{}:{}@localhost/{}".format("alx", "Al*4221@", "test")
#engine = create_engine(url, pool_pre_ping=True)

engine = create_engine("mysql+mysqldb://alx:Al*4221@@localhost/test", pool_recycle=3600)

'''Mapping the ORM'''
Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "Member_{} (name= {}, age= {})".format(self.id, self.name, self.age)

'''Create a Schema'''
#print(Member.__table__)

Base.metadata.create_all(engine)

#connection = engine.connect()
