#!/usr/bin/python3
"""
Write a script that prints the State object
with the name passed as argument

"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")
