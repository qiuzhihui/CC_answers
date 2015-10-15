class solution:
	def spacereplace(self,s,l):

		index=len(s)-1
		s=list(s)  



		for i in range(l-1,-1,-1):
			if s[i]==' ': 
				s[index],index='0',index-1
				s[index],index='2',index-1
				s[index],index='%',index-1

			else:
				s[index],index=s[i],index-1

		return ''.join(s)




s=solution()

print (s.spacereplace(' ad  ',3))