
# solution for the Knapsack problem:
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# method: decision tree in combination with Divide and Conquer
#
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

from treenode import TreeNode

def buildTree(numbers, availableSpace, total, previousNode):
    tree = []
    nodeIsValid = True

    # print initial status
    numberOfItems = len(numbers)
    print(" ")
    print("numbers: ", numbers)
    print("calculating the possible combinations: for a maximum capacity of %i" % availableSpace)

    if (numberOfItems == 0):
        print("skipping empty list of numbers")
        node = []
    elif (numberOfItems == 1):
        value = numbers[0]

        # recalculate available and used space
        if (availableSpace >= value):
            availableSpace = availableSpace - value
            total = total + value
        else:
            # the required space is too small
            nodeIsValid = False

        # initiate a new node
        node = TreeNode(value, availableSpace, total)

        print("added new node:", value)
        if (nodeIsValid == False):
            print("node is invalid")
            node.setInvalid()
        else:
            node.setValid()

        print("available space left: %i" % availableSpace)
        print("space in use:", total)

    else:
        # calculate the middlest item
        nodePosition = int(numberOfItems/2)
        value = numbers[nodePosition]

        # recalculate available and used space
        if (availableSpace >= value):
            availableSpace = availableSpace - value
            total = total + value
        else:
            # the required space is too small
            nodeIsValid = False

        # initiate this node as a new node
        node = TreeNode(value, availableSpace, total)

        print("added new node:", value)
        if (nodeIsValid == False):
            print("node is invalid")
            node.setInvalid()
        else:
            node.setValid()

        print("available space left: %i" % availableSpace)
        print("space in use:", total)

        # calculate subtree for the numbers left of the node value
        leftSubtree = buildTree(numbers[0:nodePosition], availableSpace, total, node)
        if (len(leftSubtree)):
            firstNode = leftSubtree[0]
            if isinstance(firstNode, TreeNode):
                if (firstNode.isInvalidNode()):
                    # invalid nodes belong to the right side
                    node.setRight(leftSubtree)
                else:
                    # valid nodes belong to the left side
                    node.setLeft(leftSubtree)

        # calculate subtree for the numbers right of the node value
        if (nodePosition < numberOfItems):
            rightSubtree = buildTree(numbers[nodePosition+1:], availableSpace, total, node)
        else:
            rightSubtree = []
        if (len(rightSubtree)):
            firstNode = rightSubtree[0]
            if isinstance(firstNode, TreeNode):
                if (firstNode.isInvalidNode()):
                    # invalid nodes belong to the right side
                    node.setRight(rightSubtree)
                else:
                    # valid nodes belong to the left side
                    node.setLeft(rightSubtree)

    # add the newly built node to the tree
    tree.append(node)

    print(tree)
    return tree

def printTree(node):
    result = []
    if node is None:
        print("empty node")
        return None

    if (type(node) is list):
        print("list")
        for subNode in node:
            result = printTree(subNode)

    if (isinstance(node, TreeNode)):
        value = node.getData()
        print("node:", value)
        if not node.isInvalidNode():
            result.append(value)

        leftSubtree = node.getLeft()
        if leftSubtree is not None:
            print("left subtree of %i (start)" % value)
            result.append(printTree(leftSubtree))
            print("left subtree of %i (end)"  % value)

        rightSubtree = node.getRight()
        if rightSubtree is not None:
            print("right subtree of %i (start)"  % value)
            result.append(printTree(rightSubtree))
            print("right subtree of %i (end)" % value)

    return result

def flattenList(data):
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            flattenList(element)
        else:
            flatList.append(element)
    return

# define maximum capacity of the bag
maximumCapacity = 15

# define the weight of the single items
numbers = [5, 12, 3, 4, 26, 8, 13, 1, 7, 11, 33, 10]

# sort numbers in ascending order
numbers.sort()
print("sorted numbers: ", numbers)

# remove numbers that exceed the maximum capacity of the bag
for position in range(len(numbers)):
    if (numbers[position] > maximumCapacity):
        numbers = numbers[0:position]
        break

print("cleaned value set:", numbers)

# define total
total = 0

# calculate tree
tree = buildTree(numbers, maximumCapacity, total, None)

print(" ")
result = printTree(tree)

# flatten the output (nested list)
flatList = []
flattenList(result)
print(" ")
print("result (one possible solution):", flatList)
