class solution:

	def countchar(self,s):

		olen=len(s)
		news=''
		tmp=s[0]
		count=0

		for i in range(olen):
			

			if s[i]!=tmp:
				news+=str(count)+tmp
				tmp=s[i]
				count=1
			else:
				count+=1

			if i==olen-1: 
				news+= str(count)+tmp 

		if len(news)>len(s): 
			return s
		else:
			return news


s=solution()
print(s.countchar('a'))




