"""big_table1.py

This module contains a hash table-based inventory manager.
"""

class HashTableInventory:
    """A class representing a hash table-based inventory manager."""

    def __init__(self, table_size):
        """
        Initialize the hash table with a given table size.

        Args:
            table_size (int): The maximum size of the hash table.
        """
        self.inventory = {}
        self.table_size = table_size

    def insert_item(self, item, price):
        """
        Insert an item and its price, or update the price if the item exists.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.
        """
        if len(self.inventory) < self.table_size or item in self.inventory:
            self.inventory[item] = price
        else:
            print("Inventory is full. Cannot insert new item.")

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
