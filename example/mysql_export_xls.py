# -*- coding: UTF8 -*-
# encoding = utf8
import sys
from datetime import date

import MySQLdb
from xlwt import *

reload(sys)
sys.setdefaultencoding('utf-8')

DEV_MODE = 0

# mysql offline config
dbhost = '127.0.0.1'
dbuser = 'root'
dbpasswd = '123456'
dbname = 'xxxx'

dbconn_admin = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=dbname, port=3306, charset='utf8')
dbconn_admin.select_db(dbname)


def queryWithResult(dbconn, sql):
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        results = cur.fetchall()
        dbconn.commit()
        cur.close()
        return results
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return ()


rmap = {}
for y in range(2013, 2017):
    for m in range(1, 13):
        rkey = '%s-%.2d' % (y, m)
        rmap[rkey] = {
            'year': y,
            'month': m,
            'ym': rkey,
            'new': 0,
            'renew': 0,
            'active': 0
        }

#new added
sql = "select count(1) as total,year(date_added) as y,month(date_added) as m from store group by y,m"
rs = queryWithResult(dbconn_admin, sql)
for r in rs:
    rkey = '%s-%.2d' % (r['y'], r['m'])
    if rkey not in rmap:
        continue
    rmap[rkey]['new'] = rmap[rkey]['new'] + r['total']

#renew
sql = "select count(distinct r.store_id) as total,year(r.date_added) as y,month(r.date_added) as m from renew_record r left join store s ON(s.store_id=r.store_id) where r.renew_days > 30 group by y,m"
rs = queryWithResult(dbconn_admin, sql)
for r in rs:
    rkey = '%s-%.2d' % (r['y'], r['m'])
    if rkey not in rmap:
        continue
    rmap[rkey]['renew'] = rmap[rkey]['renew'] + r['total']

results = []
for k in sorted(rmap):
    results.append(rmap[k])

ro = {
    'ym': '日期',
    'new': '新增',
    'renew': '续费',
    'active': '活跃'
}

ros = [
    'ym',
    'new',
    'renew',
    'active'
]

w = Workbook('utf8')
ws = w.add_sheet('商户')

for i in range(0, len(ros)):
    ws.write(0, i, ro[ros[i]])

idx = 1
for r in results:
    for i in range(0, len(ros)):
        ws.write(idx, i, r[ros[i]])
    idx = idx + 1

file_name = 'store-%s.xls' % (date.today().strftime('%Y%m%d'))
w.save(file_name)
print('export done')
