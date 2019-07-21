__author__ = 'hawk'
import subprocess
import collections
from random import Random


def shellWithResult(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p.stdout.read()


def md5(str):
    import hashlib

    m = hashlib.md5()
    m.update(str.encode('utf8'))
    return m.hexdigest()


def decodeBytesDict(data):
    if type(data) == bytes:
        return data.decode('utf8')
    elif isinstance(data, collections.Mapping):
        return dict(map(decodeBytesDict, data.items()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(decodeBytesDict, data))
    else:
        return data


def randomStr(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def atoi(str):
    try:
        r = int(str)
        return r
    except Exception, e:
        return 0


def checkdate(m, d, y):
    import datetime

    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False