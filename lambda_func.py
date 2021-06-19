fun = lambda a,b,c : a+b+c #lambdafun

try:
	a=int(input('Enter a INteger: '))
	b=int(input('Enter a INteger: '))
	c=int(input('Enter a INteger: '))
	print(fun(a,b,c))
	
except Exception as e:
	print(e)
except ValueError:
	print('wrong input!')

	
print('end')
