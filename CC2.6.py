class solution:

	def permutation(self,a,b):

		#check error
		if(len(a)!=len(b)): return False

		#create array
		check=[0]*256


		#check if they have same number of char
		for i in range(len(a)):
			check[ord(a[i])]+=1

		for i in range(len(a)):
			check[ord(b[i])]-=1

		for i in range(256):
			if check[i]!=0: return False

		return True







s=solution()
print(s.permutation('aaaa','aaaa'))