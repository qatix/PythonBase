# -*- coding: utf-8 -*-
# python3
__author__ = 'hawk'
import configparser
import redis

cf = configparser.ConfigParser()
cf.read('.env')
if cf.get('property', 'env') == 'development':
    cf.read('config_dev.ini')
else:
    cf.read('config_prod.ini')

# redis config
redisHost = cf.get('property', 'redisHost')
redisPort = cf.get('property', 'redisPort')
redisPassword = cf.get('property', 'redisPassword')
rds = redis.StrictRedis(host=redisHost, port=redisPort, db=0, password=redisPassword)

print(rds.get("abc"))
rds.set("abc", "abc-123")
print(rds.get("abc"))
