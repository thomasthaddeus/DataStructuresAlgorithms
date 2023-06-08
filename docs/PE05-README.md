# PE05: Programming Exercise

[Instructions][1]

## Description

This assignment is to gain knowledge on hash tables using a simple array along with a linked list. A grocery store inventory manager will be implemented for this exercise. The program stores inventory items in hash tables. Each storing mechanism is separated into different files, such as "simple_array_grocery_store_inventory.py" or "hash_grocery_store_inventory.py," where each file contains FileNameClass classes with essential methods for data manipulation. Note that "grocery_store_inventory.py" with the "main" method has already been provided (download attachment). As part of the assignment, compare the actual runtime of hash tables operation between two inventory structures and justify in a short paragraph on how it performs. Keep in mind to always comment and document your class and methods.

Documentation reference:

"Mertz, J. (2018, April). Documenting Python Code: A Complete Guide." [https://realpython.com/documenting-python-code/](https://realpython.com/documenting-python-code/)

## Expected result

### [grocery_store_inventory.py]():

This is the Main python file which is already provided and contains main and test procedure which calls methods implemented on "simple_array_grocery_store_inventory.py" or "hash_grocery_store_inventory.py" file to manage inventory items (this is already provided, but please include this file on your submission).

simple_array_grocery_store_inventory.py

This is a file that includes the class of a simple array-based inventory manager. This class contains such methods as init, insert_item, print_items, find_item. Please keep in mind the following notes for each method during implementation:

Init(): initializes two simple arrays or simple 2D array to be used throughout object life. One array might be used for storing items while another array is used for storing price with synced index.

insert_item(item, price): if the item is already in the list, this method updates the price of it. If the item is not in the list, inserts the item and price at the front of each or 2D array.

Parameters: item name and price.
Note: you are allowed to use the insert() method from Python Array Module.

print_items(): prints item in pair of item name and price.
    Ex. [(item_name, item_price),…]
find_item(item): returns the price of a given item. If the item is not found, simply use "returns" statement.
Parameters: item name to be looked up.

### [hash_grocery_store_inventory.py]()

This is a file that includes the class of hash tables based inventory manager. This class contains such methods as init, insert_item, print_items, find_item. In addition, this class requires the inner class to hold onto hash tables data as a linked list. Please keep in mind the following notes for each method during implementation:

Example illustration: hash tables based inventory structure should look like the diagram below, where each array slot is used to contain a linked list. Each item and price is stored as objects in the linked list. Each node holds onto the item name and price.

Init(tableSize): initializes array 'tableSize' size array with None object to be used to store a linked list.

Parameters: table size
Note: think this as the load factor
hash_func(key): uses item name as a key to compute the hash and returns the result.
For this exercise purpose, we will simply sum up each character's ASCII decimals from the item name to compute the hash value.
Ex. apple: a (97) + p (112) + p (112) + l (108) + e (101) = 530

Parameters: item name.
insert_item(item, price): if the item is already in the list, this method updates the price of it. If the item is not in the list, inserts the item at the end of the linked list on the corresponding array slot.

Parameters: item name and price

#### Pseudocode

Compute hash_key(hash_func_result % table size) to identify slot.
Check if the given slot is None object. If None, start a linked list with given parameters.
Check if the item is at the hash_key slot. If the item is found, update the price.
If the item is not found, create a new node and attach it at the end of the linked list.
print_items(): prints items throughout the hash tables with a linked list. Note: try to print as [ (item1, price1) … ] \n by using some combinations of "print(item, end = " ")" at each hash tables slot as shown below.
find_item(key): returns the price of a given item. If the item is not found, simply use the "returns" statement. Try to reuse the hash_func method. Parameters: item name to be looked up.
As part of the assignment, compare the actual runtime of hash tables operation between two inventory structures and justify in a short paragraph on how it performs.

## Notes

The actual runtime of hash table operations in this exercise will depend on the specific implementation and the input data. However, in general, hash tables offer faster average-case performance for insertions and lookups compared to simple arrays. This is because hash tables have an average-case time complexity of O(1) for both insertions and lookups, while simple arrays have an average-case time complexity of O(n) for lookups and O(1) for insertions at the end. In the provided code, the main function measures the time taken to insert items and find items in both the SimpleArrayGroceryStoreInventoryClass and the HashGroceryStoreInventoryClass.

Upon running the script, it is expected that the hash table implementation will demonstrate a faster performance for lookups when compared to the simple array implementation, while both data structures should have similar insertion times. However, it is important to note that the performance improvement provided by hash tables comes at the cost of increased memory usage due to the use of an array with a specified load factor, as well as the possibility of collisions in the hash table. These collisions can be resolved by using a linked list, as demonstrated in the script.

In conclusion, the script showcases the time difference between the two data structures, which can be used to justify the choice of a particular data structure based on the specific use case and requirements. In general, hash tables are a better choice when faster lookups are a priority, while simple arrays can be more appropriate when memory usage is a concern.

[1]: https://mycourses.cityu.edu/content/enforced/47262-12341133/grocery_store_inventory.py?_&d2lSessionVal=0lajd93gwEyR4UT3QX6Ozqqgj