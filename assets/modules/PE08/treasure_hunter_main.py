"""treasure_hunter_main.py

This assignment is to learn about the Greedy algorithm.
Given a hunters and treasures locations from the treasure_hunter_main.py, complete the functions
in the separate "TreasureHunterClass" class within treasure_hunter.py. 
The main object of the "TreasureHunterClass" is to find the maximum treasures with given hunters.

An array of size n is constructed with the following specifications:
-Each element in the array contains either a hunter(H) or a treasure(T).
-Each hunter can find only one treasure.
-A hunter cannot catch a treasure where is more than K units away from the hunter.

"""
from treasure_hunter import TreasureHunterClass


def main():
    th1 = TreasureHunterClass()
    arr1 = ['H', 'T', 'T', 'H', 'T'] 
    k = 2
    n = len(arr1)
    result = th1.hunt_treasure(arr1, n, k)
    print("Maximum treasures found: %s" % result)
  
    th2 = TreasureHunterClass()
    arr2 = ['T', 'T', 'H', 'H', 'T', 'H'] 
    k = 2
    n = len(arr2) 
    result = th2.hunt_treasure(arr2, n, k)
    print("Maximum treasures found: %s" % result)
  
    th3 = TreasureHunterClass()
    arr3 = ['H', 'T', 'H', 'T', 'T', 'H'] 
    k = 3
    n = len(arr3) 
    result = th3.hunt_treasure(arr3, n, k)
    print("Maximum treasures found: %s" % result)

if __name__ == "__main__":
        main()
