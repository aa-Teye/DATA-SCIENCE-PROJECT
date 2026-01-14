# lIST PLAYGROUND 

shopping_list = ["Bread", "Milk", "Eggs", "Butter"]
print("Shopping List:", shopping_list)
shopping_list.append("Cheese")
shopping_list.pop()

removed_item = shopping_list.pop()
print("The removed item is:", removed_item)
shopping_list.insert(2, "Chololin")
print("Updated Shopping List: ",shopping_list)


#LOOPING THROUGH LIST 
for item in shopping_list:
    print(f" {item} is in the shopping list.")

#Using Enumerate 
print("\n --- Bulleting the list with numbers: ---")
for index, item in enumerate(shopping_list):
    print(f"{index +1} {item} is in the shopping list")



 #Creating A Onling Shopping Cart Logic Application 
#Step 1 Creating the empty cart to add items to purchase
cart = []

#Step2 Create the Continuous Loop Menu to Display Options to User 
def cart_menu():
    print("\n --- Shopping Cart Menu  ---")
    print(1. View Cart)
    print(2. Add Item)
    print(3.Remove Item)
    print(4. Empty Cart)
    print(5. Exit)