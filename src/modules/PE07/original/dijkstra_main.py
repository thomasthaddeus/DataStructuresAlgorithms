"""dijkstra_main.py

This assignment is to learn about the Dijkstra algorithm.
Given a hash graph map from the dijkstra_main.py, complete the functions
in the separate "DijkstraClass" class within dijkstra.py. 
The main object of the "DijkstraClass" is to find the lowest-cost path
from the start (s) to finish (f).

"""

from dijkstra import DijkstraClass


graph_one = {
    's': {'a': 6, 'b': 2},
    'a': {'c': 1},
    'b': {'a': 3, 'c': 5},
    'c': {'f': 2},
    'f': {},
}

graph_two = {
    's': {},
    'a': {'c': 1},
    'b': {'a': 3, 'c': 5},
    'c': {'f': 2},
    'f': {},
}

def main():
    print("path for graph_one:")
    dij_one = DijkstraClass(graph_one)
    dij_one.initial_costs_parents()
    dij_one.find_shorted_path()
    dij_one.print_path()

    print("path for graph_two:")
    dij_two = DijkstraClass(graph_two)
    dij_two.initial_costs_parents()
    dij_two.find_shorted_path()
    dij_two.print_path()

if __name__ == "__main__":
        main()
