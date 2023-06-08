"""main.py

This assignment is to learn about the Dijkstra algorithm.
Given a hash graph map from the dijkstra_main.py, complete the functions
in the separate "DijkstraClass" class within dijkstra.py.
The main object of the "DijkstraClass" is to find the lowest-cost path
from the start (s) to finish (f).
"""
from typing import Dict
from src.dijkstra import DijkstraClass


graph_one: Dict[str, Dict[str, int]] = {
    "s": {"a": 6, "b": 2},
    "a": {"c": 1},
    "b": {"a": 3, "c": 5},
    "c": {"f": 2},
    "f": {},
}

graph_two: Dict[str, Dict[str, int]] = {
    "s": {},
    "a": {"c": 1},
    "b": {"a": 3, "c": 5},
    "c": {"f": 2},
    "f": {},
}


def main():
    """Runs the main program"""
    start_node = "s"
    end_node = "f"

    print("\n\nPath for graph_one:")
    dij_one = DijkstraClass(graph_one)
    dij_one.print_path(start_node, end_node)

    print("\n\nPath for graph_two:")
    dij_two = DijkstraClass(graph_two)
    dij_two.print_path(start_node, end_node)


if __name__ == "__main__":
    main()
