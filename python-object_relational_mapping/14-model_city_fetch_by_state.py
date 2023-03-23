#!/usr/bin/python3
""" Prints all City objects from the database"""


from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(City.state_id == State.id)\
                                      .order_by(City.id).all()
    for cities, state in query:
        print(f"{state.name}: ({cities.id}) {cities.name}")

    session.close()
