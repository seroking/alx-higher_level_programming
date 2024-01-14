#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database
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

    State_update = session.query(State).filter(State.id == 2).first()

    if (State_update):
        State_update.name = "New Mexico"

    session.commit()
