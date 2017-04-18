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
	
def batalha(seu,cata,cfug,bb,gg):
	exp=seu['exp']
	opt,mon=insale(random.randint(0,10000))
	if mon==-1:return "Voce procurou mas nao encontrou ninguem",insperdex,exp+0
	insperdex[mon]=opt
	vidop,vid=opt['vida'],seu['vida']
	if gg:print("\n"*3)
	if gg:print("Voce encontrou {0}".format(mon))
	if opt['poder'] and gg:print("poder: {0} \nvida: {1} \ndefesa: {2}".format(opt['poder'],opt['vida'],opt['defesa']))
	if gg:print("\n"*3)
	if gg:w=input("Tentar fugir?(S/N)".lower())
	else:w='n'
	if w=='s':
		if(random.randint(0,100)<cfug):
			return 'voce conseguiu fugir',insperdex,exp+1
		else:
			print('voce nao conseguiu fugir')
	while vid>0 and vidop>0:
		if bb==0:
			if(random.randint(0,100)<cata) and ((seu['poder'])-opt['defesa'])>0:
				vidop-=((seu['poder'])-opt['defesa'])
				#print("Voce atacou, vida oponente:{}".format(vidop))
			elif (opt['poder']-seu['defesa'])>0: 
				vid-=(opt['poder']-seu['defesa'])
				#print("Voce foi atacado, vida:{}".format(vid))
			else: return 'Voce perdeu',insperdex,100
		else:
			if(random.randint(0,100)<cata):
				vidop-=(seu['poder']/opt['defesa'])*1
				#print("Voce atacou, vida oponente:{}".format(vidop))
			else:
				vid-=(opt['poder']/seu['defesa'])*1
				#print("Voce foi atacado, vida:{}".format(vid))
		
		
	if vid<=0 and vidop<=0: return 'Empate',insperdex,exp+0
	if vid<=0: 
		if (exp-opt['exp'])<100:
			return 'Voce perdeu',insperdex,exp-opt['exp']
		else:
			return 'Voce perdeu',insperdex,101
	elif vidop<=0: return 'Voce ganhou',insperdex,exp+opt['exp']