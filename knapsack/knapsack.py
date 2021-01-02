import itertools

maximumCapacity = 11

numbers = [5, 12, 3, 4]
numberOfItems = len(numbers)
print("numbers: ", numbers)

print("possible combinations: for a maximum capacity of %i" % maximumCapacity)

bestSolutionSum = 0
bestSolutionItems = ()

# calculate possible combinations of numbers
for runs in range(0, numberOfItems + 1):
    for subset in itertools.combinations(numbers, runs):
        temporarySum = 0
        if (len(subset)):
            for item in subset:
                temporarySum = temporarySum + item
            if (temporarySum <= maximumCapacity):
                print("solution (sum): ", subset, "(", temporarySum, ")")
                if (bestSolutionSum < temporarySum):
                    bestSolutionSum = temporarySum
                    bestSolutionItems = subset

print(" ")
print("best result:")
print("total for these values:", bestSolutionSum, bestSolutionItems)


