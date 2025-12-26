 #Import Neded Dependencies 
#Step 1 : import needed moudles and 
import random 

#Step 2: Create function to generate questions
def questions_generator():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer  = num1  + num2 
    elif operator == '-':
        answer = num1 - num2 
    else: 
        answer = num1 * num2 
    return f" {num1} {operator} {num2} " , answer 

def Quiz_Game():
    score = 0
    rounds = 5  

    print ("\n Welcome to the Math Quiz Game! ")
    print(" Try answer these question correctly ") 

    for i in range(rounds):
        question, right_answer = questions_generator()
        print(f"\n  for Question number{i + 1} : {question}")
        user_answer  = int(input (" Your answer : "))

        if user_answer  == right_answer: 
            print (" Correct! ")
            score = score + 1   
        else:
            print(f"Wrong! The correcct answer is : {right_answer} ")

    print (f"\n --- Gave Over ---)")
    print(f" Your final score is : {score}/{rounds}")
    if score == rounds:
        print("Congratulations! Excellent results")
    elif score  == rounds // 2 or  score > rounds // 2 :
         print("Good job, you did well")
    else:
        print("Keep practicing! You can do better")

Quiz_Game()
    
