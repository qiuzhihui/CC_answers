class solution:
	def patition(self,head,k):

		if head==None or head.next==None: return head
		smaller=Node()
		greater=Node()
		shead,ghead=smaller,greater

		while(head.next!=None):
			if head.data<k:
				smaller.next=head
				smaller=smaller.next
			else:
				greater.next=head
				greater=greater.next

			head=head.next


		smaller.next=ghead.next

		return shead.next




