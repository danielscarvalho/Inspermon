import random
import sys
sys.path.append('./data')
from default import player
from default import insmon
from default import insperdex

#if !save.player: player=save.player


def insale(x):
	if x>8532 and x<9000: return -1,-1 
	y=random.choice(list(insmon.keys()))
	return insmon[y],y
	
def batalha(seu):
	opt,mon=insale(random.randint(0,10000))
	if mon==-1:return "Voce procurou mas nao encontrou ninguem"
	insperdex[mon]=opt
	vidop,vid=opt['vida'],seu['vida']
	print("\n"*3)
	print("Voce encontrou {0}".format(mon))
	if opt['poder']:print("poder: {0} \nvida: {1} \ndefesa: {2}".format(opt['poder'],opt['vida'],opt['defesa']))
	print("\n"*3)
	print("Tentar fugir?(S/N)")
	while vid>0 and vidop>0:
		vidop-=(seu['poder']-opt['defesa'])
		vid-=(opt['poder']-seu['defesa'])
	if vid<=0 and vidop<=0: return 'Empate'
	elif vid<=0: return 'Voce perdeu'
	elif vidop<=0: return 'Voce ganhou'

while True:
	print("\n"*3)
	acao=input("Quer passear ou salvar e dormir?(P/D)".upper())
	if acao=='P':
		print(batalha(player['insperdex']['pichuchu']))
	elif acao=='D':
		with open('./data/save.py', 'w') as file:
			file.write(str("player={0}\ninsperdex={1}".format(player,insperdex)))
		exit()
	