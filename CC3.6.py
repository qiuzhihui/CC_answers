

def stack_sort(stack):

	helper=[]

	while(stack):
		tmp=stack.pop()
		while(len(helper)!=0 and helper[-1]>tmp):
			stack.append(helper.pop())
		helper.append(tmp)


	return helper

	    	

print stack_sort([5,4,3,2,1])