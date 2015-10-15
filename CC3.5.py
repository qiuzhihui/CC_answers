class MyQueue:

	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def enqueue(self,data):
		self.stack1.append(data)



	def dequeue(self):

		if len(self.stack1)==0 and len(self.stack2)==0:
			print('dequeue from a empty array')
			return 

		if len(self.stack2)!=0:
			return self.stack2.pop()

		while(len(self.stack1)!=0):
			self.stack2.append(self.stack1.pop())

		return self.stack2.pop()


s=MyQueue()
s.enqueue(1)
print s.dequeue()
print s.dequeue()
