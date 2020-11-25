class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            print('*')
            return self.root
        node = self.root
        while True:
            if node.data <= data:
                print('R',end='')
                if node.right == None:
                    node.right = Node(data)
                    print('*')
                    return self.root
                node = node.right
            else:
                print('L',end='')
                if node.left == None:
                    node.left = Node(data)
                    print('*')
                    return self.root
                node = node.left
                
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

tree = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for data in inp:
    tree.insert(data)