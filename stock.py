#!/usr/bin/python3
"""
Stock class
"""

from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Stock(Base):
    """
    Stock class
    """
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(Integer)
    amount = Column(Float)
#    p_type = Column(String)

    def __init__(self, name, classification, amount):
        """
        constructor
        """
        self.name = name
        self.classification = classification
        self.amount = amount
