class stack_plates:

	def __init__(self):
		self.stacks=[[]]
		self.index=0

	def push(self,data):

		#if the stack is not full
		if len(self.stacks[self.index])<=10:
			self.stacks[self.index].append(data)

		# if the stack in use is full
		else:
			self.index+=1
			self.stacks.append(data)


	def pop(self):



		#if the stack is empty
		if (len(self.stacks[self.index])==0):
			if self.index==0:
				print('stack is empty, unable to pop!')
				return None
			else:
				self.index-=1

		output=self.stacks[self.index].pop()
		return output



s=stack_plates()
s.push(1)
s.pop()
s.pop()





