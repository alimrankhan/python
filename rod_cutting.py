#rod_cutting problem #recursion
import sys
def rod_cut(li,n):
	max_val= -sys.maxsize
	if(n<=0):
		return 0
		
	for i in range(0,n):
		max_val= max(max_val,li[i]+rod_cut(li,n-i-1)) #key_line
	
	return max_val
	
li= [2,5,9,6,7]
print(rod_cut(li,5))

