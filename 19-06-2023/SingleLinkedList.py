class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def is_empty(self):
        return self.head is None
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
            
    def insert_at_pos(self,data,position):
        new_node=Node(data)
        if self.is_empty() or position<=0:
            self.insert_at_beg(data)
        else:
            current_node=self.head
            count=1
            while count<position and current_node.next is not None:
                current_node=current_node.next
                count+=1
            new_node.next=current_node.next
            current_node.next=new_node
    
    def del_at_beg(self):
        if self.is_empty():
            print("List is empty...")
        else:
            self.head=self.head.next
        
    def del_at_end(self):
        if self.is_empty():
            print("List is empty...")
        elif self.head.next is None:
            self.head=None
        else:
            current_node=self.head
            while current_node.next.next is not None:
                current_node=current_node.next
            current_node.next=None
            
    def del_at_pos(self,position):
        if self.is_empty():
            print("List is empty...")
        elif position<=0:
            self.del_at_beg()
        else:
            current_node=self.next
            count=1
            while count<position and current_node.next is not None:
                current_node=current_node.next
                count+=1
            if current_node.next is not None:
                current_node.next=current_node.next.next
                
    def del_item(self,data):
        if self.is_empty():
            print("List is empty...")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current_node=self.head
        prev=None
        while current_node:
            if current_node.data==data:
                prev.next=current_node.next
                return
            prev=current_node
            current_node=current_node.next
        print("Deletion failed. Value not found...")
            
    def display(self):
        if self.is_empty():
            print("List is empty...")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.data,end="->")
                current_node=current_node.next
            print("None")
            
linked_list=LinkedList()
while True:
    print("\nSingly Linked List Operations:")
    print("1. Insert at the end")
    print("2. Insert at the beginning")
    print("3. Insert at perticular position")
    print("4. Delete at beginning")
    print("5. Delete a value at perticular location")
    print("6. Delete at end")
    print("7. Delete a perticular value")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        data = int(input("Enter the data to insert at the beginning: "))
        linked_list.insert_at_beg(data)
        print("Node inserted at the beginning.")
    elif choice == 2:
        data = int(input("Enter the data to insert at the end: "))
        linked_list.insert_at_end(data)
        print("Node inserted at the end.")
    elif choice == 3:
        pos = int(input("Enter the position at which to insert: "))
        data = int(input("Enter the data to insert: "))
        linked_list.insert_at_pos(pos, data)
        print("Node inserted after the given position.")
    elif choice == 4:
        linked_list.del_at_beg()
        print("Beginninng value deleted.")
    elif choice == 5:
        data = int(input("Enter the location to delete: "))
        linked_list.del_at_pos(position)
    elif choice == 6:
        linked_list.del_at_end()
        print("End value deleted.")
    elif choice == 7:
        data = int(input("Enter value to delete: "))
        linked_list.del_item(data)
        print(f"{data} deleted from list.")
    elif choice == 8:
        linked_list.display()
    elif choice == 9:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")