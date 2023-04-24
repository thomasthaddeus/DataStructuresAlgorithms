"""
File:           simple_array_shopping_list_manager.py
Author:         Thaddeus Thomas
Date:           2023-04-11
Description:    This module provides a class for managing a shopping list
                using a simple array.
"""

class SimpleArrayShoppingListManagerClass:
    """
     This class manages a shopping list using a simple array implementation
    """

    def __init__(self):
        """
        initialize an empty list to store items
        initialize the index attribute
        """
        self.items = []
        self.index = None

    def insert_item(self, item):
        """
        Insert a new item at the beginning of the list.
        """
        self.items.insert(0, item)

    def print_items(self):
        """
        Prints the list of items
        """
        print(self.items)

    def delete_item(self, item):
        """
        Delete the specified item from the list
        """
        index = self.items.index(item)
        self.items.pop(index)

    def get_last_item(self):
        """
        Get the last item in the list
        """
        return self.items[-1]

    def selection_sort(self):
        """
        Sort the list using the selection sort algorithm
        """
        for i, item in enumerate(self.items):
            min_idx = i
            for j, _ in enumerate(self.items[i+1:], start=i+1):
                if self.items[min_idx] > _:
                    min_idx = j
            self.items[i], self.items[min_idx] = self.items[min_idx], item

    def find_smallest(self):
        """
        Returns the smallest item from the array.
        """
        if not self.items:
            return None

        smallest_item = self.items[0]

        for item in self.items:
            if item < smallest_item:
                smallest_item = item

        return smallest_item
