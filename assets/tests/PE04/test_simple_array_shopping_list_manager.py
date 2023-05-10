"""test array"""

import unittest
from modules.PE04.src.simple_array_shopping_lst_mngr import SimpleArrayShoppingListManager

class TestSimpleArrayShoppingListManager(unittest.TestCase):
    def test_insert_and_print_items(self):
        sa = SimpleArrayShoppingListManager()
        sa.insert_item("apple")
        sa.insert_item("banana")
        self.assertEqual(sa.print_items, ["banana", "apple"])

    def test_quick_sort(self):
        sa = SimpleArrayShoppingListManager()
        items = ["apple", "banana", "milk", "bread"]
        for item in items:
            sa.insert_item(item)
        sa.quick_sort()
        self.assertEqual(sa.print_items, sorted(items, reverse=True))

if __name__ == "__main__":
    unittest.main()
