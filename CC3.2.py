class minstack:

	def __init__(self):
		self.stack=[]
		self.stackmin=[]


	def push(self,data):

		#if the stack is empty
		if(len(self.stack)==0):
			self.stack.append(data)
			self.stackmin.append(data)
			return None

		#if the stack is not empty
		self.stack.append(data)
		if data<=self.stackmin[-1]:
			self.stackmin.append(data)


	def pop(self):
		#check if stack is empty
		if(len(self.stack)==0):
			print('Stack is empty!')
			return None

		output=self.stack.pop()
		if(output==self.stackmin[-1]):
			self.stackmin.pop()

		return output



	def getmin(self):
		if len(self.stackmin)==0:
			print('stack is empty!')
			return None
		return self.stackmin[-1]


s=minstack()
s.push(1)
print s.getmin()
print s.pop()





