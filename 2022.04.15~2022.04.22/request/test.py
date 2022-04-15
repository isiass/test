# 导入:
from abc import ABCMeta
from audioop import add
from cgi import test
from curses import start_color
from logging import root
from re import U
from site import USER_BASE
from sqlite3 import dbapi2
from unicodedata import name
from sqlalchemy import Column, String, column, create_engine, table
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()



SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:root@localhost:3306/testdb?charset=utf8mb4"
# 初始化数据库连接:
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'abc'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    nums = Column(String(20))
    pre_nums= Column(String(20))
    price = Column(String(20))



Base.metadata.create_all(engine)
#向表中添加数据
Session=sessionmaker(bind=engine)
db_session=Session() #实例化了一个会话(或叫事务)，之后的所以操作都是基于这个对象的
import xlrd

#文件名以及路径，如果路径或者文件名有中文给前面加一个r

data=xlrd.open_workbook("abc.xlsx")

#获取book(excel文件)中一个工作表
table=data.sheet_by_index(0) #通过索引顺序获取
import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="root",db='testdb',charset='utf8',port=3306)
#创建游标
cursor=conn.cursor()
#提交
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()

print(11)



