class solution:

	def ifunique(self,a):
		a.sort()
		for i in range(len(a)-1):
			if a[i]==a[i+1]: return False
		return True


	def ifunique1(self,b):
		s=set()
		for c in b:
			if c in s: return False
			else: s.add(c)
		return True





x=solution()
print(x.ifunique1([1,2,3,4,5,5]))