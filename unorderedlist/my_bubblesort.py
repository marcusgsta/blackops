"""
The bubble_sort function
"""
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
