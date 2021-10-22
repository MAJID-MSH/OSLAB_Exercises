import random

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

word_storage = [ 'bitcoin' , 'gamingsetup' ,  'cardano' , 'maxpain' , 'battlefield' , 'destiny' , 'halo'  , 'satoshi' , 'blockchain']
word = random.choice(word_storage)
print(word)

HP = len(word)
user_guess = []

while True:
    temp = 0
    print('Your HP -->' , HP)
    
    for char in word:
        if char in user_guess:
            print(char , end=' ')
            temp +=1
        else:
            print('-- ', end=' ')

    if temp == len(word):
        print('\n==================================')
        print('_____congratulation MyFRIEND YOU WON!!!_____')
        break

    if HP == 0 :
        print('\n==================================')
        print('_____GAME OVER MY FRIEND !!!!_____')
        break

    user_en = input('\n\nPlease Enter a Letter :')
    
    if user_en in word:
        user_guess.append(user_en)
    else:
        HP -= 1

print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')