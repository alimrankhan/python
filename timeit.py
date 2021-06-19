#timeit.timeit('operation') #return required time(second)
import timeit

li=[i for i in range (1,100)]

print(sum(li))
print(timeit.timeit('sum(i for i in range(1,100))'))
