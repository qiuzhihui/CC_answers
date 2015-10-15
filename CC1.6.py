class solution:
	def rotate90(self,m):
		l=len(m)-1


		for i in range(l-1):

			for j in range(l):

				tmp=m[j+i][l-i]   #tmp=01
				m[j+i][l-i]=m[i][j+i]   #01=00
				m[i][j+i]=tmp           #00=tmp

				tmp=m[l-i][l-j-i]    #tmp=11
				m[l-i][l-j-i]=m[i][j+i]  
				m[i][j+i]=tmp 

				tmp=m[l-j-i][i]
				m[l-j-i][i]=m[i][j+i]
				m[i][j+i]=tmp 

		return m



s=solution()
print(s.rotate90(list([[1,2,3],[4,5,6],[7,8,9]])))






