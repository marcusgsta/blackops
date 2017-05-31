#!/usr/bin/python3
"""
Mapping of class
"""

from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base, object):
    """
    Product class
    """

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    p_type = Column(String)
    price = Column(Float)

    __mapper_args__ = {
        'polymorphic_identity':'product',
        'polymorphic_on':p_type
    }

    def __init__(self, arguments_list):
        """
        constructor
        """
        self.name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]

#    def __init__(self, name, p_type, price):
#        """
#        constructor
#        """
#        self.name = name
#        self.p_type = p_type
#        self.price = price
