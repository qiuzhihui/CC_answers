class solution:

	def creatlink(self,treehead):

		q=[]
		output=[[]]
		lvl=0

		q.append(treehead)
		while(q):
			length=len(q):
			for i in range(length):
				tmp=q[0]
				if tmp.left!=None: q.append(tmp.left)
				if tmp.right!=None: q.append(tmp.right)
				output[lvl].append(tmp)
			lvl+=1
			output+=[]

		return output








