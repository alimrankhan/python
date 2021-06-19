#find area of polygon

class point:
	x: float
	y: float
	def __init__(self,a,b):
		self.x= a
		self.y= b
		

def cross_product(a,b):
	return a.x*b.y - a.y*b.x

def area_tri(a,b):
	return abs(.5*cross_product(a,b))
	
def area(list):
	ans=0
	n=len(list)
	for i in range(0,n):
		x=list[i]
		y=list[(i+1)%n]
		ans+= area_tri(x,y)
	return ans

a=point(-2,-1)
b=point(4,-1)
c=point(4,3)
d=point(-2,3)

li=[a,b,c,d]
print('Area of the Polygon is:',end=' ')
print(area(li))
