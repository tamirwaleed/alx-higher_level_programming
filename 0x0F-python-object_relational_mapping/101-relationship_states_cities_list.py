#!/usr/bin/python3
"""creates a City & state objects from the database hbtn_0e_6_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).order_by(State.id).all()
    for row in data:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))
    session.commit()
    session.close()
