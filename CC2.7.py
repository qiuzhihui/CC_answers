class solution:
	def checkpalindrome(self,a):

		#bottom case check

		stack=[]
		head=a
		while(a.next!=None):
			stack.append(a.data)
			a=a.next

		while(head.next!=None):
			if(head.data!=stack.pop()) return False
			head=head.next

		return True

