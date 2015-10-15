class solution:
	def findkth(self,head,k):
		fast=head

		for i in range(k-1):
			fast=fast.next

		while(fast.next!=None):
			fast=fast.next
			head=head.next

		return head