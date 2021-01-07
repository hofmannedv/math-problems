
# solution for the Knapsack problem:
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# method: decision tree in combination with Divide and Conquer
#
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

from treenode import TreeNode

# define maximum capacity of the bag
maximumCapacity = 15

# define the weight of the single items
numbers = [5, 12, 3, 4, 26, 8, 13, 1, 7, 11, 33, 10]

# print initial status
numberOfItems = len(numbers)
print("numbers: ", numbers)
print("calculating the possible combinations: for a maximum capacity of %i" % maximumCapacity)


