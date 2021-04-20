class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue():
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0

    def enqueue(self,node):
        node=Node(node)
        if self.first is None:
            self.first=node
            self.last=node
            self.length+=1
        else:
            self.last.next=node
            self.last=node
            self.length+=1

    def peek(self):
        return self.first.data

    def dequeue(self):
        z=self.first
        self.first=None
        self.first=z.next
        self.length-=1
        return z
    
    def lookup(self,value):
        node = self.first
        while node is not None and node.data!=value:
            node=node.next
        return node is not None

    def printQueue(self):
        node=self.first
        while node is not None:
            print(node.data,"--> ",end="")
            node=node.next
        print(None)
        
s = Queue()

s.enqueue(4)
s.enqueue(8)
s.enqueue(12)
s.enqueue(20)
s.dequeue()
s.printQueue()