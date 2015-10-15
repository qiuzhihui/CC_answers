
class solution:

	def ifbalanced(self,root):
		if root==None: return True
		if abs(self.height(root.left)-self.height(root.right))>1: return False
		return self.ifbalanced(root.left) and self.ifbalanced(root.right)



	def height(self,root):
		if root==None: return 0
		return max(self.height(root.left),self.height(root.right))+1

