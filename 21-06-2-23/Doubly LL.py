class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                if current.next:
                    new_node.next = current.next
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
                break
            current = current.next
        else:
            print(f"Key '{key}' not found in the list.")

    def delete_at_beginning(self):
        if self.is_empty():
            print("List is empty. Unable to delete.")
        else:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty. Unable to delete.")
        else:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None

    def delete_key(self, key):
        if self.is_empty():
            print("List is empty. Unable to delete.")
        else:
            current = self.head
            while current:
                if current.data == key:
                    if current.prev:
                        current.prev.next = current.next
                        if current.next:
                            current.next.prev = current.prev
                    else:
                        self.head = current.next
                        if current.next:
                            current.next.prev = None
                    break
                current = current.next
            else:
                print(f"Key '{key}' not found in the list.")

    def display(self):
        if self.is_empty():
            print("List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


# Create a new doubly linked list
dll = DoublyLinkedList()

# Perform operations on the doubly linked list
while True:
    print("\nDoubly Linked List Operations:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert after a key")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete a key")
    print("7. Display the list")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        data = input("Enter the element to insert at the beginning: ")
        dll.insert_at_beginning(data)
    elif choice == 2:
        data = input("Enter the element to insert at the end: ")
        dll.insert_at_end(data)
    elif choice == 3:
        key = input("Enter the key after which element should be inserted: ")
        data = input("Enter the element to insert: ")
        dll.insert_after(key, data)
    elif choice == 4:
        dll.delete_at_beginning()
    elif choice == 5:
        dll.delete_at_end()
    elif choice == 6:
        key = input("Enter the key to delete: ")
        dll.delete_key(key)
    elif choice == 7:
        print("Doubly Linked List: ", end="")
        dll.display()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please enter a valid option.")