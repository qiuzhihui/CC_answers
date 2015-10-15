class solution:
	def findkth(self,node):

		if (node==None or node.next=None) return False

		node.data=node.next.data
		node.next=node.next.next
		return True



