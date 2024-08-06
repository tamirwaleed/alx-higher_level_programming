#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
            pool_pre_ping=True)
    State.cities = relationship("City",
                                order_by=City.id, back_populates='state')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for x in data:
        print("{}: ({}) {}".format(x[1].name, x[0].id, x[0].name))
    session.close()
