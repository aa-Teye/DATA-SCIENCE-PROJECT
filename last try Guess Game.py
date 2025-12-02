import random
secret_number = random.randint(1,10)
attempts = 3

print("Welcome to the Guessing Game!")
while attempts > 0 :
    guess = int(input('Enter the Secret number '))
    if guess == secret_number:
        print('congratulations, you got it right')
    elif guess < secret_number:
        print('Nope! Too low ')
    else:
        print('NOpe! Too high')
    attempts = attempts - 1 
if attempts == 0 :
    print('Sorry! Out of attempts')
    


