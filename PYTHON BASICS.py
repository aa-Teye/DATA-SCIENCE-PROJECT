name = "Alex "
age = 25
total_number = 276

print('name :',name)
print("age :", age)
print("the total number is",total_number)


# Taking UserInputs
username = input("what is your name?")
print("YOu are welcome ",username )
print("It is beautiful to have you with us ",username)


#Using conditional Statements:
user_age = int(input("Enter your age:  "))
if user_age >= 18:
    print("You are an adult")
elif user_age>= 13:
    print("You are a teenager ")
else:
    print("You are a minor")


#Iterations using While loops 
count = 0
while count < 10:
    print("Count is:", count)
    count = count +1


#Using For Loops 
powerful_games = ['game of thrones','the devil may cry','god of war']
for game in powerful_games:
    print('the name of selected game is ', game)


#Playing with Lists 
powerful_games.append("God's of Egypt")
powerful_games[1] = 'Final Quest'
print(powerful_games)


# Playing with Functions
def sayHello():
    print('hello from your very first function')

sayHello()
sayHello()


#Example 2 
def SayHello(name):
    print('hello!',name,'from your very first funtion')

SayHello('Vivian') 

def Multiply(a, b):
    return a*b

result = Multiply(20,30)
print('The result of the multiplication is',result)