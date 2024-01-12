#!/usr/bin/python3
"""
displays all values in the states table
where name matches the argument
write one that is safe from MySQL injections!
"""

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    for x in cur:
        if x[1] == state_name:
            print(x)

    cur.close()
