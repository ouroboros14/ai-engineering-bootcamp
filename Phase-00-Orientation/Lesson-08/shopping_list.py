grocery_items = ["Soap", "Toothpaste", "Bread", "Eggs", "Cooking Oil"]
print("The current shopping list has - " + str(grocery_items))

grocery_items.append("Milk")
print("The updated shopping list has - " + str(grocery_items))

grocery_items.remove("Cooking Oil")
print("The updated shopping list after removal has - " + str(grocery_items))

grocery_items[1] = "Toothbrush"
print("The updated shopping list after replacement has - " + str(grocery_items))

for item in grocery_items:
    print(item)