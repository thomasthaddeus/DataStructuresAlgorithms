import pytest

def test_insert_item():
    ll = LinkedListShoppingListManagerClass()
    ll.insert_item("apple")
    ll.insert_item("banana")
    assert ll.head.data == "banana"
    assert ll.head.next.data == "apple"

def test_delete_item():
    ll = LinkedListShoppingListManagerClass()
    ll.insert_item("apple")
    ll.insert_item("banana")
    ll.delete_item("apple")
    assert ll.head.data == "banana"
    assert ll.head.next is None

def test_get_last_item():
    ll = LinkedListShoppingListManagerClass()
    ll.insert_item("apple")
    ll.insert_item("banana")
    last_item = ll.get_last_item()
    assert last_item == "apple"

def test_find_smallest():
    ll = LinkedListShoppingListManagerClass()
    ll.insert_item("apple")
    ll.insert_item("banana")
    ll.insert_item("carrot")
    smallest = ll.find_smallest()
    assert smallest == "apple"
