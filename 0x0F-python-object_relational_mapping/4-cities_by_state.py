#!/usr/bin/python3
"""
lists all cities from the database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                inner JOIN states ON cities.state_id = states.id\
                order by cities.id ASC")

    for x in cur:
        print(x)

    cur.close()
    db.close()
