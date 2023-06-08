# PE02: Programming Exercise

## Instructions

`shopping_list.py``

### Description

This assignment is to gain knowledge on Linked List and Selection Sort. A shopping list will be implemented for this exercise. The program stores shopping items in both simple array or linked list. Each storing mechanism is separated into different files, such as "simple_array_shopping_list_manager.py" or "linked_list_shopping_list_manager.py," where each file contains FileNameClass classes with essential methods for data manipulation. Note that "shopping_list.py" with the "main" method has already been provided (download attachment). As part of the assignment, compare the actual runtime of insert/delete/lookup operation between two lists and justify in a short paragraph on how the algorithms perform. Keep in mind to always comment and document your class and methods.

### Documentation reference

Mertz, J. (n.d.). Documenting Python Code: A Complete Guide. <https://realpython.com/documenting-python-code/>

## Expected result

1. `shopping_list.py:`
   This is Main python file which is already provided and contains main and test procedure which calls methods implemented on "`simple_array_shopping_list_manager.py`" or "`linked_list_shopping_list_manager.py`" file to manage shopping items. (This is already provided, but please include this file on your submission).
2. `simple_array_shopping_list_manager.py`
   This is a file that includes the class of simple array based shopping list manager. This class contains such methods as `init`, `insert_item`, `print_items`, `delete_item`, `get_last_item`, `selection_sort`. Please keep in mind the following notes for each method during implementation:
    - `Init()`: initializes simple array to be used throughout object life.
    - `insert_item(item)`: inserts item at the front of the array. Parameters: item name. Note that you are allowed to use the `insert()` method from Python Array Module.
    - `print_items()`: simply prints item
    - `delete_item(item)`: deletes item. Parameters: item name. Note that for runtime study purpose, DO NOT use `remove()` method from Python Array module but you are allowed to use `pop()/index()` method
    - `get_last_item()`: returns the last item name from the simple array.
    - `selection_sort()`: sorts items on the array from the current object and replaces it with the newly sorted result.
3. `linked_list_shopping_list_manager.py`
   This is a file that includes the class of linked list based shopping list manager. This class contains such methods as `init`, `insert_item`, `print_items`, `delete_item`, `get_last_item`, `selection_sort`. In addition, this class requires the inner class to hold onto data as a linked list. Please keep in mind the following notes for each method during implementation:
    - `Init()`: initializes linked list object to be used throughout object life.
    - `insert_item(item)`: inserts item at the front of the linked list. Parameters: item name.
    - `print_items()`: simply prints item throughout linked list. Note that try to print as [ item1 item2 ] by using some combinations of "print(item, end = " ")".
    - `delete_item(item)`: deletes item. Parameters: item name.
    - `get_last_item()`: returns the last item name from the linked list.
    - `find_smallest()`: returns the smallest item from linked list. (ex. [ apple banana cheese] -> apple is smallest)

### TASK

As part of the assignment, compare the actual runtime of insert/delete/lookup operation between two lists and justify in a short paragraph on how and their performance.

## Example output

### Challenge question (not mandatory)

Implement the following selection sort for the linked list class. Note that this test case has been commented out on the Main class.

1. `find_smallest(linkedList)`: modification is required to take in the linked list object parameter, and returns the smallest item from the given linked list.
1. `selection_sort()`: sorts items on the linked list from the current object and replaces it with the newly sorted result.

---

# PE02

## Results

These are the returned results from running `shopping_list.py`

```bash
------ Simple array ------
current list:    ['fish', 'mushroom', 'beef', 'pork', 'carrot', 'cheese', 'butter', 'bread', 'milk', 'banana', 'apple']
delete milk:     ['fish', 'mushroom', 'beef', 'pork', 'carrot', 'cheese', 'butter', 'bread', 'banana', 'apple']
last element:   apple

Sorted(a to z):  ['apple', 'banana', 'beef', 'bread', 'butter', 'carrot', 'cheese', 'fish', 'mushroom', 'pork']
-insert: 2.750000567175448e-05
-delete: 4.4000043999403715e-06
-lookup: 2.300017513334751e-06

------ Linked list ------
current list:    [ fish mushroom beef pork carrot cheese butter bread milk banana apple ]
delete milk:     [ fish mushroom beef pork carrot cheese butter bread banana apple ]
last element:   apple

smallest element:       apple

Sorted(a to z):  [ apple banana beef bread butter carrot cheese fish mushroom pork ]
smallest element:       apple

-insert: 1.4599994756281376e-05
-delete: 6.89999433234334e-06
-lookup: 3.5999983083456755e-06
```

The results of running shopping_list.py show the comparison between the simple array implementation and the linked list implementation of a shopping list manager.

### simple array implementation

1. Insert operation took approximately 2.75e-05 seconds.
1. Delete operation took approximately 4.4e-06 seconds.
1. Lookup operation took approximately 2.3e-06 seconds.

### linked list implementation

1. Insert operation took approximately 1.46e-05 seconds.
1. Delete operation took approximately 6.9e-06 seconds.
1. Lookup operation took approximately 3.6e-06 seconds.

## Observations

- The insert operation is slightly faster in the linked list implementation compared to the simple array implementation.
- The delete operation is faster in the simple array implementation compared to the linked list implementation. This is because the linked list implementation has to traverse the list until it finds the item to delete, whereas the simple array implementation can directly access the item.
- The lookup operation is faster in the simple array implementation compared to the linked list implementation, as the array allows for direct access to the elements, while the linked list needs to traverse the list to find the desired item.

It is important to note that these results are specific to this particular case and may not be generalizable to all use cases. \
The performance of each implementation depends on various factors such as the size of the list, the distribution of the data, and the frequency of different operations.

## Smallest implementation

The smallest element in the shopping list are determined & sorted alphabetically. In this case, "apple" comes before all the other items in the list alphabetically, so it is considered the smallest element.

Comparing "apple" with "beef" or "pork", 'a' comes before 'b' and 'p', making "apple" the smallest element in the list.
This has nothing to do with the length of the words themselves.

## Implementation

### File #1 - SimpleArrayShoppingListManagerClass

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

### File #2 - LinkedListShoppingListManagerClass

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
