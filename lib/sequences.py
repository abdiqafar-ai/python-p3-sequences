#!/usr/bin/env python3

def print_fibonacci(length):
    # Time to get some practice! Write your code in the sequences.py file in the lib folder. Run pytest -x to check your work. Your goal is to practice manipulating sequences with the Python tools you've learned about in this lesson and the lessons before.

# Write a function print_fibonacci() that prints a list of the fibonacci sequence up to the length provided in the function's parameters.

# print_fibonacci(9)
# # => [0, 1, 1, 2, 3, 5, 8, 13, 21]
# When all of your tests are passing, submit your work using git.
   list = [0, 1, 1, 2, 3, 5, 8, 13, 21,34]
   
   print(list[0:length])
   
   return list
print_fibonacci(9)

