# -*- coding: utf-8 -*-
# python3
__author__ = 'hawk'
import sys

sys.path.append("lib")
import configparser
import mysqllib

cf = configparser.ConfigParser()
cf.read('.env')
if cf.get('property', 'env') == 'development':
    cf.read('config_dev.ini')
else:
    cf.read('config_prod.ini')

dbhost = cf.get('mysql', 'dbhost')
dbuser = cf.get('mysql', 'dbuser')
dbpasswd = cf.get('mysql', 'dbpasswd')
dbname = cf.get('mysql', 'dbname')


def getDbConn():
    dbconn = mysqllib.getDbConn(dbhost, dbuser, dbpasswd, dbname)
    return dbconn

'''
drop table if exists category;
create table category(
  id int auto_increment primary key ,
  name varchar(32) not null default '',
  create_time datetime not null default NOW(),
  update_time datetime not null default NOW()
)default  charset=utf8 comment='Category';

insert into category(name) values('Apple'),('Huawei'),('Xiaomi'),('Oppo');
'''
dbconn = getDbConn()

sql = "insert into category set name='pythonTest'"
id =  mysqllib.insertOne(dbconn,sql)
print("insert id:{}".format(id))

sql = 'SELECT * from category'
categories = mysqllib.getMany(dbconn, sql)
for category in categories:
    print(category)

dbconn.close()
