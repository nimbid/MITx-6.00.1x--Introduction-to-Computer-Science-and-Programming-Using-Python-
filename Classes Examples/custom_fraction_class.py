class Fractions(object):

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)

    def getNum(self):
        return self.num

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        newNum = self.num * other.denom + self.denom*other.num
        newDenom = self.denom * other.denom
        return Fractions(newNum, newDenom)

    def __sub__(self, other):
            newNum = self.num * other.denom - self.denom*other.num
            newDenom = self.denom * other.denom
            return Fractions(newNum, newDenom)

    def convert_float(self):
        return self.getNum() / self.getDenom() 
