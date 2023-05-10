"""hash_gsi.py

This module implements a hash table-based inventory manager.

Classes:
    Node: Represents a node in a linked list.
    HashTableInventory: Represents a hash table-based inventory manager.

"""
# Author:       Thaddeus Thomas
# Date:         2023-05-07
# Assignment:   PE05 Hash Tables
# Project:      Data Structures & Algorithms
# Repository:   https://github.com/thomasthaddeus/

class Node:
    """A class representing a node in a linked list."""

    def __init__(self, item, price):
        """
        Initialize the node with the given item and price.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.
        """
        self.item = item
        self.price = price
        self.next = None

class HashTableInventory:
    """A class representing a hash table-based inventory manager."""

    def __init__(self, table_size):
        """
        Initialize the hash table with a given table size.

        Args:
            table_size (int): The size of the hash table.
        """
        self.table_size = table_size
        self.table = [None] * table_size

    def hash_func(self, key):
        """
        Compute the hash value for a given key.

        Args:
            key (str): The item name to be hashed.

        Returns:
            int: The hash value.
        """
        return sum(ord(char) for char in key)

    def insert_item(self, item, price):
        """
        Insert an item and its price, or update the price if the item exists.

        Args:
            item (str): The name of the item.
            price (float): The price of the item.
        """
        hash_key = self.hash_func(item) % self.table_size
        if self.table[hash_key] is None:
            self.table[hash_key] = Node(item, price)
        else:
            curr = self.table[hash_key]
            while curr:
                if curr.item == item:
                    curr.price = price
                    return
                if curr.next is None:
                    curr.next = Node(item, price)
                    return
                curr = curr.next

    def print_items(self):
        """Print items and their prices in pairs."""
        for index in range(self.table_size):
            curr = self.table[index]
            while curr:
                print((curr.item, curr.price), end=", \n")
                curr = curr.next

    def find_item(self, item):
        """
        Find the price of a given item.

        Args:
            item (str): The name of the item to look up

        Returns:
            float: The price of the item if found, None otherwise.
        """
        hash_key = self.hash_func(item) % self.table_size
        curr = self.table[hash_key]
        while curr:
            if curr.item == item:
                return curr.price
            curr = curr.next
        return
