"""treasure_hunter.py

This module contains a class to represent a treasure hunting scenario.

The TreasureHunterClass can simulate a treasure hunt with a given configuration of hunters and
treasures. It uses a greedy algorithm to find the maximum number of treasures that can be collected
by the hunters given a certain maximum distance a hunter can be from a treasure.

Returns:
    TreasureHunterClass: An object representing a treasure hunt scenario.
"""

from typing import Literal, Any


class TreasureHunterClass:
    """
    This class represents a treasure hunter. It contains methods to find the maximum number of
    treasures that can be collected by hunters given the maximum distance a hunter can be from a
    treasure.
    """

    def __init__(self, arr=None, num=0, k=0) -> None:
        """
        Initializes a TreasureHunterClass object with the list of hunters and treasures, the size
        of the list, and the maximum distance a hunter can be from a treasure.

        Args:
            arr (list, optional): The list containing (H)unters and (T)reasures. Defaults to None.
            num (int, optional): The size of the list. Defaults to 0.
            k (int, optional): The maximum distance a hunter can be from a treasure. Defaults to 0.
        """
        self.arr: Any | list = (
            arr if arr is not None else []
        )  # The list of hunters and treasures
        self.num: int = num  # The size of the list
        self.k: int = k  # The maximum distance a hunter can be from a treasure

    def hunt_treasure(self) -> int:
        """
        Finds the maximum number of treasures that can be collected by the hunters.

        The left pointer will move closer to the treasure
        until it is within the acceptable distance (k)

        Returns:
            int: The maximum number of treasures that can be collected.
        """
        treasures_found = 0
        lft: Literal[0] = 0
        rht: Literal[0] = 0

        while rht < self.num:  # The right pointer will traverse the whole list
            if self.arr[rht] == "T":  # If we find a treasure
                while lft < rht and rht - lft > self.k:
                    lft += 1
                if self.arr[lft] == "H":  # If we find a hunter
                    treasures_found += 1  # Inc T found
                    lft += 1
            rht += 1

        return treasures_found
