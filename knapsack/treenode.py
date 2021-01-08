
# TreeNode class for binary trees
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# (C) 2021 Frank Hofmann <frank.hofmann@efho.de>
# Released under GNU Public License 2.0

class TreeNode:
    def __init__(self, value, availableSpace, total):
        "constructor to initiate this object"
        # store value
        self.value = value
        self.availableSpace = availableSpace
        self.total = total

        # store references (left and right item)
        self.left = None
        self.right = None
        self.previousNode = None

        # invalid flag
        self.invalid = False
        return

    def __str__(self):
        print("value: %i, availableSpace: %i, total: %i" % (self.value,self.availableSpace, self.total))
        return

    def getData(self):
        "method to return the value of the node"
        return self.value

    def setData(self, value):
        "method to save or modify the node value"
        self.value = value
        return

    def getAvailableSpace(self):
        "method to return the available space of the knapsack"
        return self.availableSpace

    def setAvailableSpace(self, value):
        "method to save or modify the available space"
        self.availableSpace = value
        return

    def getTotal(self):
        "method to return the total of the knapsack"
        return self.total

    def setTotal(self, value):
        "method to save or modify the total"
        self.total = value
        return

    def getLeft(self):
        "method to return the node left to the current one"
        return self.left

    def setLeft(self, node):
        "method to set the node left to the current one"
        self.left = node
        return

    def getRight(self):
        "method to return the node right to the current one"
        return self.right

    def setRight(self, node):
        "method to set the node right to the current one"
        self.right = node
        return

    def getPreviousNode(self):
        "method to return the previous node"
        return self.previousNode

    def setPreviousNode(self, node):
        "method to set the previous node"
        self.previousNode = node
        return

    def isInvalidNode(self):
        "method to return the node state"
        return self.invalid

    def setValid(self):
        "method to set the node valid"
        self.invalid = False
        return

    def setInvalid(self):
        "method to set the node invalid"
        self.invalid = True
        return


