import random
secret_number = random.randint(1,10)

print( 'hello you are welcome to my Guessing game! I am  thinking of a number between 0 and 11,can you guess the number')
attempts = 3

while attempts > 0 :
    guess = int(input('Enter your guess'))
    if guess == secret_number:
        print('Congratulations, You are right!')
        break
    elif guess < secret_number:
        print('You are too low,Try Again')
    else: 
        print('too high, Try Again ')
    attempts-=1
  
if attempts == 0 :
    print('You are out of attempts')



