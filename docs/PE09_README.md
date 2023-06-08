# PE09: Programming Exercise

## Instructions: Programming Assignment #9: Dynamic Programming

[main]
[lcs]

### Description

[Doc_ref]

This assignment is to learn about Dynamic Programming.

Given two string sequences from the `longest_common_subseq_main.py`, complete the functions in the separate `LCSClass` class within `longest_common_subseq.py`. The main object of the `LCSClass` is to find the length of the longest common subsequence.
Note that `longest_common_subseq_main.py` with the `main` method and starter file `longest_common_subseq.py` with class has already been provided. Keep in mind to always comment and document your class and methods.

### Examples

- abca is a subsequence of abccefa with a length of 4
- adf is a subsequence of abcdef with a length of 3
- ebcf is a subsequence of aeebbefc with a length of 3
- vc is not a subsequence of asdf

### Expected result

#### longest_common_subseq_main.py

> This is the Main python file that is already provided and contains the main and test procedure, which calls methods implemented on "longest_common_subseq.py".

#### longest_common_subseq.py

> This class contains such methods as `init`, `find`. Please keep in mind the following notes for each method during implementation:
`init()`: this method has already been provided.
`find(x, y)`: the method returns the longest common subsequence length of given test string x and subsequence string y.
**Parameters**: test string 'x', possible subsequence string 'y'

## Recursive Performance

Describe how the algorithms can be implemented recursively and how it would perform.

> This algorithm exhibits good performance due to the use of memoization, which prevents the same subproblems from being solved multiple times. Thus, the recursive nature of the function does not significantly degrade its performance. This algorithm can be implemented recursively, the idea is to compare characters of the two input strings str_x and str_y. For every index in the strings:
> - If characters match, we increase our count and move diagonally in the dp-matrix.
> - If characters do not match, the subsequence can be found either by ignoring the current character of str_x or ignoring the current character of str_y. We then move left or up in the dp-matrix and take the maximum count from both moves.
> - If either string is empty, we return 0 since an empty string cannot have a common subsequence.
> The performance of this algorithm is generally `O(n*m)` where `n` and `m` are the lengths of the two strings. This is because for every combination of indexes `(i, j)` in the strings `(1 <= i <= n, 1 <= j <= m)`, we're solving the subproblem for indices `(i, j)` only once.

[main]: <./src/longest_common_subseq_main.py> "This is the Main python file that is already provided and contains the main and test procedure, which calls methods implemented on 'longest_common_subseq.py'."
[lcs]: <./src/longest_common_subseq.py> "the method returns the longest common subsequence length of given test string x and subsequence string y."
[Doc_ref]: <https://realpython.com/documenting-python-code/> "Mertz, J. (n.d.). Documenting Python Code: A Complete Guide."
