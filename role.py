#!/usr/bin/python3
"""
Role class
"""

class Role(object):
    """
    Classification class
    """

    def __init__(self):
        """
        constructor
        """
        self.roles = ["agent", "project_manager", "coordinator"]

    def add_role(self, new_role):
        """
        add role
        """
        self.roles.append(new_role)
        return self.roles

    def remove_role(self, role):
        """
        remove classification
        """
        self.roles.pop(role)
        return self.roles
