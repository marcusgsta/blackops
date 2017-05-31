#!/usr/bin/env python3

"""
Unordered list class
"""

# Imports
from node import Node


class UnorderedList:
    """
    Unordered list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if list is empty
        """
        return self.head is None

    def add(self, item):
        """
        Add item to list
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        Return size of list
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def set(self, index, newdata):
        """
        Set node-data in list at specific index
        """
        # Här gäller det att sätta nodens data till 'newdata' på rätt
        # index-position. För att stega i listan kan du titta på metoden 'size()'

        counter = 0
        current = self.head
        while current != None:
            if counter == index:
                current.data = newdata
            current = current.get_next()
            counter = counter + 1


    def get(self, index):
        """
        Returns node data based on index
        """
        # Likt 'set()' gäller det att traversera listan men här ska du
        # returnera datan för värdet på rätt index-plats
        counter = 0
        current = self.head
        while current != None:
            if counter == index:
                return current.data
            current = current.get_next()
            counter = counter + 1


    def search(self, item):
        """
        Returns True if item found, else return False
        """
        # Här ska du returnera en bool (True/False)
        # beroende på om 'item' finns i listan
        aList = []
        current = self.head
        while current:
            aList.append(current.data)
            current = current.get_next()
        return item in aList

    def print_list(self):
        """
        Prints each item in list
        """
        # Traversera listan och gör en print() på varje element

        current = self.head
        while current != None:
            print(current.data)
            current = current.get_next()


    def remove(self, item):
        """
        Removes item from list
        """
        # Traversera listan och håll koll på föregående nod
        # och nästa nod. Om nuvarande 'data' är samma som 'item'
        # gäller det att koppla ihop föregående med nästa.

        # Tips! Om föregående är 'None' gäller det att koppla 'self.head' till nästa nod.
        current = self.head
        previous = None

        while current != None:
            if previous is None and current.data == item:
                self.head = self.head.get_next()
                previous = self.head
            elif current.data == item:
                previous.set_next(current.get_next())
            elif previous is None:
                previous = self.head
            else:
                previous = previous.get_next()
            current = current.get_next()


    def bubble_sort(self):
        """ Bubble sort """
        for i in range(self.size()):
            for j in range(self.size()-1-i):
                if self.get(j) > self.get(j+1):
                    temp = self.get(j)
                    self.set(j, self.get(j+1))
                    self.set(j+1, temp)

                    # Byt plats

        return self


class OrderedList:
    """
    Ordered list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if list is empty
        """
        return self.head is None

    def add(self, item):
        """
        Add item to list
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.bubble_sort()

    def size(self):
        """
        Return size of list
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def set(self, index, newdata):
        """
        Set node-data in list at specific index
        """
        # Här gäller det att sätta nodens data till 'newdata' på rätt
        # index-position. För att stega i listan kan du titta på metoden 'size()'

        counter = 0
        current = self.head
        while current != None:
            if counter == index:
                current.data = newdata
            current = current.get_next()
            counter = counter + 1


    def get(self, index):
        """
        Returns node data based on index
        """
        # Likt 'set()' gäller det att traversera listan men här ska du
        # returnera datan för värdet på rätt index-plats
        counter = 0
        current = self.head
        while current != None:
            if counter == index:
                return current.data
            current = current.get_next()
            counter = counter + 1


    def search(self, item):
        """
        Returns True if item found, else return False
        """
        # Här ska du returnera en bool (True/False)
        # beroende på om 'item' finns i listan
        aList = []
        current = self.head
        while current:
            aList.append(current.data)
            current = current.get_next()
        return item in aList

    def print_list(self):
        """
        Prints each item in list
        """
        # Traversera listan och gör en print() på varje element

        current = self.head
        while current != None:
            print(current.data)
            current = current.get_next()


    def remove(self, item):
        """
        Removes item from list
        """
        # Traversera listan och håll koll på föregående nod
        # och nästa nod. Om nuvarande 'data' är samma som 'item'
        # gäller det att koppla ihop föregående med nästa.

        # Tips! Om föregående är 'None' gäller det att koppla 'self.head' till nästa nod.
        current = self.head
        previous = None

        while current != None:
            if previous is None and current.data == item:
                self.head = self.head.get_next()
                previous = self.head
            elif current.data == item:
                previous.set_next(current.get_next())
            elif previous is None:
                previous = self.head
            else:
                previous = previous.get_next()
            current = current.get_next()


    def bubble_sort(self):
        """ Bubble sort """
        for i in range(self.size()):
            for j in range(self.size()-1-i):
                if self.get(j) > self.get(j+1):
                    temp = self.get(j)
                    self.set(j, self.get(j+1))
                    self.set(j+1, temp)

                    # Byt plats

        return self
