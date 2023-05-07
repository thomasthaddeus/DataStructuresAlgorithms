"""linked_listshopping_list_manager.py

Author:     Thaddeus Thomas
Date:       2023-04-30
Class:      CS 469: Data Structures & Algorithms
Assignment: PE04

This module provides a LinkedListShoppingListManager class for managing a shopping list using a
singly linked list. The LinkedListShoppingListManager class supports various operations, such as
inserting, removing, searching, updating, and sorting items, as well as merging two sorted shopping
lists, counting occurrences of items, swapping positions of items, and more. The module also
includes a Node class for representing a node in the linked list.

Example:

    from linked_list_shopping_list_manager import LinkedListShoppingListManager

    shopping_list = LinkedListShoppingListManager()
    shopping_list.insert_item("apples")
    shopping_list.insert_item("bananas")
    shopping_list.insert_item("carrots")
    shopping_list.print_items()

    shopping_list.remove_item("bananas")
    shopping_list.update_item("carrots", "cherries")
    shopping_list.insert_item_at_position("bread", 1)

    for item in shopping_list:
        print(item)

    shopping_list.sort()
    shopping_list.print_items()

Classes:

    Node: Represents a node in a singly linked list.
    LinkedListShoppingListManager: Manages a shopping list using a singly linked list.
"""

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, item) -> None:
        """Initializes a new node with the given item.

        Args:
            item (str): The item to be stored in the node.
        """
        self.item = item
        self.next = None


class LinkedListShoppingListManager:
    """Manages a shopping list using a singly linked list."""

    def __init__(self) -> None:
        """Initializes an empty linked list to store shopping list items."""
        self.head = None

    def insert_item(self, item) -> None:
        """Inserts an item at the front of the linked list.

        Args:
            item (str): The item to be added to the shopping list.
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def print_items(self) -> None:
        """Prints the items in the shopping list."""
        current = self.head
        print("[", end=" ")
        while current:
            print(current.item, end=" ")
            current = current.next
        print("]")

    def quick_sort_helper(self, head):
        """Recursively sorts the linked list using the quick sort algorithm.

        Args:
            head (Node): The head of the linked list to be sorted.

        Returns:
            Node: The head of the sorted linked list.
        """
        if not head or not head.next:
            return head

        pivot_prev, pivot = None, head
        current = head.next

        while current:
            if current.item < pivot.item:
                if pivot_prev:
                    pivot_prev.next, current.next, current = current, pivot_prev.next, current.next
                else:
                    head, current.next, current = current, head, current.next
            else:
                pivot_prev, current = current, current.next

        pivot.next = self.quick_sort_helper(pivot.next)
        head = self.quick_sort_helper(head.next)
        return head

    def quick_sort(self):
        """Sorts the items in the shopping list using the quick sort algorithm."""
        self.head = self.quick_sort_helper(self.head)
