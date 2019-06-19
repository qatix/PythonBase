__author__ = 'hawk'
import pymysql

def getDbConn(dbhost,dbuser,dbpasswd,dbname):
    connection = pymysql.connect(host=dbhost,
                             user=dbuser,
                             password=dbpasswd,
                             db=dbname,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

def getMany(dbconn,sql):
    try:
        cur=dbconn.cursor()
        # cur.execute('set names utf8')
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        print(e)
        return ()

def getOne(dbconn,sql):
    try:
        cur=dbconn.cursor()
        # cur.execute('set names utf8')
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        print(e)
        return None

def executeSql(dbconn,sql):
   # print(sql)
    try:
        cur=dbconn.cursor()
        # cur.execute('set names utf8')
        cur.execute(sql)
        dbconn.commit()
        cur.close()
    except Exception as e:
        print(e)

def insertOne(dbconn,sql):
    try:
        cur=dbconn.cursor()
        cur.execute(sql)
        dbconn.commit()
        insert_id = cur.lastrowid
        cur.close()
        return insert_id
    except Exception as e:
        print(e)
        return -1

def insertMany(dbconn,sql,args):
    try:
        cur=dbconn.cursor()
        cur.executemany(sql,args)
        dbconn.commit()
        cur.close()
    except Exception as e:
        print(e)

def queryWithResults(dbconn,sql):
    try:
        cur=dbconn.cursor(pymysql.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        print(e)
        return ()

def queryWithOneResult(dbconn, sql):
    try:
        cur=dbconn.cursor(pymysql.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        print(e)
        return ()

def queryWithNoResult(dbconn,sql):
    try:
        cur=dbconn.cursor(pymysql.cursors.DictCursor)
        cur.execute('set names utf8')

        # print("sql: %s" % sql)
        cur.execute(sql)
        dbconn.commit()
        cur.close()

        return
    except Exception as e:
        print(e)
        return ()
