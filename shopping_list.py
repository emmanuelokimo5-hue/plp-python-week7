# Start with an empty shopping list
shopping_list = []

while True:
    print("\nMenu: add / remove / show / done")
    choice = input("Choose an option: ").lower()

    if choice == "add":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(item, "has been added.")

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose add, remove, show, or done.")