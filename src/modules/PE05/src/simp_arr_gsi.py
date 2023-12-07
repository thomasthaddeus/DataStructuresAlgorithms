# Author:       Thaddeus Thomas
# Date:         2023-05-07
# Assignment:   PE05 Hash Tables
# Project:      Data Structures & Algorithms
# Repository:   https://github.com/thomasthaddeus/
"""simp_arr_gs.py

This module implements a simple array-based inventory manager.

Classes:
    SimpleArrayInventory: Represents a simple array-based inventory manager.
"""

class SimpleArrayInventory:
    """
    A class representing a simple array-based inventory manager.
    """

    def __init__(self):
        """
        Initialize two simple arrays to store items and prices.
        """
        self.items = []
        self.prices = []

    def insert_item(self, item, price):
        """
        Insert an item and its price, or update the price if the item exists.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.
        """
        if item in self.items:
            index = self.items.index(item)
            self.prices[index] = price
        else:
            self.items.insert(0, item)
            self.prices.insert(0, price)

    def print_items(self):
        """
        Print items and their prices in pairs.
        """
        for item, price in zip(self.items, self.prices):
            print((item, price), end=", \n")

    def find_item(self, item):
        """
        Find the price of a given item.

        Args:
            item (str): The name of the item to look up.

        Returns:
            float: The price of the item if found, None otherwise.
        """
        if item in self.items:
            return self.prices[self.items.index(item)]
        return
