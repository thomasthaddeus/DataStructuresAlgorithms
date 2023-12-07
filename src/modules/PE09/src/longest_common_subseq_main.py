"""longest_common_subseq_main.py

Given two string sequences from the longest_common_subseq_main.py, complete the functions
in the separate "LCSClass" class within longest_common_subseq.py.
The main object of the "LCSClass" is to find the length of the longest common subsequence.

Examples:
-abca is a subsequence of abccefa with a length of 4
-adf is a subsequence of abcdef with a length of 3
-ebcf is a subsequence of aeebbefc with a length of 3
-vc is not a subsequence of asdf

"""

from longest_common_subseq import LCSClass


def main():
    """
    Main function to find the length of the longest common subsequence between string sequences.

    This function demonstrates the usage of the `LCSClass` to find the length of the longest common
    subsequence between different string sequences.
    """
    lcs = LCSClass()
    var1 = "aaebbecc"
    yar1 = "abc"
    result1 = lcs.find(var1, yar1)

    var2 = "aeebbefc"
    yar2 = "ebcf"
    result2 = lcs.find(var2, yar2)

    var3 = "asdf"
    yar3 = "vc"
    result3 = lcs.find(var3, yar3)
    print(f"LCS length: {result1}")
    print(f"LCS length: {result2}")
    print(f"LCS length: {result3}")

if __name__=="__main__":
    main()
