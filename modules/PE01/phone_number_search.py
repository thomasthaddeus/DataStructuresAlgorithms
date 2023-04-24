"""phone_number_search.py

This assignment is to practice python language (ex. class, method, Object-Oriented Programming
concept, and syntaxes) and implement simple and binary search for looking up the phone number
of a given name.
"""

import time

from search_algorithms.binary_search import BinarySearchClass
from search_algorithms.simple_search import SimpleSearchClass


name_list = [
    "Alice",
    "Bob",
    "Charlie",
    "Daisy",
    "Emily",
    "Fred",
    "George",
    "Harry",
    "Iris",
    "Jenny",
    "Kenny",
    "Lucas",
    "Mary",
    "Nancy",
    "Oliver",
    "Phillip",
    "Quinn",
    "Rose",
    "Sophia",
    "Thomas",
]

phn_num = [
    "000-230-2491",
    "000-203-1274",
    "000-211-2394",
    "000-212-1183",
    "000-204-1237",
    "000-271-2394",
    "000-231-0183",
    "000-213-3233",
    "000-251-2395",
    "000-211-0183",
    "000-283-1214",
    "000-221-2314",
    "000-261-0243",
    "000-253-1334",
    "000-229-2183",
    "000-238-2283",
    "000-255-2133",
    "000-243-2243",
    "000-282-2386",
    "000-231-2143",
]

def main():
    """
    Runs the main function of the module
    """
    person_name = "Thomas"
    print(f"look up {person_name}'s phone number...")

    # Note that name_list and phone_number array indexes are synced
    ssc = SimpleSearchClass(name_list)
    sim_srch_st_time = time.perf_counter()
    sim_res = ssc.simple_search(person_name)
    simple_search_end_time = time.perf_counter()
    print(f"phone number(simple search): {phn_num[sim_res]}")
    print(f"--- simple search: {simple_search_end_time - sim_srch_st_time} seconds ---")

    # Note that name_list and phn_num array indexes are synced
    bsc = BinarySearchClass(name_list)
    bin_srch_st_time = time.perf_counter()
    bin_result = bsc.binary_search(person_name)
    bin_srch_end_time = time.perf_counter()
    print(f"phone number(binary search): {phn_num[bin_result]}")
    print(f"--- binary search: {bin_srch_end_time - bin_srch_st_time} seconds ---")

if __name__ == "__main__":
    main()
