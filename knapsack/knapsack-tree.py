class TreeNode:
    def __init__(self, data):
        "constructor to initiate this object"
        # store data
        self.data = data

        # store references (left and right item)
        self.left = None
        self.right = None
        return

    def getData(self):
        "method to return the value of the node"
        return self.data

    def setData(self, value):
        "method to save or modify the node value"
        self.data = value
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


