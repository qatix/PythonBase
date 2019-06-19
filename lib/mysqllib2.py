__author__ = 'hawk'
import MySQLdb

def getDbConn(dbhost,dbuser,dbpasswd,dbname):
    connection = MySQLdb.connect(host=dbhost,user=dbuser,passwd=dbpasswd,db=dbname,port=3306,charset='utf8')
    return connection

def getMany(dbconn,sql):
    print(sql)
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        results = cur.fetchall()
        dbconn.commit()
        cur.close()
        return results
    except Exception as e:
        print(e)
        return ()

def getOne(dbconn,sql):
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        result = cur.fetchone()
        dbconn.commit()
        cur.close()
        return result
    except Exception as e:
        print(e)
        return None

def executeSql(dbconn,sql):
    print(sql)
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        dbconn.commit()
        row_affected = cur.rowcount
        cur.close()
        return row_affected
    except Exception as e:
        print(e)
        return 0

def insertOne(dbconn,sql):
    print(sql)
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.execute(sql)
        dbconn.commit()
        insert_id = cur.lastrowid
        cur.close()
        return insert_id
    except Exception as e:
        print(e)
        return -1

def insertMany(dbconn,sql,args):
    print(sql)
    try:
        cur = dbconn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('set names utf8')

        cur.executemany(sql,args)
        dbconn.commit()
        insert_id = cur.lastrowid
        cur.close()
    except Exception as e:
        print(e)