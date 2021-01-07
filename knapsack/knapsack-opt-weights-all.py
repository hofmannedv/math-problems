
# solution for the Knapsack problem:
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# optimization:
# ignore the numbers whose value is greater than the maximum capacity of
# the bag
# reduces the execution time by up to 25%
# calculates and prints all possible solutions
#
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

import itertools

# define maximum capacity of the bag
maximumCapacity = 15

# define the weight of the single items
numbers = [5, 12, 3, 4, 26, 8, 13, 1, 7, 11, 33, 10]

# print initial status
numberOfItems = len(numbers)
print("original numbers: ", numbers)
print("calculating the possible combinations: for a maximum capacity of %i" % maximumCapacity)

# remove the numbers that do not fit into the bag
adjustedNumbers = []
for entry in numbers:
    if (entry <= maximumCapacity):
        adjustedNumbers.append(entry)

# print corrected number set
numberOfItems = len(adjustedNumbers)
print("adjusted number set: ", adjustedNumbers)

# try to find all the solutions
# result will be a list 
solutionList = []
bestSolutionSum = 0
bestSolutionItems = ()

# calculate possible combinations of numbers
for runs in range(0, numberOfItems + 1):
    # calculate the combinations for the selected numbers
    for subset in itertools.combinations(adjustedNumbers, runs):
        # define intermediate total
        temporarySum = 0

        # the subset can be empty
        # continue with non-empty subsets, only
        if (len(subset)):
            # calculate the total for the current subset
            temporarySum = sum(subset)
            # are we still within the limit of our bag?
            if (temporarySum <= maximumCapacity) :
                solutionEntry = [temporarySum, subset]
                solutionList.append(solutionEntry)

# output the result
print(" ")
print("discovered results:")
for solutionEntry in solutionList:
    total, subset = solutionEntry
    print("solution (sum):", subset, "(", total, ")")

