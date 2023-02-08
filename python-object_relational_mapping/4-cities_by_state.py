#!/usr/bin/python3
""" list all states from database."""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT id, name FROM cities order by id;")
    for i in c:
        if i[1] == sys.argv[4]:
            print(i)
