"""gsi.py

This script implements a grocery store inventory manager using two different data structures:
Simple Array and Hash Table. The inventory manager stores items and their prices, and is capable of
inserting new items and looking up item prices.

Classes:
    SimpleArrayInventory: Inventory implementation using a simple array.
    HashTableInventory: Inventory implementation using a hash table.

Functions:
    main() -> Tuple[float, float, float, float]: Runs the main function of the application and
        returns the operation times for the simple array and hash table.
    calc_avg(num_iter: int) -> Tuple[float, float, float, float]: Calculates average operation
        times for both data structures over a specified number of iterations.

"""

import sys
import time
from items.hash_gsi import HashTableInventory
from items.simp_arr_gsi import SimpleArrayInventory

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
    "apple",
    "salt",
    "pepper",
    "olive oil",
    "eggs",
    "flour",
]
item_price = [
    "$1.10",
    "$2.20",
    "$3.30",
    "$4.40",
    "$5.50",
    "$6.60",
    "$7.70",
    "$8.80",
    "$9.90",
    "$10.10",
    "$11.11",
    "$2.20",
    "$12.12",
    "$13.13",
    "$14.14",
    "$15.15",
    "$16.16",
]

ITEM1 = "apple"
ITEM2 = "test"


def main():
    """
    Runs the main function of the application
    """
    print("------ Simple array ------")
    sagsi = SimpleArrayInventory()

    simp_arr_insert_start_time = time.perf_counter()
    for i, j in zip(item_list, item_price):
        sagsi.insert_item(i, j)
    simp_arr_insert_end_time = time.perf_counter()

    sagsi.print_items()

    simp_arr_find_start_time = time.perf_counter()
    print(f"price for {ITEM1} : {sagsi.find_item(ITEM1)}")
    print(f"price for {ITEM2} : {sagsi.find_item(ITEM2)}")
    simp_arr_find_end_time = time.perf_counter()

    # time summary:
    sa_insert_op = simp_arr_insert_end_time - simp_arr_insert_start_time
    sa_lookup_op = simp_arr_find_end_time - simp_arr_find_start_time
    print(f"-insert: {sa_insert_op}\n-lookup: {sa_lookup_op}\n")

    print("\n\n------ Hash table ------")
    htgsi = HashTableInventory(20)
    hash_table_insert_start_time = time.perf_counter()
    for itema, itemb in zip(item_list, item_price):
        htgsi.insert_item(itema, itemb)
    hash_table_insert_end_time = time.perf_counter()

    htgsi.print_items()

    hash_table_find_start_time = time.perf_counter()
    print(f"price for {ITEM1} : {htgsi.find_item(ITEM1)}")
    print(f"price for {ITEM2} : {htgsi.find_item(ITEM2)}")
    hash_table_find_end_time = time.perf_counter()

    # time summary:
    ht_insert_op = hash_table_insert_end_time - hash_table_insert_start_time
    ht_lookup_op = hash_table_find_end_time - hash_table_find_start_time
    print(f"-insert: {ht_insert_op}\n-lookup: {ht_lookup_op}\n")

    return sa_insert_op, sa_lookup_op, ht_insert_op, ht_lookup_op

def calc_avg(num_iter: int) -> tuple[float, float, float, float]:
    """
    Calculates average operation times for both SimpleArrayInventory and HashTableInventory
    data structures over a specified number of iterations.

    Args:
        num_iter (int): The number of iterations to perform the calculations.

    Returns:
        Tuple[float, float, float, float]: Average operation times for simple array insert,
            simple array lookup, hash table insert, and hash table lookup.
    """
    iter_x = 0
    sa_insert_sum, sa_lookup_sum, ht_insert_sum, ht_lookup_sum = 0, 0, 0, 0

    while iter_x < num_iter:
        with open(file="output.txt", mode="a", encoding='utf-8') as fil:
            original_stdout = sys.stdout
            sys.stdout = fil
            sa_insert_op, sa_lookup_op, ht_insert_op, ht_lookup_op = main()
            sys.stdout = original_stdout

            sa_insert_sum += sa_insert_op
            sa_lookup_sum += sa_lookup_op
            ht_insert_sum += ht_insert_op
            ht_lookup_sum += ht_lookup_op

            iter_x += 1

    sa_insert_avg = sa_insert_sum / num_iter
    sa_lookup_avg = sa_lookup_sum / num_iter
    ht_insert_avg = ht_insert_sum / num_iter
    ht_lookup_avg = ht_lookup_sum / num_iter

    return sa_insert_avg, sa_lookup_avg, ht_insert_avg, ht_lookup_avg

if __name__ == "__main__":
    sa_in_avg, sa_out_avg, ht_in_avg, ht_out_avg = calc_avg(100)

    print(f"Simple array average timings:\n- insert: {sa_in_avg}\n- lookup: {sa_out_avg}\n")
    print(f"Hash table average timings:\n- insert: {ht_in_avg}\n- lookup: {ht_out_avg}\n")
