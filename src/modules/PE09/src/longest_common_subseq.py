"""longest_common_subseq.py

The main object of the LCSClass is to find the length of the longest common
subsequence.
"""

class LCSClass:
    """
    A class used to find the length of the longest common subsequence between two string sequences.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the LCSClass object.
        Memoization for dynamic programming
        """
        self.memo = {}

    def find(self, str_x, str_y):
        """
        Finds the length of the longest common subsequence between two string sequences.

        Parameters:
        x (str): The first string sequence.
        y (str): The second string sequence.

        Returns:
        int: The length of the longest common subsequence.
        """
        if not str_x or not str_y:
            return 0
        elif (str_x, str_y) in self.memo:
            return self.memo[(str_x, str_y)]
        elif str_x[-1] == str_y[-1]:
            result = 1 + self.find(str_x[:-1], str_y[:-1])
        else:
            result = max(self.find(str_x, str_y[:-1]), self.find(str_x[:-1], str_y))
        self.memo[(str_x, str_y)] = result
        return result
