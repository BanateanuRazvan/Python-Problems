class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack():
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0

    def push(self,node):
        node=Node(node)
        if self.top is None:
            self.top=node
            self.bottom=node
            self.length+=1
        else:
            node.next=self.top
            self.top=node
            self.length+=1

    def peek(self):
        return self.top.data

    def pop(self):
        z=self.top
        self.top=None
        self.top=z.next
        self.length-=1
        return z
    
    def lookup(self,value):
        node = self.top
        while node is not None and node.data!=value:
            node=node.next
        return node is not None

    def printStack(self):
        node=self.top
        while node is not None:
            print(node.data,"--> ",end="")
            node=node.next
        print(None)
        
s = Stack()

s.push(4)
s.push(8)
s.push(12)
s.push(20)
s.pop()
s.printStack()