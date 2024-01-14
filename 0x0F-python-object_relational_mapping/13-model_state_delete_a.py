#!/usr/bin/python3
"""
delete all states containing the letter 'a'
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

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_del = session.query(State).filter(State.name.like("%a%")).all()

    for state in states_to_del:
        session.delete(state)

    session.commit()
