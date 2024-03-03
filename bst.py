import random
from tabulate import tabulate

class TreeNode:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.left = None
        self.right = None

class BSTIndex:
    def __init__(self):
        self.root = None

    # Method to insert a new node into the BST
    def insert(self, key, record):
        self.root = self._insert_recursively(self.root, key, record)

    def _insert_recursively(self, root, key, record):
        if root is None:
            return TreeNode(key, record)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key, record)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key, record)
        return root

    # Method to delete a node from the BST
    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursively(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._find_minimum(root.right)
            root.key = min_node.key
            root.record = min_node.record
            root.right = self._delete_recursively(root.right, min_node.key)
        return root

    def _find_minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    # Method to search for a node in the BST
    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)

    # Method to traverse the tree and return student records
    def get_student_records(self):
        records = []
        self._traverse(self.root, records)
        return records

    def _traverse(self, root, records):
        if root is None:
            return
        self._traverse(root.left, records)
        records.append(root.record)
        self._traverse(root.right, records)

# Function to display menu options
def display_menu():
    print("\nMenu:")
    print("1. Search for a student record")
    print("2. Delete a student record")
    print("3. Display all student records")
    print("4. Exit")

# Function to display student records in a table format
def display_student_records(records):
    print("\nStudent Records:")
    headers = ["ID", "Name", "Additional Info"]
    print(tabulate(records, headers=headers, tablefmt="grid"))

# List of Hindu god names
hindu_gods = ["Shiva", "Vishnu", "Durga", "Ganesha", "Krishna", "Saraswati", "Lakshmi", "Hanuman", "Kali", "Brahma"]

# List of additional information about Hindu gods in three words
hindu_gods_info = {
    "Shiva": "Destroyer of evil",
    "Vishnu": "Preserver of the universe",
    "Durga": "Goddess of power and strength",
    "Ganesha": "Remover of obstacles",
    "Krishna": "God of compassion and love",
    "Saraswati": "Goddess of knowledge and arts",
    "Lakshmi": "Goddess of wealth and prosperity",
    "Hanuman": "Symbol of devotion and courage",
    "Kali": "Goddess of time and death",
    "Brahma": "Creator of the universe"
}

# List of random words
random_words = ["happy", "sunshine", "delight", "serene", "adventure", "glow", "breeze", "serendipity", "charm", "sparkle"]

# Generate a dataset of 10 student records with sequential IDs and randomly assign a Hindu god name to each student
student_records = []
for i in range(1, 11):
    student_id = i
    name = random.choice(hindu_gods)
    additional_info = hindu_gods_info[name]
    student_records.append([student_id, name, additional_info])

# Create a BST index based on student IDs
bst_index = BSTIndex()
for student_id, name, additional_info in student_records:
    bst_index.insert(student_id, [student_id, name, additional_info])

# Main loop for user interaction
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        search_key = int(input("Enter the student ID to search: "))
        result = bst_index.search(search_key)
        if result:
            print(f"Student record found: {result.record}")
        else:
            print("No student record found for the provided ID.")

    elif choice == "2":
        delete_key = int(input("Enter the student ID to delete: "))
        bst_index.delete(delete_key)
        print(f"Student record with ID {delete_key} deleted.")

    elif choice == "3":
        records = bst_index.get_student_records()
        display_student_records(records)

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")