class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        nodeToInsert=Node(data)
        if self.root is None:
            self.root=nodeToInsert
        else:
            node=self.root
            ok=True
            while ok is True:
                if nodeToInsert.data <= node.data:
                    if node.left is None:
                        node.left=nodeToInsert
                        ok=False
                    node = node.left
                else:
                    if node.right is None:
                        node.right=nodeToInsert
                        ok=False
                    node = node.right

    def removeData(self,data):
        nodeToRemove = Node(data)
        node=self.root
        while node is not None and node.data!=nodeToRemove.data:
            parent = node
            if nodeToRemove.data < node.data:
                node=node.left
            else:
                node=node.right
        if node.left is not None:
            parent.left = node.left
        if node.right is not None:
            parent.right = node.right


def printTree(node,string):
    print(string,node.data)
    string = string
    if node.left is not None:
        printTree(node.left,"Child of "+str(node.data)+" -left:")
    if node.right is not None:
       printTree(node.right,"Child of "+str(node.data)+" -right:")


tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(1)
tree.insert(20)

tree.removeData(5)
printTree(tree.root,"root:")
