"""linked_list_shopping_list_manager.py

Author:         Thaddeus Thomas
Date:           2023-04-11
Description:    This module contains a class for managing a shopping list
                using a singly linked list data structure.
"""

class Node:
    """
    A class representing a node in a single linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListShoppingListManagerClass:
    """
    A class for managing a shopping list using a single linked list.
    """
    def __init__(self):
        """
        Initialize the head of the linked list.
        """
        self.head = None

    def insert_item(self, item):
        """
        Insert an item at the front of the linked list.

        Args:
            item (str): The name of the item to be inserted.
        """
        new_node = Node(item)  # Create a new node with the given item
        new_node.next = self.head  # Set the new node's next pointer to the current head
        self.head = new_node  # Update the head of the linked list

    def print_items(self):
        """Print all the items in the linked list."""
        temp = self.head
        print("[", end=" ")
        while temp:
            print(temp.data, end=" ")  # Print the item at the current node
            temp = temp.next  # Move to the next node
        print("]")


    def delete_item(self, item):
        """
        Delete an item from the linked list.

        Args:
            item (str): The name of the item to be deleted.
        """
        temp = self.head

        # If the head node holds the item to be deleted
        if temp is not None:
            if temp.data == item:
                self.head = temp.next  # Update the head to the next node
                temp = None  # Delete the old head node
                return

        prev = None
        # Traverse the linked list to find the node with the item to be deleted
        while temp is not None:
            if temp.data == item:
                break
            prev = temp
            temp = temp.next

        # If the item is not found, return
        if temp is None:
            return

        # Update the previous node's next pointer to the node after the one to be deleted
        prev.next = temp.next
        temp = None  # Delete the node with the item


    def get_last_item(self):
        """
        Return the last item in the linked list.
        """
        temp = self.head
        # Traverse the linked list until the last node is found
        while temp.next is not None:
            temp = temp.next
        return temp.data  # Return the item at the last node


    def find_smallest(self):
        """
        Method: find_smallest
        Purpose: Returns the smallest item from the linked list.
        Returns: str - The name of the smallest item in the linked list.
        """
        if not self.head:
            return None

        smallest_item = self.head.data  # Set the smallest item to the head's data
        current_node = self.head.next

        # Traverse the linked list to find the smallest item
        while current_node:
            if current_node.data < smallest_item:
                smallest_item = current_node.data  # Update the smallest item
            current_node = current_node.next

        return smallest_item

    def selection_sort(self):
        """
        Sorts the linked list in ascending order using the selection sort algorithm.
        """
        current = self.head
        # Traverse the linked list with 'current' pointer
        while current:
            min_node = current  # Set the minimum node to the current node
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            if current != min_node:
                current.data, min_node.data = min_node.data, current.data
            current = current.next
