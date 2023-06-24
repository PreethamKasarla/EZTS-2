stack = []  # Initialize an empty list to represent the stack

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:  # Push operation
        element = input("Enter the element to push: ")
        stack.append(element)
        print(f"Element '{element}' pushed onto the stack.")

    elif choice == 2:  # Pop operation
        if not stack:
            print("Stack is empty. Cannot pop from an empty stack.")
        else:
            popped_element = stack.pop()
            print(f"Popped element: {popped_element}")

    elif choice == 3:  # Display operation
        if not stack:
            print("Stack is empty.")
        else:
            print("Elements in the stack:")
            for element in reversed(stack):
                print(element)

    elif choice == 4:  # Exit the program
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1-4).")
