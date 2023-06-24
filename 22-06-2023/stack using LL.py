class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot perform pop operation.")
        else:
            item = self.items.pop()
            print(f"Popped {item} from the stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot perform peek operation.")
        else:
            print(f"Top item: {self.items[-1]}")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:")
            for item in reversed(self.items):
                print(item)

# Create an instance of the Stack class
stack = Stack()

while True:
    print("\nSTACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item to push: ")
        stack.push(item)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
