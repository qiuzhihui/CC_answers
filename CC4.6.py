class solution:

	def findnext(self,n):
		if n.parents==None: return None

		#node is the left child
		if n.parents.left==n: return n.parents

		#node is the right child find the right most child from the subtree
		if n.parents.parents==None return None
		root = n.parents.parents
		while(root.left!=None):
			root=root.left
		return root


