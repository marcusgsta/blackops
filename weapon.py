#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Weapon(Product):
    """
    Clothes class
    """
    __tablename__ = 'weapon'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    weapon_name = Column(String)
    weapon_type = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'weapon'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
#        super(Weapon).__init__(arguments_list)
        super(Weapon, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.weapon_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.weapon_type = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Typ av vapen", self.weapon_type)
