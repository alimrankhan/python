#prime factors of a given number
from math import sqrt
n=int(input('Input a number : '))
prime_factors=[]
limit=int(sqrt(n))
print(limit)

for i in range(2,limit+1):
	while(n%i==0):
		prime_factors.append(i)
		n/=i
if n!=1:
		prime_factors.append(int(n))
print(prime_factors)
