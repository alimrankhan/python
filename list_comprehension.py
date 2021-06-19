#list comprehension

li= [1,2,3,4,5]
li2= [x for x in li if x%2==0]
li3= [x for x in range(1,6) if x%2!=0]
print(f'{li}')
print("list of even number: {}".format(li2))
print("list of odd number: {}".format(li3))
