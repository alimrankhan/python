#find all the factor of a given number
from math import sqrt
n=int(input('Enter a number to find its Factor: '))

factors=[]
limit= int(sqrt(n))

for i in range(1,limit+1):
    if n%i==0:
        factors.append(i)
        factors.append(int(n/i))
        
if limit*limit==n: factors.pop()
	
print(f'Factors of {n} is: {factors}')
