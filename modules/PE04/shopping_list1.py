"""shopping_list.py

Author:     Thaddeus Thomas
Date:       2023-04-30
Class:      CS 469: Data Structures & Algorithms
Assignment: PE04

This assignment is to gain knowledge on Quick sort using Linked list. A shopping list will be
reimplemented for this exercise. The program stores shopping items in both simple array or
linked list. Each storing mechanism is separated into different files, such as
"simple_array_shopping_lst_mngr.py" or "linked_list_shopping_lst_mngr.py", where each file
contains FileNameClass classes with essential methods for data manipulation.
Note that "shopping_list.py" with the "main" method has already been provided (download attachment).

As part of the assignment, compare the actual runtime of Quick sort operation between two lists
and justify in a short paragraph on how the algorithms perform.
"""

import time
from lst_mngr.simple_array_shopping_lst_mngr import SimpleArrayShoppingListManager
from lst_mngr.linked_list_shopping_lst_mngr import LinkedListShoppingListManager

item_list = [
    "apple",
    "banana",
    "milk",
    "bread",
    "butter",
    "cheese",
    "carrot",
    "pork",
    "beef",
    "mushroom",
    "fish",
]


def main():
    """
    The program stores shopping items in both simple array or linked list.
    """
    print("------ Simple array ------")
    sa = SimpleArrayShoppingListManager()

    # insert operation
    for _, i in enumerate(item_list):
        sa.insert_item(i)
    print("Current list:\t", end=" ")
    sa.print_items()

    # sort operation
    simple_array_sort_start_time = time.perf_counter()
    sa.quick_sort()
    simple_array_sort_end_time = time.perf_counter()
    print("Sorted(a to z):\t", end=" ")
    sa.print_items()

    # time summary:
    sa_sort_op = simple_array_sort_end_time - simple_array_sort_start_time
    print(f"-sort: {sa_sort_op}")

    print("------ Linked list ------")
    ll = LinkedListShoppingListManager()

    # insert operation
    for _, i in enumerate(item_list):
        ll.insert_item(i)
    print("Current list:\t", end=" ")
    ll.print_items()

    # sort operation
    linked_list_sort_start_time = time.perf_counter()
    ll.quick_sort()
    linked_list_sort_end_time = time.perf_counter()
    print("Sorted(a to z):\t", end=" ")
    ll.print_items()

    # time summary:
    ll_sort_op = linked_list_sort_end_time - linked_list_sort_start_time
    print(f"-sort: {ll_sort_op}")


if __name__ == "__main__":
    main()
