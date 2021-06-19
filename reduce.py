#reduce #reduce(func_name,iterable_obj)
from functools import reduce
fac= lambda a,b:a*b

li = [1,2,3,5]
mul= reduce(fac,li) #1*2*3*5=30
maxi= reduce(lambda a,b:a if a>b else b , li) #passing lambda expression #reduce(max,li)
print('sum of li: {}'.format(mul),end=' and ')
print('maximum element: {}'.format(maxi))
