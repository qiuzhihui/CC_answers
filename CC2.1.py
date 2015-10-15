class solution:

	def removedup(self,n):
		
		if n==None and n.next==None: return n

		head=n
		while(n.next!=null):
			while(n.data==n.next.data):
				n.next=n.next.next
				if(n.next==None): return head

			n=n.next
