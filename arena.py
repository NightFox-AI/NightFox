class Boardposs :
	def __init__(self):
		#self.a=[[0 for i in range(6,-1,-1)] for j in range(5,-1,-1)]
		self.a=[[0 for i in range(0,7)] for j in range(0,6)]
		#self.a[0][1]=1
		for i in range(0,6):
			print(self.a[i])

	def change_vals(self,pos,player):
		global inserted_row
		for i in range(5,-1,-1):
			if(self.a[i][pos]==0):
				self.a[i][pos]=player
				inserted_row = i
				#print("hello",inserted_row)
				break
			elif(self.a[0][pos]==1):
				print("Invalid")
				break

		for i in range(0,6):
			print(self.a[i])
	
		

	def check_for_win(self,pos,player):
		counter=0
		for i in range(pos,-1,-1):	#left
			if(self.a[inserted_row][i]==player):
				counter+=1
			else:
				break
		for i in range(pos+1,7):	#right
			if(self.a[inserted_row][i]==player):
				counter+=1
			else:
				break
		if(counter>=4):
			print("Player ",player," won : LEFT-RIGHT")
			exit(0)

		else:
			counter=0
			for i in range(inserted_row,6):	#down
				if(self.a[i][pos]==player):
					counter+=1
				else:
					break

			if(counter>=4):
				print("Player ",player," won : UP-DOWN")
				exit(0)


			else:
				counter=0
				#print("Pos ",pos," Row ",inserted_row)
				pos_diag=pos
				for i in range(inserted_row,-1,-1):	#45-degree diagonal right
					if(self.a[i][pos_diag]==player):
						pos_diag+=1
						counter+=1
						#print("hi")
						#print(counter)
					else:
						break
				#print("counter after 1st for loop",counter)
				pos_diag=pos-1
				for i in range(inserted_row+1,6):	#45-degree diagonal left
					#print("row ",i," column ",pos_diag)
					if(self.a[i][pos_diag]==player and pos_diag>0):
						pos_diag-=1
						counter+=1
						#print(counter)
					else:
						break
				if(counter>=4):
					print("Player ",player," won : NEG_DIAG")
					exit(0)


				else:
					counter=0
					#print("Pos ",pos," Row ",inserted_row)
					pos_diag=pos
					for i in range(inserted_row,-1,-1):	#135-degree diagonal left
						if(self.a[i][pos_diag]==player):
							pos_diag-=1
							counter+=1
							#print("hi")
							#print(counter)
						else:
							break
					#print("counter after 1st for loop",counter)
					pos_diag=pos+1
					for i in range(inserted_row+1,6):	#135-degree diagonal right
						#print("row ",i," column ",pos_diag)
						if(self.a[i][pos_diag]==player and pos_diag>0):
							pos_diag+=1
							counter+=1
							#print(counter)
						else:
							break
					if(counter>=4):
						print("Player ",player," won : NEG_DIAG")
						exit(0)



if(__name__=="__main__"):
	op=Boardposs()
	while(1):
		print("Player 	Position")
		player, pos = input().split(" ")
		player = int(player)
		pos = int(pos)
		ip=op.change_vals(pos,player)
		op.check_for_win(pos,player)

