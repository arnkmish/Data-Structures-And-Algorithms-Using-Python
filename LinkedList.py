class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class SLinkedList:
	def __init__(self):
		self.headval = None
	
	# Function to print all the elements present in the list
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval

	# Function to insert at the beginging of the list
	def AtBegining(self,newdata):
		NewNode = Node(newdata)
		# Update the new nodes next val to existing node
		NewNode.nextval = self.headval
		self.headval = NewNode
	
	# Function to insert a new node at the end of the list
	def AtEnd(self, newdata):
		NewNode = Node(newdata)
		if self.headval is None:
			self.headval = NewNode
			return
		laste = self.headval
		while(laste.nextval):
			laste = laste.nextval
		laste.nextval=NewNode
	# Function to insert a newdata after a specified valAfter
	def InsertAfter(self,valAfter,newdata):
		if self.headval is None:
			print(f"The list is empty, so can't insert after {valAfter}")
			return
		NewNode = Node(newdata)
		currentNode = self.headval
		while(currentNode.dataval != valAfter):
			currentNode = currentNode.nextval
			if currentNode is None:
				print("The mentioned value is not present")
				return
		if currentNode.nextval is None:
			currentnode.nextval = NewNode
		else:
			tempNode = currentNode.nextval
			currentNode.nextval = NewNode
			NewNode.nextval = tempNode	
	# Function to delete element by key value
	def RemoveNode(self, Removekey):
		HeadVal = self.headval
		if HeadVal is None:
			print("The list is empty.")
			return
		if (HeadVal is not None):
			if (HeadVal.dataval == Removekey):
				self.headval = HeadVal.nextval
				HeadVal = None
				print("The element has been removed and it was the Head of the list")
				return
		remFlag = 0
		while (HeadVal.nextval is not None):
			if HeadVal.nextval.dataval == Removekey:
				remFlag = 1
				prev = HeadVal
				HeadVal = HeadVal.nextval
				break
			HeadVal = HeadVal.nextval
		if remFlag == 1:
			if prev.nextval.nextval is None:
				print("The element has been removed and it was the last element")
				prev.nextval = None
			else:
				print("The element has been removed it was a middle element")
				prev.nextval = prev.nextval.nextval
		else:
			print("Element not found")

llist = SLinkedList()
llist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
llist.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

llist.AtBegining("Sun")
llist.AtEnd("Thu")
llist.AtEnd("Sat")
llist.listprint()
llist.InsertAfter("Thu","Fri")
llist.listprint()
llist.RemoveNode("Tue")
llist.listprint()
