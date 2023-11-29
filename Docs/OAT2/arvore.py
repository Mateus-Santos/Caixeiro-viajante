import node

node = node.Node()

class Arvore():
    def __init__(self):
        self.root = None

    def insert(current, value):
        if(current == None):
            current = node.Node(value)
        elif(value < node.getValue()):
            current.setLeft(Arvore().insert(node.getLeft(), value))
        elif(value > node.getValue()):
            current.setRight(Arvore().insert(node.getRight(), value))
        return current

    def delete(current, value):
        if(current == None):
            return None
        if(value < current.getValue()):
            current.setLeft(Arvore().delete(current.getLeft(), value))
        elif(value > current.getValue()):
            current.setRight(Arvore().delete(current.getRight(), value))
        else:
            sucessor = current
            prox = current.getRight()

            while(prox.getLeft() == None):
                sucessor = prox
                prox = prox.getLeft()
            
            if(sucessor != current):
                sucessor.setLeft(current.getLeft())
                sucessor.setRight(current.getRight())
            
            current.setValue(sucessor.getValue())

            return sucessor
        return current
    
    def busca(current, value):
        if(current == None):
            return -1
        if(current.getValue() == value):
            return value
        elif(value < current.getValue()):
            return Arvore().busca(current.getLeft(), value)
        else:
            return Arvore().busca(current.getRight(), value)