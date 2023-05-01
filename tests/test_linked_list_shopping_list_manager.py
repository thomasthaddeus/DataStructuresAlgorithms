import unittest
from modules.PE04.list_manager.linked_list_shopping_list_manager import LinkedListShoppingListManager

class TestLinkedListShoppingListManager(unittest.TestCase):
    def test_insert_and_print_items(self):
        ll = LinkedListShoppingListManager()
        ll.insert_item("apple")
        ll.insert_item("banana")
        self.assertEqual(ll.print_items, ["banana", "apple"])

    def test_quick_sort(self):
        ll = LinkedListShoppingListManager()
        items = ["apple", "banana", "milk", "bread"]
        for item in items:
            ll.insert_item(item)
        ll.quick_sort()
        self.assertEqual(ll.print_items, sorted(items, reverse=True))

if __name__ == "__main__":
    unittest.main()
