#Creating a shopping List Applicaton that allows users to add, remove, view, and clear items from their shopping list.

#Creating an empty shopping list
shopping_list =[]

#Function to Create Menu
def  Shopping__menu():
    print("\n ----- Shopping List Menu ----")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear list")
    print("5. Exit")

# The Program Loop Menu
while True:
    Shopping__menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1" :
        print("\n ----- Shopping List ----")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index , item in enumerate(shopping_list):
                print(f"{1+ index}. {item}")
    elif choice == "2":
        item = input("Enter the item to add ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item } has been removed from the shopping list. ")
        else:
            print(f"{item} is not in the shopping list.")
    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared.")
    elif choice == "5":
        print("Thank you for shopping with us. Goodbye!")
        break 
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

