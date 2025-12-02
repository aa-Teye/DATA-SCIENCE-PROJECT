import random 
secret_number = random.randint(1,20)
attempts = 5

print('Hello, welcome to the guess game')

while attempts > 0:
    guess = int(input('Enter your guess number'))
    if guess == secret_number:
        print('Congratulations you got it right')
        break
    elif guess < secret_number:
        print('low, please try Again ')
    else:
        print('high, please try again')
    attempts = attempts - 1
if attempts < 0 :
    print('You are out of chances')
