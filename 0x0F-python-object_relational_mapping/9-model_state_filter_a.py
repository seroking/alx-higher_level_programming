#!/usr/bin/python3
"""
list all states starting with 'a'
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.ilike('%a%')).order_by(State.id)

    for state in states.all():
        print("{}: {}".format(state.id, state.name))
