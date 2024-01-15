#!/usr/bin/python3
"""
prints all City objects from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]))

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).options(joinedload(
        City.state)).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
