#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Clothes(Product):
    """
    Clothes class
    """
    __tablename__ = 'clothes'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    clothes_name = Column(String)
    storlek = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'clothes'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Clothes, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.clothes_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.storlek = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("storlek", self.storlek)
