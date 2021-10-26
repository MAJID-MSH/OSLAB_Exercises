print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Hi')

temp = input("WRITE start TO BEGIN THE APP:")
while True:
    
    if temp == 'yes' or temp == 'start':
            n = int (input("Pls ENTER YOUR NUMBER :"))
            fibonacci_list = [0, 1]

            if n == 0 :
                print(fibonacci_list[0])

            elif n == 1 :
                print(fibonacci_list[1])

            else:
                for i in range(2, n+1):
                    fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
                print(fibonacci_list)

            print("Wanna Try Again With Another Number (yes or no):")
            temp = input()

    elif temp == 'no' or temp == 'credits':
            break

    else :
        print("Input is incorrect! try again")
        temp = input()

print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')