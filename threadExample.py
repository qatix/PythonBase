# coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    time.sleep(1)

thread_list = []
for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()


for t in thread_list:
    t.join()

print 'main_thread end!'