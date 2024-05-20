class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        """
        Inserts a key-value pair into the linked list.
        If the key already exists, updates the value.
        """
        if self.head is None:
            self.head = Node(key, value)
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                current = current.next
            if current.key == key:
                current.value = value  # Update existing key
            else:
                current.next = Node(key, value)

    def search(self, key):
        """
        Searches for a key in the linked list and returns its value.
        Returns None if the key is not found.
        """
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the linked list.
        """
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        """
        Simple hash function to calculate the index for a given key.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self.hash_function(key)
        self.table[index].insert(key, value)

    def search(self, key):
        """
        Searches for a key in the hash table and returns its value.
        """
        index = self.hash_function(key)
        return self.table[index].search(key)

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.
        """
        index = self.hash_function(key)
        return self.table[index].delete(key)


if __name__ == "__main__":
    hash_table = HashTable(10)
    
    # Inserting data
    hash_table.insert(53, 'Employee_1')
    hash_table.insert(43, 'Employee_2')
    hash_table.insert(23, 'Employee_3')
    hash_table.insert(13, 'Employee_4')

    # Searching data
    print("Search results:")
    print(hash_table.search(53))  # Output: Employee_1
    print(hash_table.search(43))  # Output: Employee_2
    print(hash_table.search(23))  # Output: Employee_3
    print(hash_table.search(13))  # Output: Employee_4
    print(hash_table.search(33))  # Output: None

    # Deleting data
    print("\nDeleting key 23:")
    hash_table.delete(23)
    print(hash_table.search(23))  # Output: None
    print(hash_table.search(13))  # Output: Employee_4
