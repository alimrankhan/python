#map

sqr= lambda n:n*n #lambda function
li=[x for x in range(1,6)]
print(li)
li2=list(map(sqr,li))
print(li2)

