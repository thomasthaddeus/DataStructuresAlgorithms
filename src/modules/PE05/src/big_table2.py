"""big_table2.py

This module contains a hash table-based inventory manager.
"""

class HashTableInventory:
    """A class representing a hash table-based inventory manager."""

    def __init__(self, table_size):
        """
        Initialize the hash table with a given table size.

        Args:
            table_size (int): The size of the hash table.
            Unused in the current implementation as Python
            dictionaries handle table resizing internally.
        """
        self.inventory = {}

    def insert_item(self, item, price):
        """
        Insert an item and its price, or update the price if the item exists.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.
        """
        self.inventory[item] = price

    def print_items(self):
        """Print items and their prices in pairs."""
        for item, price in self.inventory.items():
            print((item, price), end=", ")

    def find_item(self, item):
        """
        Find the price of a given item.

        Args:
            item (str): The name of the item to look up

        Returns:
            float: The price of the item if found, None otherwise.
        """
        return self.inventory.get(item)
