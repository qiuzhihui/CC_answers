class threestack:

	def __init__(self):
		self.stack=30*[None]
		self.index=[0,10,20]
		

	def push(self,num,data):
		if(self.index[num-1]>(10*(num-1)+9)):
			print ('stack'+str(num) +' is full!')
			return -1
		self.stack[self.index[num-1]]=data
		self.index[num-1]+=1


	def pop(self,num):
		if(self.index[num-1]==(10*(num-1))):
			print ('stack'+str(num) +' is empty!')
			return -1
		self.index[num-1]-=1
		output=self.stack[self.index[num-1]]
		
		return output


s=threestack()
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)
s.push(3,4)

print(s.pop(3))

