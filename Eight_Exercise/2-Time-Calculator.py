class Time:
    
    def __init__(self, h=None, m=None, s=None):
        self.hour = h
        self.minute = m
        self.second = s


    def fix(self):

        if self.second>=60:
            self.second-=60
            self.minute+=1
        elif self.minute>=60:
            self.minute-=60
            self.hour+=1

        if self.second<0:
            self.minute-=1
            self.second+=60
        elif self.minute<0:
            self.hour-=1
            self.minute+=60


    def sum(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.fix()
        return result


    def sub(self, other):
        result = Time()
        result.hour = self.hour - other.hour
        result.minute = self.minute - other.minute
        result.second = self.second - other.second
        result.fix()
        return result


    def SecToHour(self):
        result = Time()
        result.hour=int (self.second/3600)
        Second=self.second%3600
        result.minute=int (Second/60)
        result.second=Second%60
        return result


    def HourToSec(self):
        print(self.hour*3600 + self.minute*60 + self.second)


    def show(self):
        print(self.hour ,":",self.minute,":", self.second)


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('^^^^^^^^^^^^^^^^TIME CALCULATOR^^^^^^^^^^^^^^^^^')
print('Hi')

h1 = int(input("ENTER Hours Of The First  : "))
m1 = int(input("ENTER Minute Of The First : "))
s1 = int(input("ENTER Second Of The First : "))
h2 = int(input("ENTER Hours Of The Second  : "))
m2 = int(input("ENTER Minute Of The Second : "))
s2 = int(input("ENTER Second Of The Second : "))
t1 = Time(h1,m1,s1)
t2 = Time(h2,m2,s2)

x=int(input("Enter seconds (For Convert To Time): "))
t3=Time(0,0,x)

print("Your First Entered Time: ")
t1.show()
print("Your Second Entered Time: ")
t2.show()
print("Sum of your Times:")
out1 = t1.sum(t2)
out1.show()
print("subtraction of your Times:")
out2 = t1.sub(t2)
out2.show()
print("Your First Entered Time To Second:")
t1.HourToSec()
print("Your Second Entered Time To Second:")
t2.HourToSec()

print("======================================")
print("your Converted Time(second to hours) :")
out3=t3.SecToHour()
out3.show()
print("======================================")

print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')