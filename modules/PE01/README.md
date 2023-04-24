# PE01: Programming Exercise

`phone_number_search.py`

This assignment is to practice python language (ex. class, method, Object-Oriented Programming concept, and syntaxes)
and implement simple and binary search for looking up the phone number of a given name.

## Description

The `simple_search` and `binary_search` method should be part of a class named `SimpleSearchClass` class within `simple_search.py` file and `BinarySearchClass` class within `binary_search.py` file along with the class initialization method which takes in the alphabetically named array `name_list`.

The simple and binary search function itself will be called from another python file named `phone_number_search.py` with an input parameter that holds the person's name. From each search function, the result will be an index of where the person's name was located from the `name_list` array and should be used to lookup/print the person's phone number from `phone_number` array. To learn how the search algorithm works in simple search, DO NOT use `index()` method from the python standard library. **Note** that `name_list` and `phone_number` array indexes are synced. Lastly, `phone_number_search.py` file has already been provided, which also uses a `time` module to compare the simple and binary search runtime.

As part of the assignment, compare each search algorithm's actual runtime and justify in a short paragraph on how and which search algorithm runs faster. Keep in mind to always comment and document your class and methods.

## Documentation reference

- Mertz, J. (n.d.). [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/).

## Expected result

1. `phone_number_search.py` file (This is already provided, but please include this file on your submission)
2. `simple_search.py` file (contains `SimpleSearchClass` and `simple_search` function)
   - `init(array)` function should act as a constructor and initializes an array of the object with `name_list` array.
   - `simple_search(searching_item)` function within the class should take in the value of the searching item.
3. `binary_search.py` file (contains `BinarySearchClass` and `binary_search` function)
   - `init(array)` function should act as a constructor and initializes an array of the object with `name_list` array.
   - `binary_search(searching_item)` function within the class should take in the value of the searching item.
4. Short paragraph on how and which search function runs faster.

## Results

The binary search algorithm performed much faster than the simple search algorithm.

**Prediction**: Its obvious too why the binary search performed so much faster than the simple search, it doesn't look at every item in the array.

**Binary_search** time: varied

**Simple_search** time: varied

I ran out of time to properly implement my test suite and won't know for sure whether the binary search is truly faster than the simple search but after 10 tests I found that they were about even. If i had to guess its because the simple search found the ones closer to zero faster than the binary search.

![Tests](../../img/1-phone_number_search.png)
