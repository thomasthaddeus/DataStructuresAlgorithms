"""knn_wrapper_main.py

Complete the functions in the separate "knnWrapperClass" class within
knn_wrapper.py, and edit the parameter on the "train" method call
from the main method to achieve 100% accuracy.

The "knnWrapperClass" object is used to implement a k-nearest classifier
wrapper and classify test data.

Files are in pair of "data" and "target," where their lows are synced, and each
data low is labeled with classes at the target file.
  Train files:
    iris_data.csv, iris_target.csv, wine_data.csv, wine_target.csv
  Test files:
    iris_test_data.csv, iris_test_target.csv,
    wine_test_data.csv, wine_test_target.csv

Result should achieve five 0s, five 1s, five 2s:
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
"""
# In a short paragraph, provide which 'neighbor' parameter works best for each
# dataset and describe tips on choosing the 'neighbor' value.
# Using the KNeighborsClassifier library from sklearn achieve a 100%
# classification rate on test data.

from src.knn_wrapper import KNNWrapperClass
from numpy import ndarray


def main() -> None:
    """
    Main function for executing KNN classification tasks on Iris and Wine
    datasets.

    This function creates two instances of the knnWrapperClass, importing
    training and test data for the Iris and Wine datasets. It trains the KNN
    classifier with 2 neighbors and makes predictions on the test data for each
    dataset, printing the results.
    """
    knnw = KNNWrapperClass()
    knnw.import_train_file("./data/iris_data.csv", "./data/iris_target.csv")
    knnw.train(3)
    knnw.import_test_file("D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/iris_test_data.csv", "D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/iris_test_target.csv")
    result: ndarray = knnw.predict()
    print(result)

    knnw2 = KNNWrapperClass()
    knnw2.import_train_file("D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/wine_data.csv", "D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/wine_target.csv")
    knnw2.train(3)
    knnw2.import_test_file("D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/wine_test_data.csv", "D:/Repositories/PEs/Algorithms/VL/assets/modules/PE10/data/wine_test_target.csv")
    result: ndarray = knnw2.predict()
    print(result)


if __name__ == "__main__":
    main()
