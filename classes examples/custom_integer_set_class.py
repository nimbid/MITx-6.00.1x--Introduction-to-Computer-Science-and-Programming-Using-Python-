# Create a new type to represent a set of integers.
#  1. Initially the set is empty.
#  2. Each integer appears only once in the set- representational invariant
#     enforced by code.


class intSet(object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found.')

    def __str__(self):
        self.vals.sort()
        result = ''
        for i in self.vals:
            result = result + str(i) + ','
        return '{' + result[:-1] + '}'
