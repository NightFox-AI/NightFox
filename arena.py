def change_vals(bObj,pos,player):
	global inserted_row
	for i in range(5,-1,-1):
		if(bObj.a[i][pos]==0):
			bObj.a[i][pos]=player
			inserted_row = i
			#print("hello",inserted_row)
			break
		elif(bObj.a[0][pos]==1):
			print("Invalid")
			break
	print("\nThe format is ")
	print(" 0  1  2  3  4  5  6")
	for i in range(0,6):
		print(bObj.a[i])

	

def check_for_win(bObj,pos,player):
	counter=0
	for i in range(pos,-1,-1):	#left
		if(bObj.a[inserted_row][i]==player):
			counter+=1
		else:
			break
	for i in range(pos+1,7):	#right
		if(bObj.a[inserted_row][i]==player):
			counter+=1
		else:
			break
	if(counter>=4):
		print("Player ",player," won : LEFT-RIGHT")
		exit(0)

	else:
		counter=0
		for i in range(inserted_row,6):	#down
			if(bObj.a[i][pos]==player):
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
				if(pos_diag<7 and bObj.a[i][pos_diag]==player):
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
				if(pos_diag>=0  and bObj.a[i][pos_diag]==player):
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
					if(pos_diag>=0 and bObj.a[i][pos_diag]==player):
						pos_diag-=1
						counter+=1
						#print("hi")
						#print(counter)
						#print("l",counter)
					else:
						break
				#print("counter after 1st for loop",counter)
				pos_diag=pos+1
				for i in range(inserted_row+1,6):	#135-degree diagonal right
					#print("row ",i," column ",pos_diag)
					#print(pos_diag)
					if(pos_diag<7 and bObj.a[i][pos_diag]==player ):
						pos_diag+=1
						counter+=1
						#print("r , pos",counter,pos_diag)
					else:
						break
				if(counter>=4):
					print("Player ",player," won : NEG_DIAG")
					exit(0)



if(__name__=="__main__"):
	import Boardpos
	bObj = Boardpos.Boardpos()
	while(1):
		print("Player 	Position")
		player, pos = input().split(" ")
		player = int(player)
		pos = int(pos)
		ip=change_vals(bObj,pos,player)
		check_for_win(bObj,pos,player)