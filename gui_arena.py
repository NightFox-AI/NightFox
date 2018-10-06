class Boardposs :
	
	def __init__(self,player1 = 'X', player2 = 'O'):
		self.size = {'c' : 7, 'r': 6} # 7 columns x 6 rows
		self.grid = []
		self.first_player = True # True - player 1 on the move, False - player 2 on the move
		self.players = {True : player1, False : player2} # Anything except ? (question mark) AND 1 character only!
		self.game_over = False
		self.grid = [[] for i in range(self.size['c'])]
		self.pos=None
		self.player=None
		self.inserted_row=None
		self.a=None
	# Returns True if disc was successfully dropped, False otherwise
	def drop(self, column): # Drop a disc into a column
		if self.game_over: return False # Cannot proceed because game has already ended.

		if column < 0 or column >= self.size['c']:
		    return False
		if len(self.grid[column]) >= self.size['r']:
		    return False
		self.pos=column
		
		self.grid[column].append(self.players[self.first_player])
		#print("column lenhth :",len(self.grid[column]))
		self.inserted_row=len(self.grid[column])-1
		#print(column)
		#print(self.inserted_row)
		#print("inserted_row in drop = ",self.inserted_row)
		c = self.check()
		if c == False:
		    self.first_player = not self.first_player
		    return True
		else:
		    self.game_over = c
		    return True


	"""
	def change_vals(self,pos,player):
		global inserted_row
		for i in range(5,-1,-1):
			if(self.a[i][self.pos]==0):
				self.a[i][self.pos]=player
				inserted_row = i
				#print("hello",inserted_row)
				break
			elif(self.a[0][self.pos]==1):
				print("Invalid")
				break

		for i in range(0,6):
			print(self.a[i])
	"""		
		

	def check(self):
	
		#print((self.grid))
		
		#up
		self.a=[[0 for i in range(0,7)] for j in range(0,6)]
		pl_var=self.players[self.first_player]
		if(pl_var=='X'):
			self.player=1
		elif(pl_var=='O'):
			self.player=2		
			#horizontal

		for i,column in enumerate(self.grid):
			#print(i,len(j))
			#i=6-i
			#Down
			#if(len(column)==4):
			#	return True
			
			#j is each column
			k=0
			for j in column:
				if(j=='X'):
					self.a[k][i]=1
					#self.player=1
				elif(j=='O'):
					self.a[k][i]=2
					#self.player=2
				k+=1
				
			#horizontal
		#print(self.a)
		#print(self.a)
		for i in range(5,-1,-1):
			print(self.a[i])

		#print("row 0",self.a[self.inserted_row])
			#diagpnal1

			#diagonal2

		#print("Player",self.player)
		#use set() to check
		#self.inserted_row-=1
		
		counter=0
		#print("inserted_row in check",self.inserted_row)
		for i in range(self.pos,-1,-1):	#left
			#print("a[-1][0]",self.a[-1][0])
			#print("value","player","pos",self.a[self.inserted_row][i],self.player,self.pos)
			if(self.a[self.inserted_row][i]==self.player):
				counter+=1
			else:
				break
		for i in range(self.pos+1,7):	#right
			#print(self.a[self.inserted_row][i],self.player)
			if(self.a[self.inserted_row][i]==self.player):
				counter+=1
			else:
				break
		#print("hori counter:",counter)
		if(counter>=4):
			print("Player ",self.player," won : LEFT-RIGHT")
			#exit(0)
			return True

		#else:
		counter=0
		for i in range(self.inserted_row,6):	#up
			if(self.a[i][self.pos]==self.player):
				counter+=1
			else:
				break
		for i in range(self.inserted_row-1,-1,-1):	#down
			if(self.a[i][self.pos]==self.player):
				counter+=1
			else:
				break
		#print("verti counter:",counter)
		if(counter>=4):
			print("Player ",self.player," won : UP-DOWN")
			#exit(0)
			return True

		else:
			counter=0
			#print("Pos ",pos," Row ",inserted_row)
			pos_diag=self.pos
			for i in range(self.inserted_row,-1,-1):	#45-degree diagonal right
				if(pos_diag<7 and self.a[i][pos_diag]==self.player):
					pos_diag+=1
					counter+=1
					#print("hi")
					#print("45 deg",counter)
				else:
					break
			#print("counter after 1st for loop",counter)
			pos_diag=self.pos-1
			for i in range(self.inserted_row+1,6):	#45-degree diagonal left
				#print("row ",i," column ",pos_diag)

				#print("pos_diag","player",self.a[i][pos_diag],self.player)
				if(pos_diag>=0 and self.a[i][pos_diag]==self.player ):
					pos_diag-=1
					counter+=1
					#print("45 deg",counter)
				else:
					break
			
			if(counter>=4):
				print("Player ",self.player," won : NEG_DIAG")
				#exit(0)
				
				return True

				#else:
			counter=0
			#print("Pos ",pos," Row ",inserted_row)
			pos_diag=self.pos
			for i in range(self.inserted_row,-1,-1):	#135-degree diagonal left
				if( pos_diag>=0 and self.a[i][pos_diag]==self.player):
					pos_diag-=1
					counter+=1
					#print("hi")
					#print("135",counter)
				else:
					break
			#print("counter after 1st for loop",counter)
			pos_diag=self.pos+1
			for i in range(self.inserted_row+1,6):	#135-degree diagonal right
				#print("row ",i," column ",pos_diag)
				if(pos_diag<7 and  self.a[i][pos_diag]==self.player ):
					pos_diag+=1
					counter+=1
					#print("135",counter)
				else:
					break
			#print("135 deg",counter)
			if(counter>=4):
				print("Player ",self.player," won : NEG_DIAG")
				#exit(0)
				
				return True
		return False
		
	


"""
op=Boardposs()
while(1):
	print("Player 	Position")
	player, pos = input().split(" ")
	player = int(player)
	pos = int(self.pos)
	ip=op.change_vals(self.pos,player)
	op.check_for_win(self.pos,player)
"""


#135 diag not working in middle