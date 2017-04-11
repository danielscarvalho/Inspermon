def LufLuf():
	print('''
	Bem Vindo ao jogo da Vida
	https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
	divirta-se observando :>
	ainda tem alguns erros mas foi o que deu pra fazer
	''')
	x,y=0,0
	import random
	import time
	grid=int(input("Qual o tamanho da matriz do jogo?"))
	temp=int(input("Deseja quantos FPS?(5 ideal)"))
	mapa=[]
	amapa=[]



	while x<grid:
		mapa.append([])
		y=0
		while y<grid:
			mapa[x].append('.')
			y+=1
		y=0
		x+=1
			
	x=0


	while x<grid/1.5:
		cellInx=random.randint(2,grid-2)
		cellIny=random.randint(2,grid-2)
		mapa[cellInx][cellIny]='█'
		viz=random.randint(0,6)
		y=0
		while y<viz:
			mapa[cellInx+int(random.uniform(-2, 2))][cellIny+int(random.uniform(-2, 2))]='█'
			y+=1
		x+=1
	y,x=0,0

	def MostraMap(x=0,y=0):
		print ("\n"*30)
		while x<grid:
			while y<grid:
				print(mapa[x][y]," ",end="")
				y+=1
			y=0
			print("")
			x+=1
		return 0
	#def MostraMapGUI(mapa,grid):
		#mapp=makeLevel("vida",grid,grid)
			
	MostraMap()

	x,y,viz=0,0,0
	amapa=mapa
	acao=input('´crtl+C´ para parar o jogo, qualquer botao para iniciar')
	while acao!='c':
		while x<grid:
			while y<grid:
				if y<grid-1: 
					if amapa[x][y+1]=='█': viz+=1
				if y>0: 
					if amapa[x][y-1]=='█': viz+=1
				if x<grid-1: 
					if amapa[x+1][y]=='█': viz+=1
				if x>0: 
					if amapa[x-1][y]=='█': viz+=1
				if y<grid-1 and x<grid-1: 
					if amapa[x+1][y+1]=='█': viz+=1
				if x<grid-1 and y>0: 
					if amapa[x+1][y-1]=='█': viz+=1
				if y>0 and x>0: 
					if amapa[x-1][y-1]=='█': viz+=1
				if x>0 and y<grid-1: 
					if amapa[x-1][y+1]=='█': viz+=1
				#if viz>0:
					#print('x=',x,'y=',y,'viz=',viz)
				if viz<2 and mapa[x][y]=='█': mapa[x][y]='.'
				if viz>3 and mapa[x][y]=='█': mapa[x][y]='.'
				if viz==3 and mapa[x][y]=='.': mapa[x][y]='█'
				
				
				viz=0
				y+=1
			y,viz=0,0
			x+=1
		x,y,viz=0,0,0
		MostraMap()
		time.sleep(1/temp)
		#if amapa==mapa: print ('Erro, por favor reinicie')
		amapa=mapa
	return 0