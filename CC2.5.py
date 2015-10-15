


class solution:
	def addlinkedlist(self,a,b):
		if a==None: return b
		if b==None: return a


		count=0
		tmp=0
		result=0
		iteration=0
		while(a.next!=None and b.next!=None):
			tmp=(a.data+b.data)%10 + count
			count=(a.data+b.data)/10

			result=tmp*(10**iteration)
			iteration+=1

		while(a.next!=None):
			tmp=a.data + count
			result=tmp*(10**iteration)
			iteration+=1
			count=0

		while(b.next!=None):
			tmp=b.data + count
			result=tmp*(10**iteration)
			iteration+=1
			count=0

		return result


