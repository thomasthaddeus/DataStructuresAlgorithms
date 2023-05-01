"""linked_listshopping_list_manager.py

This module defines a LinkedListShoppingListManager class for managing a shopping list using a
singly linked list. It also includes a Node class for representing a node in the linked list.
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
        current = head

        while current:
            if current.item < pivot.item:
                if pivot_prev:
                    pivot_prev.next, current.next, current = current, pivot_prev.next, current.next
                else:
                    head, current.next, current = current, head, current.next
            else:
                pivot_prev, current = current, current.next

        pivot.next = self.quick_sort_helper(pivot.next)
        head = self.quick_sort_helper(head)
        return head

    def quick_sort(self) -> None:
        """Sorts the items in the shopping list using the quick sort algorithm."""
        tail = self.head
        while tail and tail.next:
            tail = tail.next
        self.head = self.quick_sort_helper(self.head)
