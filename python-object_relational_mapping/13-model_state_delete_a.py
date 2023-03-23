#!/usr/bin/python3
"""
Script that deletes all the State objects with a name
containing the letter "a" from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    queryList = session.query(State).filter(State.name.like("%a%")).all()

    for statesWith_a in queryList:
        session.delete(statesWith_a)

    session.commit()
    session.close()
