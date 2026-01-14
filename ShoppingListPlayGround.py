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


#  PROJECT WORK:APPLYING CONCEPTS TO BUILDI AN ONLINE SHOPPING CART LOGIC APPLICATION
 #Creating A Onling Shopping Cart Logic Application 
#Step 1 Creating the empty cart to add items to purchase
cart = []

#Step2 Create the Continuous Loop Menu to Display Options to User 
def cart_menu():
    print("\n --- Shopping Cart Menu  ---")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Empty Cart")
    print("5. Exit")

#Creating the Program Loop
while True:
    cart_menu()
    user_choice = input("what will you want to do, (1-5): ")
    if user_choice ==  "1":
        print("\n --- Your Shopping Cart ---")
        if not cart:
            print(" Your cart is empty.")
        else:
            for index, item in enumerate(cart):
                print(f"{index + 1} .{item}")

    elif user_choice == "2":
        item =input("Enter item to be added to the cart: ")
        cart.append(item)
        print(f"{item} , has been added to your cart successfully. ")

    elif user_choice == "3":
        item = input("Enter the item to remove from the cart: ")
        if item in cart:
            cart.remove(item)
            print(f"{item}has been removed from your cart successfully.")
        else:
            print(f"{item} is not in your cart. ")

    elif user_choice == "4":
        cart.clear()
        print("Your cart has been emptied successfully.")  

    elif user_choice == "5":
        print("Thank you for shopping with us. Have a fruitful week")
        break
    
    else:
        print("Invalid choice, please enter a number between 1-5")

                  

