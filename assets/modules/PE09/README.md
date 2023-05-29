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

[main]: <./src/longest_common_subseq_main.py> "This is the Main python file that is already provided and contains the main and test procedure, which calls methods implemented on 'longest_common_subseq.py'."
[lcs]: <./src/longest_common_subseq.py> "the method returns the longest common subsequence length of given test string x and subsequence string y."
[Doc_ref]: <https://realpython.com/documenting-python-code/> "Mertz, J. (n.d.). Documenting Python Code: A Complete Guide."
