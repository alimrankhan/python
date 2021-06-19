#gcd #euclid

def gcd(a,b):
	while(a%b!=0):
		temp= a%b
		a=b
		b= temp
	return b

if __name__ == '__main__' :
	print(gcd(12,18))
	
	
