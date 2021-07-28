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

    def __len__(self):
        counter = 0
        for i in self.vals:
            counter += 1
        return counter

    def intersect(self, otherpoint):
        '''
        Define an intersect method that returns a new intSet
        containing elements that appear in both sets.
        '''
        common_elements = intSet()
        if len(self.vals) <= len(otherpoint.vals):
            for elem in self.vals:
                if otherpoint.member(elem) ==  True:
                    common_elements.insert(elem)
        else:
            for elem in otherpoint.vals:
                if self.member(elem) == True:
                    common_elements.insert(elem)
        return common_elements
