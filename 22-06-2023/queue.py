queue = []  # Initialize an empty list to represent the queue

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Quit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        item = input("Enter the element to enqueue: ")
        queue.append(item)
        print(f"Enqueued element: {item}")
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            item = queue.pop(0)
            print(f"Dequeued element: {item}")
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

print("Queue program has ended.")
