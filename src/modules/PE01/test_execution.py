"""test_execution.py

Version:      1.0,
Author:       Thaddeus Thomas,
Date:         2023-04-09
Repository:   github.com/thomasthaddeus
Project:      Binary Search vs Simple Search,
Description:  This is a test implementation of the binary search algorithm &
              the simple search algorithm. This implementation tests for which
              is the most efficient.
"""

import time
import random
import string
from src.binary_search import BinarySearchClass
from src.simple_search import SimpleSearchClass


def rndm_name(length) -> str:
    """
    Generates a random string of a given length.

    Args:
        length (int): The length of the random string.

    Returns:
        str: A randomly generated string of the specified length.
    """
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

def test_execution() -> None:
    """
    Tests the execution time of the SimpleSearchClass and BinarySearchClass algorithms for
    searching a phone number in a list of names.
    """
    # Generate sorted list of random names
    nlst: list[str] = sorted([rndm_name(5) for _ in range(1000)])

    # Generate list of random phone numbers
    phn_nums: list[str] = [
        f"{random.randint(0,999)}-{random.randint(0,999)}-{random.randint(1000, 9999)}"
        for _ in range(1000)
    ]
    print(phn_nums)

    # Select a random name from the list
    tst_name: str = nlst[random.randint(0, 999)]

    print(f"Looking up {tst_name}'s phone number...")

    # Perform simple search
    ssc = SimpleSearchClass(nlst)
    ssc_st_time: float = time.perf_counter()
    sim_res: int | None = ssc.simple_search(tst_name)
    ssc_end_time: float = time.perf_counter()

    # Display simple search results
    if sim_res is not None:
        print(f"Phone number (simple search): {phn_nums[sim_res]}")
    else:
        print("Name not found (simple search)")
    print(f"--- Simple search: {ssc_end_time - ssc_st_time} seconds ---")

    # Perform binary search
    bsc = BinarySearchClass(nlst)
    bin_srch_st_time: float = time.perf_counter()
    bin_res: int | None = bsc.binary_search(tst_name)
    bin_srch_etime: float = time.perf_counter()

    # Display binary search results
    if bin_res is not None:
        print(f"Phone number (binary search): {phn_nums[bin_res]}")
    else:
        print("Name not found (binary search)")
    print(f"--- Binary search: {bin_srch_etime - bin_srch_st_time} seconds ---")
