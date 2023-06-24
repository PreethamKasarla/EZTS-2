class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = minValue(root.right)
        root.right = delete(root.right, root.key)
    return root

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Driver code
root = None

while True:
    print("\nBinary Tree Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        value = int(input("Enter the value to insert: "))
        root = insert(root, value)
        print("Node inserted successfully!")

    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        root = delete(root, value)
        print("Node deleted successfully!")

    elif choice == 3:
        value = int(input("Enter the value to search: "))
        result = search(root, value)
        if result:
            print("Value found in the tree!")
        else:
            print("Value not found in the tree!")

    elif choice == 4:
        print("Inorder Traversal:")
        inorder(root)

    elif choice == 5:
        print("Preorder Traversal:")
        preorder(root)

    elif choice == 6:
        print("Postorder Traversal:")
        postorder(root)

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
