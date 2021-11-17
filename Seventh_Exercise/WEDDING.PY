import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
result=[]

for i in range(len(boys)):

    tempB = random.choice(boys)
    boys.remove(tempB)
    tempG = random.choice(girls)
    girls.remove(tempG)
   
    m=(tempB,tempG)
    result.append(m)

print(result)
