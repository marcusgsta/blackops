#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Drone(Product):
    """
    Drone class
    """
    __tablename__ = 'drone'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    drone_name = Column(String)
    drone_type = Column(String)
    classification = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'drone'
    }

    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Drone, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.drone_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.drone_type = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Typ av dron", self.drone_type)
