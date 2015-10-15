class solution:
	def setzero(self,m,x,y):
		r=[0]*x
		c=[0]*y

		for i in range(x):
			for j in range(y):
				if m[i][j]==0:
					r[i]=1
					c[j]=1

		for i in range(x):
			if r[i]==1:
				for j in range(y):
					m[i][j]=0

		for j in range(y):
			if c[j]==1:
				for i in range(x):
					m[i][j]=0

		return m


s=solution()
print s.setzero([[1,0],[1,1]],2,2)