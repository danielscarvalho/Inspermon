import random
import batalha
import sys
cfug=100 #chance de fuga
cata=50 #chance de ataque
sys.path.append('./data')
from default import player
import save
if save.player: player=save.player


while True:
	print("\n"*3)
	acao=input("Quer passear ou salvar e dormir?(p/d)".lower())
	if acao=='p':
		(x,y)=batalha.batalha(player['inspermon']['pichuchu'],cata,cfug)
		print(x)
	elif acao=='d':
		with open('./data/save.py', 'w') as file:
			file.write(str("player={0}\ninsperdex={1}".format(player,y)))
		exit()
	