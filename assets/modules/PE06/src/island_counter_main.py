"""island_counter_main.py

This script demonstrates the usage of the IslandCounterClass to count the number of islands in a grid representation of a map.

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.
"""

from island_counter import IslandCounterClass

grid_one_island = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid_three_island = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def main():
    """runs the main function of the program"""
    print("One island test")
    ic_one = IslandCounterClass(grid_one_island)
    print("\n---Before visited---")
    ic_one.print_grid_visited()
    result = ic_one.count_island()
    print("\n---After visited---")
    ic_one.print_grid_visited()
    print(f"\nCounted: {result} \n")

    print("\n\nThree island test")
    ic_three = IslandCounterClass(grid_three_island)
    print("\n---Before visited---")
    ic_three.print_grid_visited()
    result = ic_three.count_island()
    print("\n---After visited---")
    ic_three.print_grid_visited()
    print(f"\nCounted: {result} \n")


if __name__ == "__main__":
    main()
