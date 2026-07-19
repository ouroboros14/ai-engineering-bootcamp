# Grocery Store Inventory Management - Phase 00 Final Project

print("==============================")
print("   Grocery Store Inventory    ")
print("==============================")

grocery_list = ["Milk", "Eggs", "Butter", "Cheese", "Bread"] # Initial grocery list with 5 items.

# To display the menu options repeatedly to the user.
while True:
    print("\n==============================")
    print("              MENU              ")
    print("==============================")
    print("1. Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Replace Item")
    print("5. Sort Inventory")
    print("6. Count Items")
    print("7. Exit")

    user_choice = input("Please select an option (1-7): ") # To store user's choice.

    # If the user chooses option 1, display the current inventory.
    if user_choice == "1":
        if len(grocery_list) == 0:
            print("\nInventory is empty.")
        else:
            print(f"\nCurrent Inventory ({len(grocery_list)} items):")
            for index, grocery in enumerate(grocery_list, start=1):
                print(f"{index}. {grocery}")

    # If the user chooses option 2, prompt for an item to be added to the inventory.
    elif user_choice == "2":
        new_item = input("Enter the item to be added: ").strip().title()
        if new_item in grocery_list:
            print(f"{new_item} already exists in the inventory.")
        else:
            grocery_list.append(new_item)
            print(f"{new_item} has been added to the inventory.")

    # If the user chooses option 3, prompt for an item to be removed from the inventory.
    elif user_choice == "3":
        remove_item = input("Enter the item to remove: ").strip().title()
        if remove_item in grocery_list:
            grocery_list.remove(remove_item)
            print(f"{remove_item} has been removed from the inventory.")
        else:
            print(f"{remove_item} is not in the inventory.")

    # If the user chooses option 4, prompt for an item to be replaced in the inventory.
    elif user_choice == "4":
        old_item = input("Enter the item to replace: ").strip().title()
        if old_item in grocery_list:
            new_item = input("Enter the new item: ").strip().title()
        elif old_item == new_item:
            print("Both items are the same.")
            index = grocery_list.index(old_item)
            grocery_list[index] = new_item
            print(f"{old_item} has been replaced with {new_item}.")
        else:
            print(f"{old_item} is not in the inventory.")

    # If the user chooses option 5, sort the inventory alphabetically.
    elif user_choice == "5":
        grocery_list.sort()
        print("Inventory has been sorted alphabetically.")

    # If the user chooses option 6, display the total number of items in the inventory.
    elif user_choice == "6":
        item_count = len(grocery_list)
        print(f"There are {item_count} items in the inventory.")

    # If the user chooses option 7, exit the program.
    elif user_choice == "7":
        print("\nThank you for using Grocery Store Inventory Manager!")
        print("Goodbye!")
        break

    # If the user enters an invalid option, display an error message.
    else:
        print("Invalid option. Please select a number between 1 and 7.")