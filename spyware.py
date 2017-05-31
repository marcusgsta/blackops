#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Spyware(Product):
    """
    Spyware class
    """
    __tablename__ = 'spyware'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    spyware_name = Column(String)
    spyware_type = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'spyware'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Spyware, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.spyware_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.spyware_type = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Typ", self.spyware_type)
