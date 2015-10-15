class solution:
	def checkifBST(self,root):
		if root==None: return True

		#how to deal with equal case
		if root.left!=None and root.left>root: return False
		if root.right!=None and root.right<root: return True

		return self.checkifBST(root.left) and self.checkifBST(root.right)


