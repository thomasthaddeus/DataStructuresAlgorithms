"""shopping_list.py

This assignment is to gain knowledge on Linked List and Selection Sort. As implementation scenario,
shopping list have been selected. The program stores shopping items in both of simple array or
linked list. Each storing mechanism are separated to different files such as
simple_array_shopping_list_manager.py or linked_list_shopping_list_manager.py each file contains
FileNameClass classes with essential methods for data manipulation. Note that shopping_list.py
with the "main" method have been already implemented, and you are assigned to implement other
classes/methods. As part of assignment, compare actual runtime of insert/delete/lookup operation
between two lists and justify in a short paragraph on how and their performance.
"""

import time
from list_manager.simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass
from list_manager.linked_list_shopping_list_manager import LinkedListShoppingListManagerClass

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
    """Runs the main function of the program."""
    print("------ Simple array ------")
    sa = SimpleArrayShoppingListManagerClass()

    # insert operation
    simple_array_insert_start_time = time.perf_counter()
    for _, item in enumerate(item_list):
        sa.insert_item(item)
    simple_array_insert_end_time = time.perf_counter()
    print("current list:\t", end=" ")
    sa.print_items()

    # delete operation
    simple_array_delete_start_time = time.perf_counter()
    sa.delete_item("milk")
    simple_array_delete_end_time = time.perf_counter()
    print("delete milk:\t", end=" ")
    sa.print_items()

    # look up operation(last element)
    simple_array_lookup_start_time = time.perf_counter()
    sa_last_element = sa.get_last_item()
    simple_array_lookup_end_time = time.perf_counter()
    print(f"last element:\t{sa_last_element}\n")

    # sort operation
    sa.selection_sort()
    print("Sorted(a to z):\t", end=" ")
    sa.print_items()

    # time summary:
    sa_insert_op = simple_array_insert_end_time - simple_array_insert_start_time
    sa_delete_op = simple_array_delete_end_time - simple_array_delete_start_time
    sa_lookup_op = simple_array_lookup_end_time - simple_array_lookup_start_time
    print(
        f"-insert: {sa_insert_op}\n"
        f"-delete: {sa_delete_op}\n"
        f"-lookup: {sa_lookup_op}\n"
    )

    print("------ Linked list ------")
    ll = LinkedListShoppingListManagerClass()
    # insert operation
    linked_list_insert_start_time = time.perf_counter()
    for _, item in enumerate(item_list):
        ll.insert_item(item)
    linked_list_insert_end_time = time.perf_counter()
    print("current list:\t", end=" ")
    ll.print_items()

    # delete operation
    linked_list_delete_start_time = time.perf_counter()
    ll.delete_item("milk")
    linked_list_delete_end_time = time.perf_counter()
    print("delete milk:\t", end=" ")
    ll.print_items()

    # look up operation(last element)
    linked_list_lookup_start_time = time.perf_counter()
    ll_last_element = ll.get_last_item()
    linked_list_lookup_end_time = time.perf_counter()
    print(f"last element:\t{ll_last_element}\n")

    # find smallest
    print(f"smallest element:\t{ll.find_smallest()}\n")

    # sort operation
    ll.selection_sort()
    print("Sorted(a to z):\t", end = " ")
    ll.print_items()

    # find smallest
    print(f"smallest element:\t{ll.find_smallest()}\n")

    # time summary:
    ll_insert_op = linked_list_insert_end_time - linked_list_insert_start_time
    ll_delete_op = linked_list_delete_end_time - linked_list_delete_start_time
    ll_lookup_op = linked_list_lookup_end_time - linked_list_lookup_start_time
    print(
        f"-insert: {ll_insert_op}\n"
        f"-delete: {ll_delete_op}\n"
        f"-lookup: {ll_lookup_op}\n"
    )


if __name__ == "__main__":
    main()
