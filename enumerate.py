#enumerate

li=[1,2,3,4,5]
print('Index||Item')
for index, item in enumerate(li):
	print('{}      {}'.format(index,item))
	
print(list(enumerate(li)))
