class solution:

	def search(start,end):

		if start==end: return 	
		stack=[]
		stack.push(start)

		while(stack):
			tmp=stack.pop()
			tmp.state='visited'
			for v in tmp.getAdjavent():
				if v.state=='unvisited':
					if v=end: return True
					else: 
						v.state='visiting'
						stack.append(v)
						
		return False







