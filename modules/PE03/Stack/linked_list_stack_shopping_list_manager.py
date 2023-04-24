"""linked_list_stack_shopping_list_manager.py

Author: Thaddeus Thomas
Date:   2023-04-23
Description:
    This module contains a Node class and a LinkedListStackShoppingListManager class.
    The LinkedListStackShoppingListManager class manages a shopping list using a linked
    list-based stack. It includes methods to insert items, print items from top to bottom
    and vice versa, check if the list is empty, get and remove the last item. The Node
    class is a helper class to create nodes for the linked list-based stack.
"""

class Node:
    """
    A class to store data and reference to the next node in the linked list.
    """

    def __init__(self, data):
        """
        Initializes the data and the next reference in the Node.

        Args:
            data: The data to be stored in the Node.
        """
        self.data = data
        self.next = None


class LinkedListStackShoppingListManager:
    """
    A class to manage a shopping list using a linked list-based stack.
    """

    def __init__(self):
        """
        Initializes the head of the linked list-based stack.
        """
        self.head = None


    def insert_item(self, item):
        """
        Inserts a new item into the linked list-based stack.

        Args:
            item: The item to be inserted.
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node


    @property
    def is_list_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not bool(self.head)


    def print_item_recursive_from_top(self, current_node):
        """
        Recursively prints the items from the top of the linked list-based stack.

        Args:
            current_node: The current node being visited in the recursive call.
        """
        if current_node is not None:
            print(current_node.data, end=" ")
            self.print_item_recursive_from_top(current_node.next)


    def print_items_from_top(self):
        """
        Prints the items from the top of the stack.
        """
        self.print_item_recursive_from_top(self.head)
        print()


    def print_item_recursive_from_bottom(self, current_node):
        """
        Recursively prints the items from the bottom of the linked list-based stack.

        Args:
            current_node: The current node being visited in the recursive call.
        """
        if current_node is not None:
            self.print_item_recursive_from_bottom(current_node.next)
            print(current_node.data, end=" ")


    def print_items_from_bottom(self):
        """
        Prints the items from the bottom of the stack.
        """
        self.print_item_recursive_from_bottom(self.head)
        print()


    def get_last_item(self):
        """
        Returns the last item from the list (top of the stack).

        Returns:
            The last item or None if the stack is empty.
        """
        if self.is_list_empty:
            return None
        return self.head.data


    def remove_last_item(self):
        """
        Removes the last item from the list (top of the stack) and returns it.

        Returns:
            The last item or None if the stack is empty.
        """
        if self.is_list_empty:
            return None
        item = self.head.data
        self.head = self.head.next
        return item
