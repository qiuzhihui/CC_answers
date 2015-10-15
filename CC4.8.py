class solution:

	def containssubtree(self,a,b):

		stack=[]
		stack.append(a)

		while(stack):
			tmp=stack[0]
			stack.remove(0)
			if tmp==b:
				return sametree(tmp,b)
			if tmp.left!=None: stack.append(tmp.left)
			if tmp.right!=None: stack.append(tmp.right)

		return False


	def sametree(self,a,b):

		if a!=b: return False
		if a==None and b==None return True
		return self.sametree(a.left,b.left) and self.sametree(a.right,b.right)
