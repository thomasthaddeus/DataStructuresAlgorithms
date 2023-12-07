"""simple_array_shopping_list_manager.py

Author:     Thaddeus Thomas
Date:       2023-04-30
Class:      CS 469: Data Structures & Algorithms
Assignment: PE04

This module contains the SimpleArrayShoppingListManager class, which provides an implementation
of a shopping list manager using a simple array data structure. The class includes methods
for initializing the array, inserting items, printing items, and sorting the items using the
quick sort algorithm.

The SimpleArrayShoppingListManager class includes the following methods:

- __init__: Initializes the simple array to be used throughout the object's life.
- insert_item: Inserts an item at the front of the array.
- print_items: Returns the items in the array.
- quick_sort_helper: A helper method for the quick sort algorithm that sorts the array recursively.
- partition: Partitions the array for the quick sort algorithm.
- quick_sort: Sorts the items in the array using the quick sort algorithm and replaces the original
              array with the sorted result.
"""

class SimpleArrayShoppingListManager:
    """Manages a shopping list using a simple array."""

    def __init__(self):
        """Initializes an empty array to store shopping list items."""
        self.arr = []


    def insert_item(self, item):
        """Inserts an item at the front of the array.

        Args:
            item (str): The item to be added to the shopping list.
        """
        self.arr.insert(0, item)


    def print_items(self):
        """Prints the items in the shopping list."""
        for item in self.arr:
            print(item, end=" ")
        print()

    def quick_sort_helper(self, arr, low, high):
        """Recursively sorts the given array using the quick sort algorithm.

        Args:
            arr (list): The array to be sorted.
            low (int): The starting index of the array segment to be partitioned.
            high (int): The ending index of the array segment to be partitioned.

        Returns:
            list: The sorted array.
        """
        if low < high:
            piv = self.partition(arr, low, high)
            self.quick_sort_helper(arr, low, piv - 1)
            self.quick_sort_helper(arr, piv + 1, high)


    def partition(self, arr, low, high):
        """Partition the array for the quick sort algorithm.

        This method selects a 'pivot' element from the array and rearranges the elements
        in the array so that all elements smaller than the pivot are placed before the pivot,
        and all elements greater than the pivot are placed after it. The index of the pivot
        is returned.

        Args:
            array (list): The array to be partitioned.
            low (int): The starting index of the array segment to be partitioned.
            high (int): The ending index of the array segment to be partitioned.

        Returns:
            int: The index of the pivot element after partitioning.
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    def quick_sort(self):
        """Sorts the items in the shopping list using the quick sort algorithm."""
        self.quick_sort_helper(self.arr, 0, len(self.arr) - 1)
