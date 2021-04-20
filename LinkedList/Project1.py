class Node:
	def __init__(self,value):
		self.value=value
		self.next=None
		self.prev=None

class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None

	def setHead(self,node):
		self.removeBoundings(node)
		if self.head is None:
			self.head=node
			self.tail=node
			return
		self.insertBefore(self.head,node)

		
	
	def setTail(self,node):
		self.removeBoundings(node)
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(node)

	def remove(self,node):
		if node==self.head:
			self.head=self.head.next
		if node==self.tail:
			self.tail=self.tail.prev
		self.removeBoundings(node)

	def removeBoundings(self,node):
		if node.prev is not None:
			node.prev.next=node.next
		if node.next is not None:
			node.next.prev=node.prev
		node.next=None
		node.prev=None

	def insertAfter(self,node,nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert==self.tail:
			return
		self.removeBoundings(nodeToInsert)
		nodeToInsert.prev=node
		nodeToInsert.next=node.next
		if node.next is None:
			self.tail=nodeToInsert
		else:
			node.next.prev=nodeToInsert
		node.next=nodeToInsert


	def insertBefore(self,node,nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert==self.tail:
			return
		self.removeBoundings(nodeToInsert)
		nodeToInsert.next=node
		nodeToInsert.prev=node.prev
		if node.prev is None:
			self.head=nodeToInsert
		else:
			node.prev.next=nodeToInsert
		node.prev=nodeToInsert

	def insertAtPosition(self,position,nodeToInsert):
		pos=1
		node=nodeToInsert
		if position==1:
			self.setHead(nodeToInsert)
			return
		while node is not None and pos!=position:
			node=node.next
			pos+=1
			if node is not None:
				self.insertBefore(node,nodeToInsert)
			else:
				self.setTail(nodeToInserd)



	def removeNodeWithValue(self,value):
		node=self.head
		while node is not None:
			nodeToRemove=node
			if nodenodeToRemove.value==value:
				self.remove(nodeToRemove)
			node=node.next


	def findNodeWithValue(self,value):
		node=self.head
		while node is not None and node.value!=value:
			node=node.next
		return node is not None

	def printList(self):
		node=self.head
		while node is not None:
			print(node.value,"--> ", end="")
			node=node.next
		print(None)


	def reverseList(self):
		p1,p2=None,self.head
		while p2 is not None:
			p3=p2.next
			p2.next=p1
			p1=p2
			p2=p3
		self.head=p1
		return p1

list = LinkedList()

x=Node(10)
y=Node(5)
z=Node(3)
w=Node(2)
u=Node(20)

list.setHead(x)
list.insertAfter(x,y)
list.insertAfter(y,z)
list.insertAtPosition(1,u)
list.reverseList()
list.printList()


