

class Node:
	def __init__(self,name=None,type=None):
		self.name=name
		self.type=type
		self.next=None



class Shelter:

	def __init__(self,head=None,tail=None):
		self.head=head
		self.tail=tail

	def enqueue(self,type,name):
		newnode=Node(name,type)
		if self.head==None:
			self.head=newnode
			self.tail=newnode
		else:
			self.tail.next=newnode
			self.tail=self.tail.next

	def dequeueany(self):
		output=self.head
		if self.head!=self.tail:
			self.head=self.head.next
		else:
			self.head=None
			self.tail=None
		return output

	def dequeuedog(self):
		tmp=self.head
		if self.head.type=='dog':
			return dequeueany()

		while(tmp.next!=None):
			if tmp.next.type=='dog':
				output=tmp.next
				tmp.next=tmp.next.next
				return output

		print('No dog in the shelter')
		return None

	def dequeuecat(self):
		tmp=self.head
		if self.head.type=='cat':
			return dequeueany()

		while(tmp.next!=None):
			if tmp.next.type=='cat':
				output=tmp.next
				tmp.next=tmp.next.next
				return output

		print('No cat in the shelter')
		return None



s=Shelter()
s.enqueue('dog','zach')
















