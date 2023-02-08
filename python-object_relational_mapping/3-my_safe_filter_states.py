#!/usr/bin/python3
"""SQL Injection"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    for i in c:
        if i[1] == sys.argv[4]:
            print(i)
