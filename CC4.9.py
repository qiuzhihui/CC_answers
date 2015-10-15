class solution:

	def gothrougheachnode(self,root,num):

		stack=[]
		stack.append(root)
		path=[]

		while(stack):
			tmp=stack.pop()
			nodepath=findpath(tmp,num)
			path.append(nodepath)

		return path




	def findpath(self,root,num):
		stack=[]
		stack.append(root)
		output=[]

		while(stack):
			tmp=stack.pop()
			if sum(stack)==num:
				output.append(stack)

			if tmp.left!=None: stack.append(tmp.left)
			if tmp.right!=None: stack.append(tmp.right)


