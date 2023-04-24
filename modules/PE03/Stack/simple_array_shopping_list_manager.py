"""simple_array_shopping_list_manager.py

Author: Thaddeus Thomas
Date:   2023-04-23
Description:

"""

class SimpleArrayShoppingListManager:
    """
    A class to manage a shopping list using a simple array-based implementation.
    """

    def __init__(self):
        """
        Initializes the list of items.
        """
        self.items = []

    def insert_item(self, item):
        """
        Inserts a new item into the shopping list at the beginning.

        Args:
            item: The item to be inserted.
        """
        self.items.insert(0, item)

    def print_items(self):
        """
        Prints the items in the shopping list.
        """
        for item in self.items:
            print(item, end=" ")
        print()
