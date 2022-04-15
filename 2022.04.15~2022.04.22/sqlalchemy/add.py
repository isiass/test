
# 导入:

from audioop import add

from re import U

from site import USER_BASE

from sqlite3 import dbapi2

from unicodedata import name

from sqlalchemy import Column, String, create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:

Base = declarative_base()

SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:root@localhost:3306/testdb?charset=utf8mb4"

# 初始化数据库连接:

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()#向表中添加数据
Session=sessionmaker(bind=engine)
sess=Session() #实例化了一个会话(或叫事务)，之后的所以操作都是基于这个对象的
user=User(id='2',name='maligan')
sess.add(user)
#向数据库提交数据
sess.commit()
#关闭会话
sess.close()