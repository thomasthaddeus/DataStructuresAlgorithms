import pytest


def test_insert_item():
    sa = SimpleArrayShoppingListManagerClass()
    sa.insert_item("apple")
    sa.insert_item("banana")
    assert sa.items == ["banana", "apple"]

def test_delete_item():
    sa = SimpleArrayShoppingListManagerClass()
    sa.insert_item("apple")
    sa.insert_item("banana")
    sa.delete_item("apple")
    assert sa.items == ["banana"]

def test_get_last_item():
    sa = SimpleArrayShoppingListManagerClass()
    sa.insert_item("apple")
    sa.insert_item("banana")
    last_item = sa.get_last_item()
    assert last_item == "apple"

def test_selection_sort():
    sa = SimpleArrayShoppingListManagerClass()
    sa.insert_item("apple")
    sa.insert_item("banana")
    sa.insert_item("carrot")
    sa.selection_sort()
    assert sa.items == ["apple", "banana", "carrot"]
