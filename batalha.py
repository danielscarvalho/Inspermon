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
	opt,mon=insale(random.randint(0,10000))
	if mon==-1:return "Voce procurou mas nao encontrou ninguem",insperdex
	insperdex[mon]=opt
	vidop,vid=opt['vida'],seu['vida']
	print("\n"*3)
	print("Voce encontrou {0}".format(mon))
	if opt['poder']:print("poder: {0} \nvida: {1} \ndefesa: {2}".format(opt['poder'],opt['vida'],opt['defesa']))
	print("\n"*3)
	w=input("Tentar fugir?(S/N)".lower())
	if w=='s':
		if(random.randint(0,100)<cfug):
			return 'voce conseguiu fugir'
		else:
			print('voce nao conseguiu fugir')
	while vid>0 and vidop>0:
		if(random.randint(0,100)<cata): vidop-=(seu['poder']-opt['defesa'])
		else: vid-=(opt['poder']-seu['defesa'])
		
	if vid<=0 and vidop<=0: return 'Empate',insperdex
	elif vid<=0: return 'Voce perdeu',insperdex
	elif vidop<=0: return 'Voce ganhou',insperdex