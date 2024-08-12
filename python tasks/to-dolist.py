todo_list = []
while True:
    # Display the menu
    print("\nTo-Do List Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        # Add item
        item = input("Enter the item to add: ")
        todo_list.append(item)
        print(f"'{item}' has been added to your to-do list.")
    
    elif choice == '2':
        # Remove item
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            # View list
            print("\nTo-Do List:")
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
            
            index = int(input("Enter the number of the item to remove: ")) - 1
            if 0 <= index < len(todo_list):
                removed_item = todo_list.pop(index)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid number. No item removed.")
    
    elif choice == '3':
        # View list
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
    
    elif choice == '4':
        # Exit
        print("Exiting the to-do list application.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
