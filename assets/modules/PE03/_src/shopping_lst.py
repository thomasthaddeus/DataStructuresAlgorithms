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


def main(num_iterations=1000):
    """
    Main method of the program
    """
    print("------ Simple array ------")
    sim_arr = SimpleArrayShoppingListManager()

    # insert operation
    simple_array_insert_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        for item in item_list:
            sim_arr.insert_item(item)
        end_time = time.perf_counter()
        simple_array_insert_time += end_time - start_time
    simple_array_insert_avg_time = simple_array_insert_time / num_iterations
    print("Insert operation average time:", simple_array_insert_avg_time)

    # delete operation
    simple_array_delete_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        sim_arr.delete_item("milk")
        end_time = time.perf_counter()
        simple_array_delete_time += end_time - start_time
    simple_array_delete_avg_time = simple_array_delete_time / num_iterations
    print("Delete operation average time:", simple_array_delete_avg_time)

    # look up operation(last element)
    simple_array_lookup_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        sa_last_element = sim_arr.get_last_item()
        end_time = time.perf_counter()
        simple_array_lookup_time += end_time - start_time
    simple_array_lookup_avg_time = simple_array_lookup_time / num_iterations
    print("Lookup operation average time:", simple_array_lookup_avg_time)

    # sort operation
    simple_array_sort_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        sim_arr.selection_sort()
        end_time = time.perf_counter()
        simple_array_sort_time += end_time - start_time
    simple_array_sort_avg_time = simple_array_sort_time / num_iterations
    print("Sort operation average time:", simple_array_sort_avg_time)

    print("------ Linked list ------")
    lnk_lst = LinkedListStackShoppingListManager()

    # insert operation
    linked_list_insert_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        for item in item_list:
            lnk_lst.insert_item(item)
        end_time = time.perf_counter()
        linked_list_insert_time += end_time - start_time
    linked_list_insert_avg_time = linked_list_insert_time / num_iterations
    print("Insert operation average time:", linked_list_insert_avg_time)

    # delete operation
    linked_list_delete_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        lnk_lst.remove_last_item()
        end_time = time.perf_counter()
        linked_list_delete_time += end_time - start_time
    linked_list_delete_avg_time = linked_list_delete_time / num_iterations
    print("Delete operation average time:", linked_list_delete_avg_time)

    # look up operation(last element)
    linked_list_lookup_time = 0
    for i in range(num_iterations):
        start_time = time.perf_counter()
        ll_last_element = lnk_lst.get_last_item()
        end_time = time.perf_counter()
        linked_list_lookup_time += end_time - start_time
    linked_list_lookup_avg_time = linked_list_lookup_time / num_iterations
    print("Lookup operation average time:", linked_list)

if __name__ == "__main__":
    main()
