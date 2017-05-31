#!/usr/bin/python3
"""
Rented Material class
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///static/db/blackops.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

class RentedMaterial(Base):
    """
    Rented Material class
    """
    __tablename__ = "rented_material"

    id = Column(Integer, primary_key=True)
    person_name = Column(String)
    product_name = Column(String)
    amount = Column(Float)
    product_id = Column(Integer)

    def __init__(self, person_name, product_name, amount, product_id):
        """
        constructor
        """
        self.person_name = person_name
        self.product_name = product_name
        self.amount = amount
        self.product_id = product_id

    def get_material(self):
        """
        Get material with classification 3
        Rent material from stock to general manager
        """
        pass
