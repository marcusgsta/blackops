#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Shoes(Product):
    """
    Shoes class
    """
    __tablename__ = 'shoes'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    shoes_name = Column(String)
    storlek = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'shoes'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Shoes, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.shoes_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.storlek = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Storlek", self.storlek)

