# PE08: Programming Exercise

## Instructions

- `treasure_hunter_main.py`
- `treasure_hunter.py`

### Description

This assignment is to learn about the greedy algorithm. Given a hunters and treasures locations from the treasure_hunter_main.py, complete the functions in the separate `TreasureHunterClass` class within `treasure_hunter.py`. The main object of the `TreasureHunterClass` is to find the maximum treasures with given hunters. Note that `treasure_hunter_main.py` with the `main` method and starter file "`treasure_hunter.py`" with class has already been provided (download attachment).

As part of the assignment, describe how the greedy algorithms can be used with an example problem. Keep in mind to always comment and document your class and methods.

### Documentation reference:

[Mertz, J. (n.d.). Documenting Python Code: A Complete Guide.](https://realpython.com/documenting-python-code/)

A `treasure` + `hunter` map `array` of size `n` is constructed with the following specifications:

1. Each element in the array contains either a `hunter(H)` or a `treasure(T)`.
2. Each hunter can find only one treasure.
3. A hunter cannot catch a treasure that is more than `K` units away from the hunter.

Expected result:

treasure_hunter_main.py:
This is the Main python file that is already provided and contains the main and test procedure, which calls methods implemented on "treasure_hunter.py" (this is already provided, but please include this file in your submission).

treasure_hunter.py
This class contains such methods as init, hunt_treasure. Please keep in mind the following notes for each method during implementation:
init(): this method has already been provided.
Hunt_treasure(arr, n, k): the method returns the maximum number of treasures that can be found with given hunters on the map. Parameters: treasure hunt map 'arr', array length 'n', hunter coverage units 'k'
As part of the assignment, describe how the greedy algorithms can be used with an example problem.

Example output:

Note to instructor:

This assignment has multi-parts for students to learn as follows:
Continue practice implementation in python language with the OOP concepts.
Gain knowledge/practice on how greedy algorithm works.
