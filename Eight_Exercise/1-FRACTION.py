class Fraction:
    def __init__(self,s=0,m=None):
        self.s = s
        self.m = m


    def show(self):
        print(self.s ,"/", self.m)
        if self.m == self.s:
            print("= 1")


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
        # if result.m == result.s:
        #     print(result.s ,"/" ,result.m , "= 1")    
        
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

s1 = int(input("ENTER (SOORAT) The numerator Of First Fraction : "))
m1 = int(input("ENTER (MAKHRAGE) Denominator Of First Fraction: "))
s2 = int(input("ENTER (SOORAT) The numerator Of Second Fraction: "))
m2 = int(input("ENTER (MAKHRAGE) Denominator Of Second Fraction: "))
a = Fraction(s1,m1)
b = Fraction(s2,m2)

su = a.sum(b)
print("sum is:")
su.show()

mu = a.mul(b)
print("Multiply is:")
mu.show() 

subb = a.sub(b)
print("subtraction is:")
subb.show()

divi = a.div(b)
print("Division is:")
divi.show()

# a = Fraction(1,2)
# a.show()
# b=Fraction(5,2)
# b.show()

# c = a.mul(b)
# c.show()
# d = a.sum(b)
# d.show()
# e= a.sub(b)
# e.show()
# f= a.div(b)
# f.show()
print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')
