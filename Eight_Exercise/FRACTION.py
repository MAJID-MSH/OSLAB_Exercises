
class Fraction:
    def __init__(self,s=0,m=None):
        self.s = s
        self.m = m

    def show(self):
        print(self.s ,"/", self.m)


    def sum(self , other):
        result = Fraction()
        result.s = self.s * other.m + self.m * other.s
        result.m = self.m * other.m
        return result

    def mul(self , y):
        result = Fraction()
        result.s = self.s * y.s
        result.m = self.m * y.m
        return result
        #return Fraction(x.s * y.s , x.m * y.m)

    def sub(self , other):
        result = Fraction()
        result.s = self.s*other.m - self.m*other.s
        result.m = self.m*other.m
        return result

    def div(self , other):
        result = Fraction()
        result.s = self.s*other.m
        result.m = self.m*other.s
        return result

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('^^^^^^^^^^^^^^^^FRACTION CALCULATOR^^^^^^^^^^^^^^^^^')
print('Hi')
a = Fraction(1,9)
a.show()

b=Fraction(22,6)
b.show()

c = a.mul(b)
c.show()

d = a.sum(b)
d.show()

e= a.sub(b)
e.show()

f= a.div(b)
f.show()


print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')