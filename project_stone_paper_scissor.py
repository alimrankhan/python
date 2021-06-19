#project #stone_paper_scissor #python
import random

def gameplay():
	dic={ 1:'Stone', 2:'Paper', 3:'Scissor'}
	print('\n\nYour play')
	for i in dic:
		print(i,' ',dic[i])
	op= int(input())
	print('You choose: ',dic[op])
	keys=list(dic.keys())
	bot= random.choice(keys)
	print('Bot choose: ',dic[bot],end='\n')  
	print('The winner is: ',result(op,bot))
	print('Do you want to play again?')       
	print('1: Yes')
	print('0: No, quit')
	t=int(input())
	if t==0:
		pass
	elif t==1:
		gameplay()
	else:
		print('Wrong Input')
		
def result(user,bot):
	if user==bot:
		return 'Draw'
	elif (user==1 and bot==2 or user==2 and bot==3 or user==3 and bot==1):
		return 'Bot'
	else:
		return 'User'
def start():
	print('WELCOME TO --STONE-PAPER-SCISSOR-- GAME',end='\n\n')
	print('1: Start')
	print('0: Exit')
	op= int(input())
	if op==1:
		gameplay()

if __name__=='__main__':
	start()
