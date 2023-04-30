"""simple_array_shopping_list_manager.py

"""

class SimpleArrayShoppingListManager:
    """Manages a shopping list using a simple array."""

    def __init__(self):
        """Initializes an empty array to store shopping list items."""
        self.array = []

    def insert_item(self, item):
        """Inserts an item at the front of the array.

        Args:
            item (str): The item to be added to the shopping list.
        """
        self.array.insert(0, item)

    def print_items(self):
        """Prints the items in the shopping list."""
        for item in self.array:
            print(item, end=" ")
        print()

    def quick_sort_helper(self, array):
        """Recursively sorts the given array using the quick sort algorithm.

        Args:
            array (list): The array to be sorted.

        Returns:
            list: The sorted array.
        """
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.quick_sort_helper(left) + middle + self.quick_sort_helper(right)

    def quick_sort(self):
        """Sorts the items in the shopping list using the quick sort algorithm."""
        self.array = self.quick_sort_helper(self.array)
