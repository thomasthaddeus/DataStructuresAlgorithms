# Modules PE02

## Implementation of the SimpleArrayShoppingListManagerClass and LinkedListShoppingListManagerClass:

### File #1

```py
"""
File: simple_array_shopping_list_manager.py
Author: [Your Name]
Date: [Creation Date]
Description: This module provides a class for managing a shopping list using a simple array.
"""

from array import array

class SimpleArrayShoppingListManagerClass:
    """
    Class: SimpleArrayShoppingListManagerClass
    Purpose: Provides functionality to manage a shopping list using a simple array.
    """

    def init(self):
        """
        Method: init
        Purpose: Initializes the simple array to be used throughout the object's life.
        """
        self.items = array('u', [])

    def insert_item(self, item):
        """
        Method: insert_item
        Purpose: Inserts an item at the front of the array.
        Parameters: item (str) - The name of the item to be inserted.
        """
        self.items.insert(0, item)

    def print_items(self):
        """
        Method: print_items
        Purpose: Prints all the items in the array, separated by spaces.
        """
        for item in self.items:
            print(item, end=" ")
        print()

    def delete_item(self, item):
        """
        Method: delete_item
        Purpose: Deletes an item from the array.
        Parameters: item (str) - The name of the item to be deleted.
        """
        index = self.items.index(item)
        self.items.pop(index)

    def get_last_item(self):
        """
        Method: get_last_item
        Purpose: Returns the last item name from the simple array.
        Returns: str - The name of the last item in the array.
        """
        return self.items[-1]

    def selection_sort(self):
        """
        Method: selection_sort
        Purpose: Sorts items in the array using the selection sort algorithm.
        """
        for i in range(len(self.items)):
            min_idx = i
            for j in range(i+1, len(self.items)):
                if self.items[min_idx] > self.items[j]:
                    min_idx = j
            self.items[i], self.items[min_idx] = self.items[min_idx], self.items[i]

```

### File #2

```py
"""linked_list_shopping_list_manager.py"""

class LinkedListShoppingListManagerClass:
class Node:
def init(self, item):
self.item = item
self.next = None

python
Copy code
def __init__(self):
    self.head = None

def insert_item(self, item):
    new_node = self.Node(item)
    new_node.next = self.head
    self.head = new_node

def print_items(self):
    current = self.head
    while current:
        print(current.item, end=" ")
        current = current.next
    print()

def delete_item(self, item):
    if self.head and self.head.item == item:
        self.head = self.head.next
        return

    current = self.head
    while current.next:
        if current.next.item == item:
            current.next = current.next.next
            return
        current = current.next

def get_last_item(self):
    current = self.head
    while current.next:
        current = current.next
    return current.item

def find_smallest(self):
    smallest = self.head.item
    current = self.head.next
    while current:
        if current.item < smallest:
            smallest = current.item
        current = current.next
    return smallest
```

Note: The selection sort for the linked list is not implemented in this solution as it is not efficient for linked lists.
Comparing the runtime of insert/delete/lookup operations between the simple array and the linked list:

Insert operation:

Simple array: In the worst case, the insert operation takes O(n) time due to the need to shift elements when inserting at the front.
Linked list: The insert operation is constant time O(1) as it only requires updating pointers.
Delete operation:

Simple array: The delete operation takes O(n) time in the worst case, as the need to find the item's index and shift the elements after the deleted item.
Linked list: The delete operation takes O(n) time in the worst case, as the need to traverse the list and update the pointers.
Lookup operation (last element):

Simple array: The lookup operation is constant time O(1) as it directly accesses the last element using its index.
Linked list: The lookup operation takes O(n) time in the worst case, as the need to traverse the list to find the last element.
In conclusion, the linked list is more efficient for insert operations, while the simple array is more efficient for the lookup operation (for the last element). The delete operation has the same complexity for both data structures. However, the actual runtime can be different due to factors such as the underlying memory allocation and the size of the data. The selection sort is not recommended for the linked list because it requires a lot of pointer manipulation, and there are more efficient sorting algorithms for linked lists, such as merge sort.

In conclusion, the choice between a simple array and a linked list for managing a shopping list depends on the specific use case and the operations that will be performed most frequently. If insertions and deletions are more common, a linked list may be more efficient. However, if direct access to elements is a priority, a simple array may be a better choice.
