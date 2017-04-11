import random
import batalha
import sys
import lifee
cfug=50 #chance de fuga
cata=50 #chance de ataque
gg=0 #1 sem debug 0 com debug
sys.path.append('./data')
import default
import save
insperdex={}
acao=input("Quer apagar o save ou usar ele?(a/u)".lower())
if acao=="wwssadadba":
	acao1=input('<g>ame of life ou <c>continuar')#
	if acao1=='g':
		lifee.LufLuf()
	player=save.player
	player['choice']=7
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
	print("Voce selecionou: \nnome: {0} \npoder: {1} \nvida: {2} \ndefesa: {3}".format(player['inspermon']['7']['name'],player['inspermon']['7']['poder'],player['inspermon']['7']['vida'],player['inspermon']['7']['defesa']))
	
elif acao=='a':
	with open('./data/save.py', 'w') as file:
			file.write(str("player={0}\ninsperdex={1}").format(default.player,insperdex))
	player=default.player
	player['choice']=0
else:
	player=save.player
			
if player['choice']==0:
	while player['choice']!=1 and player['choice']!=2 and player['choice']!=3 and player['choice']!=4 and player['choice']!=5 and player['choice']!=6:
		player['choice']=-1
		acao=input("Escolha seu pokemon inicial:\n1-{0}\n2-{1}\n3-{2}\n4-{3}\n5-{4}".format(player['inspermon']['1']['name'],player['inspermon']['2']['name'],player['inspermon']['3']['name'],player['inspermon']['4']['name'],player['inspermon']['5']['name']))
		player['choice']=int(acao)
	print("Voce selecionou: \nnome: {0} \npoder: {1} \nvida: {2} \ndefesa: {3}".format(player['inspermon'][acao]['name'],player['inspermon'][acao]['poder'],player['inspermon'][acao]['vida'],player['inspermon'][acao]['defesa']))



while True:
	if gg:print("\n"*3)
	if gg:acao=input("Quer passear ou salvar e dormir?(p/d)".lower())
	else:acao='p'
	if acao=='p':
		(x,insperdex,player['inspermon'][str(player['choice'])]['exp'])=batalha.batalha(player['inspermon'][str(player['choice'])],cata,cfug,1,gg)
		print(x)
	elif acao=='d':
		with open('./data/save.py', 'w') as file:
			file.write(str("player={0}\ninsperdex={1}".format(player,insperdex)))
		exit()
	