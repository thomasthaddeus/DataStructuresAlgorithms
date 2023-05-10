"""binary_search.py

Version:      1.0,
Author:       Thaddeus Thomas,
Date:         2023-04-09
Repository:   github.com/thomasthaddeus
Project:      Binary Search vs Simple Search,
Description:  This module contains a class that implements the binary search
              algorithm. Runs in O(log n) time where
"""

class BinarySearchClass:
    """
    The BinarySearchClass provides an implementation of the binary search algorithm.
    """

    def __init__(self, name_list):
        """
        Initializes the BinarySearchClass with a list of names to search.

        Args:
            name_list (list): A list of names, assumed to be sorted alphabetically.
        """
        self.name_list = name_list


    def binary_search(self, tgt_name):
        """
        Searches for the given target name using binary search.

        Args:
            tgt_name (str): The name to search for in the name_list.

        Returns:
            int: The index of the target name if found, None otherwise.
        """
        left, right = 0, len(self.name_list) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_name = self.name_list[mid]

            if mid_name == tgt_name:
                return mid
            elif mid_name < tgt_name:
                left = mid + 1
            else:
                right = mid - 1

        return None

if __name__ =='__main__':
    main()
