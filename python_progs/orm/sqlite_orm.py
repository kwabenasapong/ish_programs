#!/usr/bin/python3
'''ORM tutorial from sqlalchemy'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///:memory', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "User_{}_(name={}, fullname={}, nickname={})",format(self.id, self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)
