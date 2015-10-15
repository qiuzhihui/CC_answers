class solution:

	def nextnumber(self,n):

		for i in range(32):
			if((n&(1<<i))!=0 and (n&(1<<(i+1)))==0):
				nextlarge = n & (~(1<<i)) | (1<<(i+1))
		
		for i in range(32):
			if((n&(1<<i))==0 and (n&(1<<(i+1)))!=0):
				nextsmall = (n | (1<<i) ) & (~(1<<(i+1)))

		return nextsmall





s=solution()

print(s.nextnumber(2))








