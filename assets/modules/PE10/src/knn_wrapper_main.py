"""knn_wrapper_main.py

This assignment is to learn about k-nearest neighbors.
Given two data sets, complete the functions in the separate "knnWrapperClass" class within knn_wrapper.py,
and edit the parameter on the "train" method call from the main method to achieve 100% accuracy.
The "knnWrapperClass" object is to implement a k-nearest classifier wrapper and classify test data.
Note that you are allowed to use the KNeighborsClassifier library from sklearn, and you need to achieve a 100% classification rate on test data.
In short paragraph, provide which 'neighbor' parameter works best for each dataset and describe tips on choosing the 'neighbor' value.

-Files are in pair of "data" and "target," where their lows are synced, and each data low is labeled with classes at the target file.
  Train files: iris_data.csv, iris_target.csv, wine_data.csv, wine_target.csv
  Test files: iris_test_data.csv, iris_test_target.csv, wine_test_data.csv, wine_test_target.csv

-Result should achieve five 0s, five 1s, five 2s:
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
  [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]


"""
from knn_wrapper import knnWrapperClass


def main():

    knnW = knnWrapperClass()
    knnW.import_train_file("iris_data.csv", "iris_target.csv")
    # have set neighbor n value as 2, but please find better value
    knnW.train(2)
    knnW.import_test_file("iris_test_data.csv", "iris_test_target.csv")
    result = knnW.predict()
    print(result)

    knnW = knnWrapperClass()
    knnW.import_train_file("wine_data.csv", "wine_target.csv")
    knnW.train(2)
    knnW.import_test_file("wine_test_data.csv", "wine_test_target.csv")
    result = knnW.predict()
    print(result)


if __name__ == "__main__":
    main()
