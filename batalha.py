import random
import sys
sys.path.append('./data')
from default import insmon
from default import insperdex
import save
if save.insperdex: insperdex=save.insperdex

def insale(x):
	if x>8532 and x<9000: return -1,-1 
	y=random.choice(list(insmon.keys()))
	return insmon[y],y
	
def batalha(seu,cata,cfug):
	exp=seu['exp']
	opt,mon=insale(random.randint(0,10000))
	if mon==-1:return "Voce procurou mas nao encontrou ninguem",insperdex,exp+0
	insperdex[mon]=opt
	vidop,vid=opt['vida']*seu['exp']/120,seu['vida']*seu['exp']/100
	print("\n"*3)
	print("Voce encontrou {0}".format(mon))
	if opt['poder']:print("poder: {0} \nvida: {1} \ndefesa: {2}".format(opt['poder'],opt['vida'],opt['defesa']))
	print("\n"*3)
	w=input("Tentar fugir?(S/N)".lower())
	if w=='s':
		if(random.randint(0,100)<cfug):
			return 'voce conseguiu fugir',insperdex,exp+1
		else:
			print('voce nao conseguiu fugir')
	print (seu['exp'])
	while vid>0 and vidop>0:
		if(random.randint(0,100)<cata) and ((seu['poder']*seu['exp']/100)-opt['defesa']*seu['exp']/120)>0: 
			vidop-=((seu['poder']*seu['exp']/100)-opt['defesa']*seu['exp']/120)
			print("Voce atacou, vida oponente:{}".format(vid))
		elif (opt['poder']*seu['exp']/120-seu['defesa']*seu['exp']/100)>0: 
			vid-=(opt['poder']*seu['exp']/120-seu['defesa']*seu['exp']/100)
			print("Voce foi atacado, vida:{}".format(vid))
		else: return 'Voce perdeu',insperdex,100
		
		
	if vid<=0 and vidop<=0: return 'Empate',insperdex,exp+0
	if vid<=0: 
		if (exp-opt['exp'])<100:
			return 'Voce perdeu',insperdex,exp-opt['exp']
		else:
			return 'Voce perdeu',insperdex,101
	elif vidop<=0: return 'Voce ganhou',insperdex,exp+opt['exp']