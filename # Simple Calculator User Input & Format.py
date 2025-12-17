# Simple Calculator  User Input & Formatted Output
a = 20
b = 10

print("\n ------Simple Calculator ------")
print(f"Addition: {a+b}")
print(f"Subsraction: {a-b}")
print(f"Multiplication: {a *b}")
print(f"Division: {a/b}")
print(f"floor Division: {a//b}")
print(f"Modulus: {a%b}")
print(f"Exponentiation: {a**b}")


#Simple Calculator 

#Get User Input
number1 = float(input("\n Enter first number: "))
number2 = float(input("\n Enter second number: ")) 

#Perform Arithmetic Operations
additon = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_division = number1 // number2
modulus = number1 % number2
exponentiation = number1 ** number2 

#Display the results
print("\n ---Simple Calculator Results ---")
print(f"Addition: {additon}")
print(f"Substraction: {substraction}")
print(f"Multiplication: {multiplication}")      
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
print("\n Thank you for using the Simple Calculator!")
