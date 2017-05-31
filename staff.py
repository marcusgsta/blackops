#!/usr/bin/python3
"""
Mapping of class
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Staff(Base):
    """
    Staff class
    """
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    list_of_staff = []
    # All staff gets 2 pair of shoes, just to show inheritance
    shoes = 2

    def __init__(self, name, role):
        """
        constructor
        """
        self.name = name
        self.role = role
#        super(Staff, self).__init__()

    def __str__(self):
        pass
#        return "Namn: {n}, Roll: {r}".format(n=self.name, r=self.role)

