#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Firstaid(Product):
    """
    FirstAid class
    """
    __tablename__ = 'firstaid'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    firstaid_name = Column(String)
    firstaid_type = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'firstaid'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Firstaid, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.firstaid_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.firstaid_type = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Typ", self.firstaid_type)
