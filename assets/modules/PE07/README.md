# PE07: Programming Exercise

## Instructions

- `dijkstra_main.py`
- `dijkstra.py`

### Description

This assignment is to learn about the Dijkstra algorithm. Given a hash graph map from the dijkstra_main.py, complete the functions in the separate "DijkstraClass" class within dijkstra.py. The main object of the "DijkstraClass" is to find the lowest-cost path from the start (s) to finish (f). Note that "dijkstra_main.py" with the "main" method and starter file "dijkstra.py" with class has already been provided (download attachment).

As part of the assignment, describe how the Dijkstra algorithm works in your own words. Keep in mind to always comment and document your class and methods.

### Documentation reference

[Mertz, J. (n.d.). Documenting Python Code: A Complete Guide.](https://realpython.com/documenting-python-code/)

### Expected result

1. `dijkstra_main.py`
   - This is the Main python file that is already provided and contains the main and test procedure, which calls methods implemented on "dijkstra.py" (this is already provided, but please include this file in your submission).
2. `dijkstra.py`
   - This class contains such methods as init, initial_costs_parents, find_shorted_path, find_lowest_cost_node, and print_path. Please keep in mind the following notes for each method during implementation:
   - `init()`: this method has already been provided.
   - `initial_costs_parents()`: this method initializes costs and parents global variables as to how the Dijkstra algorithm works.
   - `find_shorted_path()`: this method updates costs and parents global variables by following the Dijkstra algorithm.
   - `find_lowest_cost_node (costs)`: this method finds and returns the lowest cost node that hasn't been processed yet.
3. **Parameters**: *costs*
   - `print_path()`: if there is path, prints path from `s` to `f`

### Summary

As part of the assignment, describe how the Dijkstra algorithm works in your own words.
