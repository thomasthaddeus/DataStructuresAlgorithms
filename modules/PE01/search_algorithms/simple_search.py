'''simple_search.py

Version:     1.0,
Author:      Thaddeus Thomas,
Date:        2023-04-09
Repository:  github.com/thadsalgorithmslibrary
Project:     Binary Search vs Simple Search,
Description: Simple search algorithm checks each element of the list one by one
               runs the algorithm in O(n) time.
'''


class SimpleSearchClass:
    """
    The SimpleSearchClass provides an implementation of the simple search algorithm.
    """

    def __init__(self, name_list):
        self.name_list = name_list  # Initialize the list of names to be searched


    def simple_search(self, target_name):
        """
        The simple_search method takes a target name and returns the index of the name in the list.
        If the name is not found, it returns None.

        Args:
            target_name (str): The name to search for in the list.

        Returns:
            int or None: The index of the target_name in the list, or None if the name is not found.
        """
        for index, name in enumerate(self.name_list):
            if name == target_name:
                return index  # Return the index of the target_name in the list

        return None  # Return None if the target_name is not found in the list

if __name__ =='__main__':
    main()
