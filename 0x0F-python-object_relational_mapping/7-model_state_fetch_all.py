#!/usr/bin/python3
"""
list all state ordered by id

"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]))

    with engine.connect() as conn:
        result = conn.execute('SELECT * FROM states ORDER BY id')

    for row in result.fetchall():
        print("{}: {}".format(row['id'], row['name']))
