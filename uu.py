import random
t = str(input('enter difficulty level\n 1.easy\n 2.medium\n 3.hard'))
a = 0
if t == '1':
    hidden = random.randint(0, 21)
    for a in range(1, 6):
        guess = int(input('guess the number from 0 to 20'))
        if guess < hidden:
            print('you are too low')

        elif guess == hidden+1:
            print('you are close')

        elif guess == hidden-1:
            print('you are close')

        elif guess > hidden:
            print('you are too high')
        elif guess == hidden:
            print('hit! you are a winner')
            break


elif t == '2':
    hidden1 = random.randint(0, 501)
    for a in range(1, 6):
        guess = int(input('guess the number from 0 to 500'))
        if guess < hidden1:
            print('you are too low')

        elif guess == hidden1+1:
            print('you are close')

        elif guess == hidden1-1:
            print('you are close')

        elif guess > hidden1:
            print('you are too high')
        elif guess == hidden1:
            print('hit! you are a winner')
            break
elif t == '3':
    hidden2 = random.randint(0, 1001)
    for a in range(1, 11):
        guess = int(input('guess the number from 0 to 1000'))
        if guess < hidden2:
            print('you are too low')
        elif guess > hidden2:
            print('you are too high')
        elif guess == hidden2:
            print('hit! you are a winner')
            break
