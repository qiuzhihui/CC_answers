class solution:
	def commonancester(root,a,b):
		if root==None: return -1
		stack=[]

		stack.append(root)
		flag=0

		while(stack):
			tmp=stack.pop()
			if tmp==a:
				ary1=stack
				flag+=1
			if tmp==b:
				ary2=stack
				flag+=1
			if flag==2:
				for i in range(min(len(ary1),len(ary2))):
					if ary1[i]!=ary2[i]:
						return ary[i-1]

			if tmp.left!=None:
				stack.append(tmp.left)
			if tmp.right!=None: 
				stack.append(tmp.right)
		return -1
		