class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Queue:
    def _init_(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

# Main program
queue = Queue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter the element to enqueue: ")
        queue.enqueue(data)
        print("Element enqueued.")
    elif choice == "2":
        data = queue.dequeue()
        if data is not None:
            print("Dequeued element:", data)
    elif choice == "3":
        print("Queue elements:")
        queue.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")