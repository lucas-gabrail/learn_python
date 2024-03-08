# x=5
# print(x)
# y=4
# print(y)

# print("The sum of x and y is: ", x+y)
# e=7
# print(e)
# print("The sum of e and x is:  ", e+x)
      
# h=2
# print(h)
# print("The sum of h and y is: ",  h+y)
# r=8
# print(r)
# print("The sum of r and h is: ",  r+h)

# name = input('Enter your name:\n')

# print(name, "you are a piece of poop!")


import random

answer = random.randrange(1,11)
current_try = 1
max_tries = 3
print('Welcome to the number guessing game!')
print('I chose a number from 1 to 10, try to guess the number')
while current_try <= max_tries:
    user_guess = int(input())
    if user_guess == answer:
        print(f'You won! You got it in {current_try}')
        break
    else:
        if max_tries == current_try:
            print(f'You failed! The answer was: {answer}')
            break
        if user_guess > answer:
            print('Answer is lower')
        else:
            print('Answer is higher')
        print(f'You have {max_tries - current_try} tries left. Try again!')
        current_try += 1

