"""shopping_list.py

This assignment is to gain knowledge on Linked List and Selection Sort. As implementation scenario,
shopping list have been selected. The program stores shopping items in both of simple array or
linked list. Each storing mechanism are separated to different files such as
'simple_array_shopping_list_manager.py' or linked_list_shopping_list_manager.py each file contains
FileNameClass classes with essential methods for data manipulation. Note that 'shopping_list.py'
with the 'main' method have been already implemented implement other classes/methods. As part of
assignment, compare actual runtime of insert/delete/lookup operation between two lists and justify
in a short paragraph on how and their performance.
"""

import time
from Stack.simple_array_shopping_list_manager import SimpleArrayShoppingListManager
from Stack.linked_list_stack_shopping_list_manager import LinkedListStackShoppingListManager


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
    Main method of the program
    """
    print("------ Simple array ------")
    sim_arr = SimpleArrayShoppingListManager()

    # insert operation
    simple_array_insert_start_time = time.perf_counter()
    for item in item_list:
        sim_arr.insert_item(item)
    simple_array_insert_end_time = time.perf_counter()
    print("current list:\t", end=" ")
    sim_arr.print_items()

    # delete operation
    simple_array_delete_start_time = time.perf_counter()
    sim_arr.delete_item("milk")
    simple_array_delete_end_time = time.perf_counter()
    print("delete milk:\t", end=" ")
    sim_arr.print_items()

    # look up operation(last element)
    simple_array_lookup_start_time = time.perf_counter()
    sa_last_element = sim_arr.get_last_item()
    simple_array_lookup_end_time = time.perf_counter()
    print(f"last element:\t{sa_last_element}")

    # sort operation
    simple_array_sort_start_time = time.perf_counter()
    sim_arr.selection_sort()
    simple_array_sort_end_time = time.perf_counter()
    print("Sorted(a to z):\t", end=" ")
    sim_arr.print_items()

    # time summary:
    sa_insert_op = simple_array_insert_end_time - simple_array_insert_start_time
    sa_delete_op = simple_array_delete_end_time - simple_array_delete_start_time
    sa_lookup_op = simple_array_lookup_end_time - simple_array_lookup_start_time
    sa_sort_op = simple_array_sort_end_time - simple_array_sort_start_time
    print(
        f"-insert: {sa_insert_op}\n \
          -delete: {sa_delete_op}\n \
          -lookup: {sa_lookup_op}\n \
            -sort: {sa_sort_op}\n"
    )

    print("------ Linked list ------")
    lnk_lst = LinkedListStackShoppingListManager()

    # insert operation
    linked_list_insert_start_time = time.perf_counter()
    for item in item_list:
        lnk_lst.insert_item(item)
    linked_list_insert_end_time = time.perf_counter()
    print("current list:\t", end=" ")
    lnk_lst.print_items_from_top()

    # delete operation
    linked_list_delete_start_time = time.perf_counter()
    lnk_lst.remove_last_item("milk")
    linked_list_delete_end_time = time.perf_counter()
    print("delete milk:\t", end=" ")
    lnk_lst.print_items_from_top()

    # look up operation(last element)
    linked_list_lookup_start_time = time.perf_counter()
    ll_last_element = lnk_lst.get_last_item()
    linked_list_lookup_end_time = time.perf_counter()
    print(f"last element:\t{ll_last_element}")

    # find smallest
    linked_list_smallest_start_time = time.perf_counter()
    ll_smallest = lnk_lst.find_smallest()
    linked_list_smallest_end_time = time.perf_counter()
    print(f"smallest element:\t{ll_smallest}")

    # time summary:
    ll_insert_op = linked_list_insert_end_time - linked_list_insert_start_time
    ll_delete_op = linked_list_delete_end_time - linked_list_delete_start_time
    ll_lookup_op = linked_list_lookup_end_time - linked_list_lookup_start_time
    ll_smallest_op = linked_list_smallest_end_time - linked_list_smallest_start_time
    print(
        f"-insert: {ll_insert_op}\n \
          -delete: {ll_delete_op}\n \
          -lookup: {ll_lookup_op}\n \
        -smallest: {ll_smallest_op}\n"
    )



if __name__=='main':
    main()
