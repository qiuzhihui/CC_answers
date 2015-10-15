class solution:
	def isnertnumber(self,a,b,i,j):

		a=self.set0(a,i,j)
		output=a|(b<<i)
		return output




	def set0(self,a,i,j):

		for k in range(i,j+1):
			a=a & (~(1<<k))
		return a




s=solution()
a=8
b=3
print bin(a)
a=s.isnertnumber(a,b,0,1)
print bin(a)