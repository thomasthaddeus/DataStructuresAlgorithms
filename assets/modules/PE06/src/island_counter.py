"""island_counter.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

from collections import deque


class IslandCounterClass:
    """
    This class takes a grid as input and provides methods
    to count the number of islands within the grid.
    """

    def __init__(self, grid):
        """
        Initializes an instance of the IslandCounterClass with the provided grid.

        Args:
            grid (List[List[int]]): A 2D list representing a map,
            where '1' represents land and '0' represents water.
        """
        self.grid = grid
        self.visited = [["0" for x in range(len(grid[0]))] for y in range(len(grid))]

    def print_grid_visited(self):
        """
        Prints the grid (map) and the visited cells.
        """
        print("Map:")
        print("\n".join(["\t".join([str(cell) for cell in row]) for row in self.grid]))
        print("Visited:")
        print(
            "\n".join(["\t".join([str(cell) for cell in row]) for row in self.visited])
        )

    def count_island(self):
        """
        Counts the number of islands in the grid while marking visited cells.

        Returns:
            int: The number of islands in the grid.
        """
        result = 0
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if cell == '1' and self.visited[x][y] == '0':
                    result += 1
                    self.mark_visited_island(x, y)
        return result

    def mark_visited_island(self, x, y):
        """
        Marks unvisited island cells as visited using a Breadth-First Search (BFS) approach.

        Args:
            x (int): The x-coordinate of the starting cell.
            y (int): The y-coordinate of the starting cell.
        """
        queue_x = deque([x])
        queue_y = deque([y])

        while queue_x:
            current_x = queue_x.popleft()
            current_y = queue_y.popleft()

            if 0 <= current_x < len(self.grid) and 0 <= current_y < len(self.grid[0]) and self.grid[current_x][current_y] == '1' and self.visited[current_x][current_y] == '0':
                self.visited[current_x][current_y] = '1'

                # Check neighboring cells
                queue_x.extend([current_x - 1, current_x + 1, current_x, current_x])
                queue_y.extend([current_y, current_y, current_y - 1, current_y + 1])
