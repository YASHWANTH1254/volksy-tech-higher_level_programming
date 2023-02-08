#!/usr/bin/python3
""" the sql injection."""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT name from cities where state_id=3;")
    for i in c:
        print(i)
