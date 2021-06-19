#args
def argss(*test): #any name(test) will work 
	print(f'Name: {test[0]} \nAge: {test[1]}')
	for i in test:
		print(i)
	
li=['khan',22]  #tuple,set also work
argss('Imran',33)
argss(*li)

#kwargs
def kwargss(**test):
	for key,value in test.items():  # i->key # j->value
		print(key, value)

dic={'name':'al imran khan','age':23}
kwargss(**dic)
