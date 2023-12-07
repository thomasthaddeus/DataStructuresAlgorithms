"""island_counter.py

This module contains a class, IslandCounterClass, which is responsible for
counting the number of islands in a 2D grid. Each cell in the grid is either
land ('1') or water ('0'). An island is defined as a group of '1's (land)
connected vertically or horizontally. The grid can be of any size.

The IslandCounterClass has the following methods:
- print_grid_visited: Prints the input grid and the cells that have been visited
                                                         during the island count.
- count_island: Counts the number of islands in the grid. It marks cells as
                                    visited when they are part of an island.
- mark_visited_island: Marks all cells of an island as visited. It uses a
                                      Breadth-First Search (BFS) approach.
"""

from typing import List
from collections import deque

WTR = "0"
LND = "1"
VIS = True
NOT_VIS = False
DIR: list = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up


class IslandCounterClass:
    """
    A class used to count the number of islands in a 2D grid.

    Attributes:
        grid (List[List[str]]): A 2D list representing a map, where '1' represents
                                land and '0' represents water.
        visited (List[List[bool]]): A 2D list that keeps track of the cells that
                                    have been visited during the island count.

    Methods:
        print_grid_visited(): Prints the input grid and the cells that have been
                              visited during the island count.
        count_island() -> int: Counts and returns the number of islands in the grid.
                               Marks cells as visited when they are part of an island.
        mark_visited_island(x: int, y: int): Marks all cells of an island as visited.
                            It uses a Breadth-First Search (BFS) approach.
        is_valid_land(x: int, y: int) -> bool: Checks if a cell is a valid part of an
            island (i.e., it is within the grid boundaries, is land, and is unvisited).
        visit(x: int, y: int): Marks a cell as visited.
    """

    def __init__(self, grid: List[List[str]]) -> None:
        """
        Initializes an instance of the IslandCounterClass with the provided grid.

        Args:
            grid (List[List[str]]): A 2D list representing a map, where '1'
            represents land and '0' represents water.
        """
        self.grid: List[List[str]] = grid
        self.visited: list[list[bool]] = [[NOT_VIS for _ in row] for row in grid]

    def print_grid_visited(self) -> None:
        """
        Prints the input grid and the cells that have been visited during
        the island count.
        """
        print("Map:")
        print("\n".join(["\t".join(row) for row in self.grid]))
        print("Visited:")
        print("\n".join(["\t".join(str(cell) for cell in row) for row in self.visited]))

    def count_island(self) -> int:
        """
        Counts and returns the number of islands in the grid. Marks cells as
        visited when they are part of an island.

        Returns:
            int: The number of islands in the grid.
        """
        res = 0
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == LND and not self.visited[i][j]:
                    res += 1
                    self.mark_visited_island(i, j)
        return res

    def mark_visited_island(self, xcrd, ycrd) -> None:
        """
        Marks all cells of an island as visited using a Breadth-First Search (BFS) approach.

        Args:
            x (int): The x-coordinate of the starting cell.
            y (int): The y-coordinate of the starting cell.
        """
        queue = deque([(xcrd, ycrd)])

        while queue:
            cur_x, cur_y = queue.popleft()
            if self.is_valid_land(cur_x, cur_y):
                self.visit(cur_x, cur_y)
                for dir_x, dir_y in DIR:
                    queue.append((cur_x + dir_x, cur_y + dir_y))

    def is_valid_land(self, xcrd: int, ycrd: int) -> bool:
        """
        Checks if a cell is a valid part of an island (i.e., it is within the
            grid boundaries, is land, and is unvisited).

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            bool: True if the cell is a valid part of an island, False otherwise.
        """
        return (0 <= xcrd < len(self.grid)
            and 0 <= ycrd < len(self.grid[0])
            and self.grid[xcrd][ycrd] == LND
            and not self.visited[xcrd][ycrd]
        )

    def visit(self, xcrd: int, ycrd: int) -> None:
        """
        Marks a cell as visited.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
        """
        self.visited[xcrd][ycrd] = VIS
