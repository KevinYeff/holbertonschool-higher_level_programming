#!/usr/bin/python3
"""
Prints the State objects with the name passed as argument from the database
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

    stateName = argv[4]

    searchState = session.query(State).filter(State.name == stateName).all()

    if searchState:
        for state in searchState:
            print(state.id)
    else:
        print("Not found")

    session.close()
