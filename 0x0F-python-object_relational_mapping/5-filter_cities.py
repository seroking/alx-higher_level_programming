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
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s"
    cur.execute(query, (argv[4],))
    cities = cur.fetchall()

    row = sql_cm.fetchall()

    if not row:
        print("")

    for i in range(len(row)):
        if i == len(row) - 1:
            print(row[i][0])
        else:
            print(row[i][0], end=", ")

    cur.close()
    db.close()

