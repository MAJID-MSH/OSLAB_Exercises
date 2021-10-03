print('Hi')
print('HINT:\nWeight to KILOGRAM \nHeight to METER')
print('---------------------------------------------')

Weight =  float(input("Enter Your Weight: "))
Height =  float(input("Enter Your Height: "))
BMI = float( Weight/(Height*Height) )

if BMI < 18.5 :
    print('Your BMI is: ', BMI, '\nYour Condition is: Underweight')

if 18.5 <= BMI and BMI <= 24.9 :
    print('Your BMI is: ', BMI, '\nYour Condition is: Normal')

if 25 <= BMI and BMI <= 29.9 :
    print('Your BMI is: ', BMI, '\nYour Condition is: Overweight')

if 30 <= BMI and BMI <= 34.9 :
    print('Your BMI is: ', BMI, '\nYour Condition is: Obese')

if BMI >= 35 :
    print('Your BMI is: ', BMI, '\nYour Condition is: Extremely Obese')


print('\n   ----MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')

 