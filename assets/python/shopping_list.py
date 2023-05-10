"""shopping_list.py

INSTRUCTIONS:
This assignment aims to help you learn about Linked Lists and Selection Sort through a practical
example involving a shopping list. In the program, you'll store shopping items using two different
data structures: a simple array and a linked list. These structures will be managed in separate
files, named "simple_array_shopping_list_manager.py" and "linked_list_shopping_list_manager.py",
respectively.

Each file will contain a class (FileNameClass) with essential methods for manipulating the data.
It's important to note that the "shopping_list.py" file with the "main" method has already been
implemented, so your task is to complete the other classes and methods.

As part of this assignment, you should also compare the actual runtime of insert/delete/lookup
operations between the two data structures. Once you've made these comparisons, write a brief
paragraph explaining the differences in performance and the reasons behind them.
"""

import time
from simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass
from linked_list_shopping_list_manager import LinkedListShoppingListManagerClass

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
    "fish"
]

def main():
    """
    Runs the main function of shopping_list.py

    """
    print("------ Simple array ------")
    sa = SimpleArrayShoppingListManagerClass()

    #insert operation
    simple_array_insert_start_time = time.perf_counter()
    for i in range(len(item_list)):
        sa.insert_item(item_list[i])
    simple_array_insert_end_time = time.perf_counter()
    print("current list:\t", end = " ")
    sa.print_items()

    #delete operation
    simple_array_delete_start_time = time.perf_counter()
    sa.delete_item("milk")
    simple_array_delete_end_time = time.perf_counter()
    print("delete milk:\t", end = " ")
    sa.print_items()

    #look up operation(last element)
    simple_array_lookup_start_time = time.perf_counter()
    sa_last_element = sa.get_last_item()
    simple_array_lookup_end_time = time.perf_counter()
    print(f"last element:\t{sa_last_element}")
    #sort operation
    sa.selection_sort()
    print("Sorted(a to z):\t", end = " ")
    sa.print_items()

    #time summary:
    saInsertOp = simple_array_insert_end_time - simple_array_insert_start_time
    saDeleteOp = simple_array_delete_end_time - simple_array_delete_start_time
    saLookupOp = simple_array_lookup_end_time - simple_array_lookup_start_time
    print(f"-insert: {saInsertOp} \
            -delete: {saDeleteOp} \
            -lookup: {saLookupOp}\n")

    print("------ Linked list ------")
    ll = LinkedListShoppingListManagerClass()
    #insert operation
    linked_list_insert_start_time = time.perf_counter()
    for i in range(len(item_list)):
        ll.insert_item(item_list[i])
    linked_list_insert_end_time = time.perf_counter()
    print("current list:\t", end = " ")
    ll.print_items()

    #delete operation
    linked_list_delete_start_time = time.perf_counter()
    ll.delete_item("milk")
    linked_list_delete_end_time = time.perf_counter()
    print("delete milk:\t", end = " ")
    ll.print_items()

    #look up operation(last element)
    linked_list_lookup_start_time = time.perf_counter()
    ll_last_element = ll.get_last_item()
    linked_list_lookup_end_time = time.perf_counter()
    print(f"last element:\t{ll_last_element}")

    #find smallest
    print(f"smallest element:\t{ll.find_smallest()}")

    #sort operation
    #ll.selection_sort()
    #print("Sorted(a to z):\t", end = " ")
    #ll.print_items()

    #time summary:
    llInsertOp= linked_list_insert_end_time - linked_list_insert_start_time
    llDeleteOp= linked_list_delete_end_time - linked_list_delete_start_time
    llLookupOp= linked_list_lookup_end_time - linked_list_lookup_start_time
    print(f"-insert: {llInsertOp} \
            -delete: {llDeleteOp} \
            -lookup: {llLookupOp}\n")

if __name__ == "__main__":
    main()
