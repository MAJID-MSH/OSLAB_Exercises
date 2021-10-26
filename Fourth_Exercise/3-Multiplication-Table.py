def Multi (n , m):
    for i in range(1 , n+1):
        for j in range(1 , m+1):
            print( i*j , end='\t')
        print()


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Hi')

print("start--> TO BEGIN THE APP")
print("credits--> TO SHOW DEVELOPER AND EXIT")

temp = input("ENTER YOURS CHOICE :")
while True:
    
    if temp == 'yes' or temp == 'start':
            n = int (input("ENTER ROW NUMBER :"))
            m = int (input("ENTER COLUMN NUMBER :"))
            Multi(n , m)
            print("Wanna Try Again With Another Number (yes or no):")
            temp = input()

    elif temp == 'no' or temp == 'credits':
            break

    else :
        print("Input is incorrect! try again")
        temp = input()


print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')