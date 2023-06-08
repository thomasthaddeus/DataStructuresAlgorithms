"""dijkstra.py
_summary_

_extended_summary_

Raises:
    ValueError: _description_
    ValueError: _description_
    ValueError: _description_
    ValueError: _description_

Returns:
    _type_: _description_
"""

from typing import Dict, Optional

class DijkstraClass:
    def __init__(self, graph: Dict[str, Dict[str, int]]):
        if not isinstance(graph, Dict):
            raise ValueError("Input graph must be a dictionary.")

        for node, edges in graph.items():
            if not isinstance(node, str) or not isinstance(edges, Dict):
                raise ValueError("Graph must be a dictionary of dictionaries.")

        self.graph = graph
        self.infinity = float("inf")
        self.costs = {}
        self.parents = {}
        self.processed = []

    def initial_costs_parents(self, start: str):
        if start not in self.graph:
            raise ValueError("Start node must be in the graph.")

        for node in self.graph:
            if node == start:
                self.costs[node] = 0
            else:
                self.costs[node] = self.infinity
            self.parents[node] = None

    def find_shortest_path(self, start: str, end: str):
        if start not in self.graph or end not in self.graph:
            raise ValueError("Both start and end nodes must be in the graph.")

        self.initial_costs_parents(start)
        node = start
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for i in neighbors.keys():
                new_cost = cost + neighbors[i]
                if i not in self.costs or new_cost < self.costs[i]:
                    self.costs[i] = new_cost
                    self.parents[i] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node(self.costs)

    def find_lowest_cost_node(self, costs: Dict[str, int]) -> Optional[str]:
        lowest_cost = self.infinity
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def print_path(self, start: str, end: str):
        self.find_shortest_path(start, end)
        node = end
        path = []
        while node is not None:
            path.append(node)
            node = self.parents.get(node, None)

        if len(path) == 1 and path[0] == end:
            print(f"No path from {start} to {end}")
        else:
            path.reverse()
            print(f"Shortest path from {start} to {end}: {path}")
