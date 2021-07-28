class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
    '''
    Define __repr__, a special method that returns a string that looks like a
    valid Python expression that could be used to recreate an object with the same value.
    In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.
    '''
        return 'Coordinate(%d,%d)' % (self.x, self.y)
