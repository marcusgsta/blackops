#!/usr/bin/python3
"""
Mapping of class
"""
from product import Product
from sqlalchemy import Column, String, Integer, ForeignKey

class Car(Product):
    """
    Car class
    """
    __tablename__ = 'car'
    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    car_name = Column(String)
    classification = Column(Integer)
    car_type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'car'
    }


    def __init__(self, arguments_list, classification):
        """
        constructor
        """
        super(Car, self).__init__(arguments_list)
        self.name = arguments_list[0]
        self.car_name = arguments_list[0]
        self.p_type = arguments_list[1]
        self.price = arguments_list[2]
        self.car_type = arguments_list[3]
        self.classification = classification

    def get_specific(self):
        """
        Get specific attribute for this class
        to use as a table
        """
        return ("Typ av bil", self.car_type)
