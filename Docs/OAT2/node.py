class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setValue(self, value):
        self.value = value

    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right