#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306,
        )
    state_name = argv[4]

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)


    cur.close()
    db.close()
