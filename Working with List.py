
#Playing with List

shopping_list  = ["Milk", "Eggs", "Bread", "Butter "]
print(shopping_list)

#Accessing items 
shopping_list.append("cheese")
shopping_list.insert(1, "Juice")
shopping_list.insert(6, "Cocktail")
print(shopping_list)
position = shopping_list.index("Cocktail")
print(position)


#Updating items
shopping_list[0]= "Almond Milk"
print(shopping_list)

#Removing items
shopping_list.remove("Eggs")
print(shopping_list)

shopping_list.pop()
print(shopping_list)

print(shopping_list.pop(1))# This remove the index item and also returns it
print(shopping_list)

for item in shopping_list: 
    print(f" -{item}")

for index, item in enumerate(shopping_list):
    print(f"{index +1}. {item}")
shopping_list = ['apples', 'bananas', 'oranges']

#This will make sure the list is numbered from 1
for index, item in enumerate(shopping_list):
    print(f" {1 + index} {item}")

#List Methods
shopping_list.sort()
print(shopping_list)

shopping_list.reverse()
print(shopping_list)

shopping_list.clear()
print(shopping_list)
