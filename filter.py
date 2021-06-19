#filter

li=[1,2,3,4,5] #tuple() and set{} also work [iterable]

def func(n):
	if n%2==0:
		return True
	else:
		return False
	
ans= filter(func , li)
print('{}\nOdd list: '.format(li),list(ans)) #also can use tuple,set etc.

