import random

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Hi')

n = int(input("Please Enter Array Lenght :"))
Arr = []

for i in range(n) :
    temp = random.randint(0,100)
    
    if temp not in Arr:
        Arr.append(temp)


print('\nArray -->' , Arr)
print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')