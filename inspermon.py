import random
import batalha
import sys
cfug=100 #chance de fuga
cata=50 #chance de ataque
sys.path.append('./data')
from default import player
import save
if save.player: player=save.player
acao=input("Quer apagar o save ou usar ele?(a/u)".lower())
if acao=="wwssadadba":
	player[choice]=5
	print('''
		_______
	    .adOOOOOOOOOba.
	   dOOOOOOOOOOOOOOOb
	  dOOOOOOOOOOOOOOOOOb
	 dOOOOOOOOOOOOOOOOOOOb
	|OOOOOOOOOOOOOOOOOOOOO|
	OP'~"YOOOOOOOOOOOP"~`YO
	OO     `YOOOOOP'     OO
	OOb      `OOO'      dOO
	YOOo      OOO      oOOP
	`OOOo     OOO     oOOO'
	 `OOOb._,dOOOb._,dOOO'
	  `OOOOOOOOOOOOOOOOO'
	   OOOOOOOOOOOOOOOOO
	   YOOOOOOOOOOOOOOOP
	   `OOOOOOOOOOOOOOO'
	   `OOOOOOOOOOOOO'
	    `OOOOOOOOOOO'
	     `~OOOOO~'   UNLOCKED
	''')
	
elif acao=='a':
	with open('./data/save.py', 'w') as file:
			file.write(str("player={'choice':0}\ninsperdex={}"))
			
if player[choice]==0:
	player
	acao=input("Escolha seu pokemon inicial:\n1-{0}\n1-{1}\n1-{2}".format(player['inspermon']['1']['name'],player['inspermon']['2']['name'],player['inspermon']['3']['name'])



while True:
	print("\n"*3)
	acao=input("Quer passear ou salvar e dormir?(p/d)".lower())
	if acao=='p':
		(x,insperdex,player['inspermon'][str(player['choice'])]['exp'])=batalha.batalha(player['inspermon'][str(player['choice'])],cata,cfug)
		print(x)
	elif acao=='d':
		with open('./data/save.py', 'w') as file:
			file.write(str("player={0}\ninsperdex={1}".format(player,y)))
		exit()
	