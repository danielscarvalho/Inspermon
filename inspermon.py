import random
import sys
sys.path.append('./data')
import save
import default

#if !save.player: player=save.player
player={
	'insperdex': {
		'pichuchu':{
			'poder':30,
			'vida':40,
			'defesa':15,
		}
	}
}

insmon={
	'bubaluba':{
		'poder':20,
		'vida':40,
		'defesa':15,
	},
	'babybef':{
		'poder':20,
		'vida':40,
		'defesa':15,
	},
	'bilabila':{
		'poder':20,
		'vida':40,
		'defesa':15,
	},
	'bronibru':{
		'poder':20,
		'vida':40,
		'defesa':15,
	},
	'orange':{
		'poder':100000,
		'vida':1000000,
		'defesa':100000,
	},
}

def insale(x):
	if x>8532 and x<900: return 'ninguem e voce cansou, tente novamente' 
	y=random.choice(list(insmon.keys()))
	return insmon[y],y
	
def batalha(seu):
	opt,mon=insale(random.randint(0,10000))
	print("\n"*3)
	print("Voce encontrou {0}".format(mon))
	if opt['poder']:print("poder: {0} \nvida: {1} \ndefesa: {2}".format(opt['poder'],opt['vida'],opt['defesa']))
	print("\n"*3)
	print("Tentar fugir?(S/N)")
	while seu['vida']>0 and opt['vida']>0:
		opt['vida']-=(seu['poder']-opt['defesa'])
		seu['vida']-=(opt['poder']-seu['defesa'])
	if seu['vida']<=0: return 'Voce perdeu'
	elif opt['vida']<=0: return 'Voce ganhou'

while True:
	acao=input("Quer passear ou salvar e dormir?(P/D)".upper())
	if acao=='P':
		print(batalha(player['insperdex']['pichuchu']))
	elif acao=='D':
		#print(save.player1[insperdex])
		with open('save.py', 'w') as file:
			file.write(str("player={}".format(player)))
		exit()
	