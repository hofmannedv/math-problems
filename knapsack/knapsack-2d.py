
# solution for the Knapsack problem:
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# two-dimensional version -- numbers and weights
# 
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

import itertools

# define maximum capacity of the bag
maximumCapacity = 15

# define the weight of the single items
numbers = [5, 12, 3, 4, 26, 8, 13, 1, 7, 11, 33, 10]
weights = [10, 7, 12, 15, 6, 5, 18, 40, 8, 6, 1, 13]
nw = []
for i in range(len(numbers)):
    nw.append([numbers[i], weights[i]])

# print initial status
numberOfItems = len(nw)
print("numbers: ", numbers)
print("weights: ", weights)
print("calculating the possible combinations: for a maximum capacity of %i" % maximumCapacity)

# try to find one of the best solutions
# result will show just one, also if more than one exist
bestSolutionSum = 0
bestSolutionWeight = 0
bestSolutionItems = ()

# calculate possible combinations of numbers
for runs in range(0, numberOfItems + 1):
    # calculate the combinations for the selected numbers
    for subset in itertools.combinations(nw, runs):
        # define intermediate total
        temporarySum = 0
        temporaryWeight = 0

        # the subset can be empty
        # continue with non-empty subsets, only
        if (len(subset)):
            # calculate the total for the current subset
            for item in subset:
                temporarySum = temporarySum + item[0]
                temporaryWeight = temporaryWeight + item[1]

            # are we still within the limit of our bag?
            if (temporarySum <= maximumCapacity):
                print("solution (sum, weight): ", subset, "(", temporarySum, temporaryWeight,  ")")
                # is the new solution better than the one we already have?
                if (bestSolutionSum <= temporarySum):
                    if (bestSolutionWeight < temporaryWeight):
                        bestSolutionSum = temporarySum
                        bestSolutionWeight = temporaryWeight
                        bestSolutionItems = subset

# output the result
print(" ")
print("best result:")
print("total for these values (sum, weight, items): %i, %i" % (bestSolutionSum, bestSolutionWeight), bestSolutionItems)

