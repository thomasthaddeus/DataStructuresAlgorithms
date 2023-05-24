"""treasure_hunter_main.py

This assignment is to learn about the Greedy algorithm.
Given a hunters and treasures locations from the treasure_hunter_main.py,
complete the functions in the separate "TreasureHunterClass" class within
treasure_hunter.py. The main object of the "TreasureHunterClass" is to find
the maximum treasures with given hunters.

An array of size n is constructed with the following specifications:
-Each element in the array contains either a hunter(H) or a treasure(T).
-Each hunter can find only one treasure.
-A hunter cannot catch a treasure where is more than K units away from the hunter.

"""

from treasurehunt.treasure_hunter import TreasureHunterClass


def main() -> None:
    """
    The main function runs a few scenarios of treasure hunting.

    It creates instances of TreasureHunterClass and provides them with hunters
    and treasures configurations. It then calls the hunt_treasure method to
    find out the maximum number of treasures that can be collected by the hunters.
    """
    # Treasure hunt 1
    arr1: list[str] = ["H", "T", "T", "H", "T"]
    k1 = 2
    num1: int = len(arr1)
    th1 = TreasureHunterClass(arr1, num1, k1)
    result1: int = th1.hunt_treasure()
    print(f"Maximum treasures found: {result1}")

    # Treasure Hunt 2
    arr2: list[str] = ["T", "T", "H", "H", "T", "H"]
    k2 = 2
    num2: int = len(arr2)
    th2 = TreasureHunterClass(arr2, num2, k2)
    result2: int = th2.hunt_treasure()
    print(f"Maximum treasures found: {result2}")

    # Treasure Hunt 3
    arr3: list[str] = ["H", "T", "H", "T", "T", "H"]
    k3 = 3
    num3: int = len(arr3)
    th3 = TreasureHunterClass(arr3, num3, k3)
    result3: int = th3.hunt_treasure()
    print(f"Maximum treasures found: {result3}")


if __name__ == "__main__":
    main()
