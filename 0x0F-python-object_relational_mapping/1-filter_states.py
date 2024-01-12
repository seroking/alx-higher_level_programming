#!/usr/bin/python3
"""
lists all states starting with 'N' from the database hbtn_0e_0_usa:
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for x in cur:
        if x[1][0] == 'N':
            print(x)

    cur.close()
    db.close()
