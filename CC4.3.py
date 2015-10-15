class solution:


	def createminBST(self,a):
		return self.createmintree(a,0,len(a))
	



	def createminBST(self,a,start,end):
		if (end<start):
			return None

		mid=(start+end)/2	
		n=Node(a[mid])

		n.left=self.createmintree(a,start,mid-1)
		n.right=self.createmintree(a,mid+1,end)
		return n




