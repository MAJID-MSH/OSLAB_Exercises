def checkered_page (n , m):
    for r in range (n):
        for c in range (m):
            if r % 2 == 0 :
                if c % 2 == 0 :
                    print('#', end='')
                else:
                    print('*', end='')
            else :
                if c % 2 == 0:
                    print('*', end='')
                else:
                    print('#', end='')
        print()



print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Hi')

temp = input("WRITE start TO BEGIN THE SHOW :")
while True:
    
    if temp == 'yes' or temp == 'start':
            n = int (input("ENTER ROW NUMBER :"))
            m = int (input("ENTER COLUMN NUMBER :"))
            checkered_page(n,m)
            print("Wanna Try Again With Another Number (yes or no):")
            temp = input()

    elif temp == 'no':
            break

    else :
        print("Input is incorrect! try again")
        temp = input()


print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')
