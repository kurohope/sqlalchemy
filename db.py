import random


from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship



engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/blog?charset=utf8')
Base = declarative_base()
print engine
print Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article')




class Article(Base):

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User')




    #def __repr__(self):
        #return '%s(%r)' % (self.__class__.__name__, self.username)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    user = User(username='Harp', password='123456',email='2132321@qq.com')
    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(user)
    session.commit()