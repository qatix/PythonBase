__author__ = 'hawk'
#!/usr/bin/env python
# coding=utf-8

import redis

#Record the error to log
redisHost = '127.0.0.1'
redisPort = 6379
redisPassword = ''

rds = redis.StrictRedis(host=redisHost, port=redisPort, db=0, password=redisPassword)

p = rds.pubsub()
# p.subscribe('myc-1','myc-2');
#way 1
# while True:
#     message = p.get_message()
#     if message:
#         print('get message')
#         print(message)
#     time.sleep(0.001)

#way2
# for message in p.listen():
#     print(message)

#way3
def my_handler(message):
    print('handle message')
    print(message)

# p.subscribe(**{'myc-1':my_handler});
# thread = p.run_in_thread(sleep_time=0.001)

p.psubscribe(**{'myc-*':my_handler})
thread = p.run_in_thread(sleep_time=0.001)

# p.get_message()



