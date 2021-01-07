
# solution for the Knapsack problem:
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

import itertools

# define maximum capacity of the bag
maximumCapacity = 15

# define the weight of the single items
numbers = [5, 12, 3, 4, 6, 8, 13]

# print initial status
numberOfItems = len(numbers)
print("numbers: ", numbers)
print("calculating the possible combinations: for a maximum capacity of %i" % maximumCapacity)

# try to find one of the best solutions
# result will show just one, also if more than one exist
bestSolutionSum = 0
bestSolutionItems = ()

# calculate possible combinations of numbers
for runs in range(0, numberOfItems + 1):
    # calculate the combinations for the selected numbers
    for subset in itertools.combinations(numbers, runs):
        # define intermediate total
        temporarySum = 0

        # the subset can be empty
        # continue with non-empty subsets, only
        if (len(subset)):
            # calculate the total for the current subset
            temporarySum = sum(subset)
            # are we still within the limit of our bag?
            if (temporarySum <= maximumCapacity):
                print("solution (sum): ", subset, "(", temporarySum, ")")
                # is the new solution better than the one we already have?
                if (bestSolutionSum < temporarySum):
                    bestSolutionSum = temporarySum
                    bestSolutionItems = subset

# output the result
print(" ")
print("best result:")
print("total for these values:", bestSolutionSum, bestSolutionItems)


