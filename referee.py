# import time
# import arena
import gametree as gt
# import boardpos
# import movemaker
# import math



# 100 points if a dual case occurs(5+5)
# -25 for each occurence of 3 dots together unnoticed by opponent but missed by the player.
# -1000 if the player facilitates the opponent by not blocking the winning chance.
#  20 if a player blocks the three occurance of other player
# 2 for three consecutive dots
# 1000 for each four consecutive dots(ie the player won)
# 20 points for the player if he blocks the opponent with 3 consecutive dots
# 7 points if the player won with 5 consecutive dots (rare chance)  (optional)

# please add more if u feel like doing so.
# i have used a terminology called dots for the red and green.
#import ga2.gaDisc as gad





# class Boardpos:
#     def __init__(self):
#         self.a = [[0 for i in range(0,7)] for j in range(0,6)]
#class Boardpos:
#	def __init__(self):
#		self.a = [[0 for i in range(0,7)] for j in range(0,6)]


def referee(move, e):
	o = gt.toggle(e)
	move.players = dict()
	move.players[e] = dict()
	move.players[e]['du']=dual(move,e,o)
	move.players[e]['fr']=four(move,e,o)
	move.players[e]['th']=three(move,e,o)
	move.players[e]['fblk']=block(move,o,e)
	move.players[e]['ftb']=block(move,o,0) 

	move.players[o] = dict()
	move.players[o]['du']=dual(move,o,e)
	move.players[o]['fr']=four(move,o,e)
	move.players[o]['th']=three(move,o,e)
	move.players[o]['fblk']=block(move,e,o)
	move.players[o]['ftb']=block(move,e,0)

	fitness=0
	fitness=(-1000*move.players[e]['ftb'])+(1000*move.players[e]['fr'])+(500*move.players[e]['th'])+(100*move.players[e]['du'])+(1000*move.players[e]['fblk']) - ((-1000*move.players[o]['ftb'])+(1000*move.players[o]['fr'])+(500*move.players[o]['th'])+(100*move.players[o]['du'])+(1000*move.players[o]['fblk']))
	# playerObj2.fitness=pow(5,playerObj2.ftb)+pow(-5,playerObj1.ftb)+pow(2,playerObj2.th)+pow(3,playerObj2.tw)
	return fitness

def block(move,e,f):
	count=0
	# move.a=[[0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0],     #just for test pls comment out when doing the original
	# 	[0,0,0,0,1,0,0],
	# 	[0,0,0,1,0,0,0],
	# 	[0,0,1,0,0,0,0],
	# 	[0,0,0,0,0,0,0],
	# 	[0,0,0,0,0,0,0]]
	for i in range(0,6):
		for j in range(0,7):
			if move.a[i][j]== e:
				if (j-1>=0)and(move.a[i][j-1]==e):   #horizontal
						if (j-2>=0)and (move.a[i][j-2]==e):
							if ((j-3>=0)and(move.a[i][j-3]==f)):
								count=count+1
							if ((j+1<7)and(move.a[i][j+1]==f)):
								count=count+1
                                                                
				if (i-1>=0)and(move.a[i-1][j]==e):       #vertical
						if (i-2>=0)and (move.a[i-2][j]==e):
							if ((i-3>=0)and(move.a[i-3][j]==f)): # or(((i+1<6)and(move.a[i+1][j]==f) )):
								count=count+1
					 
				if (i-1>=0)and(j-1>=0)and(move.a[i-1][j-1]==e):  #principle diagonal       above
						if (i-2>=0)and(j-2>=0)and (move.a[i-2][j-2]==e):
							if ((i-3>=0)and(j-3>=0)and(move.a[i-3][j-3]==f)):
								count=count+1
						if ((i+1<6)and(j+1<7)and(move.a[i+1][j+1] == f)):
					 			count=count+1
				'''
				if (i+1<6)and(j+1<7)and(move.a[i+1][j+1]==e):       #principle diagonal below
						if (i+2<6)and(j+2<7)and (move.a[i-2][j-2]==e):
							if ((i+3<6)and(j+3<7)and(move.a[i-3][j-3]==f)) :
								count=count+1	
				'''
				if (i-1>=0)and(j+1<7)and(move.a[i-1][j+1]==e):       #off diagonal above
						if (i-2>=0)and(j+2<7)and (move.a[i-2][j+2]==e):
							if ((i-3>=0)and(j+3<7)and(move.a[i-3][j+3]==f)) :
								count=count+1
							if((i+1<6)and(j-1 >= 0)and(move.a[i+1][j-1] == f)):
								count=count+1
				'''
				if (i+1<6)and(j-1>=0)and(move.a[i+1][j-1]==e):       #off diagonal below
						if (i+2<6)and(j-2>=0)and (move.a[i+2][j-2]==e):
							if ((i+3<6)and(j-3>=0)and(move.a[i+3][j-3]==f)) :
								count=count+1
				'''				
	# print("fail to block")							
	# print(count)
	return (count);


def four(move,e,f):
	count=0
	# move.a=[[0,1,1,1,1,1,1],
	# 	    [2,1,2,1,1,1,1],     #just for test pls comment out when doing the original
	# 	    [0,2,2,1,1,0,1],
	# 		[0,1,0,2,1,0,2],
	# 		[0,1,0,2,2,0,1],
	# 		[0,1,0,2,2,2,1],
	# 		[0,1,2,2,1,0,1]]
	for i in range(0,6):
		for j in range(0,7):
			if move.a[i][j]== e:
				if (j-1>=0)and(move.a[i][j-1]==e):   #horizontal
						if (j-2>=0)and (move.a[i][j-2]==e):
							if ((j-3>=0)and(move.a[i][j-3]==e)) :#or((j+1<7)and(move.a[i][j+1]==e) ):
								count=count+1

				if (i-1>=0)and(move.a[i-1][j]==e):       #vertical
						if (i-2>=0)and (move.a[i-2][j]==e):
							if ((i-3>=0)and(move.a[i-3][j]==e)):#or(((i+1<6)and(move.a[i+1][j]==e) )) :
								#print(i,j)
								count=count+1
					 
				if (i-1>=0)and(j-1>=0)and(move.a[i-1][j-1]==e):  #principle diagonal       above
						if (i-2>=0)and(j-2>=0)and (move.a[i-2][j-2]==e):
							if ((i-3>=0)and(j-3>=0)and(move.a[i-3][j-3]==e)) :
								count=count+1
					 
				if (i+1<6)and(j+1<7)and(move.a[i+1][j+1]==e):       #principle diagonal below
						if (i+2<6)and(j+2<7)and (move.a[i-2][j-2]==e):
							if ((i+3<6)and(j+3<7)and(move.a[i-3][j-3]==e)) :
								count=count+1	

				if (i-1>=0)and(j+1<7)and(move.a[i-1][j+1]==e):       #off diagonal above
						if (i-2>=0)and(j+2<7)and (move.a[i-2][j+2]==e):
							if ((i-3>=0)and(j+3<7)and(move.a[i-3][j+3]==e)) :
								count=count+1
								

				if (i+1<6)and(j-1>=0)and(move.a[i+1][j-1]==e):       #off diagonal below
						if (i+2<6)and(j-2>=0)and (move.a[i+2][j-2]==e):
							if ((i+3<6)and(j-3>=0)and(move.a[i+3][j-3]==e)) :
								count=count+1				
	# print("the no of 4 cases are")
	# print(count)
	return(count)							
def three(move,e,f):
	count=0
	# move.a=[[0,1,1,1,1,1,1],
	# 	    [2,1,2,1,1,1,1],     #just for test pls comment out when doing the original
	# 	    [0,2,2,1,1,0,1],
	# 		[0,1,0,2,1,0,2],
	# 		[0,1,0,2,2,0,1],
	# 		[0,1,0,2,2,2,1]]

#	move.a=[[0,0,2,0,0,0,0],
#		    [0,0,2,0,0,0,0],     #just for test pls comment out when doing the original
#		    [0,0,2,0,0,0,0],
#			[0,0,0,0,2,0,0],
#			[0,0,2,2,2,0,0],
#			[0,0,2,0,2,0,0],
#			[0,0,2,0,0,2,0]]		
	for i in range(0,6):
		for j in range(0,7):
			if (move.a[i][j]==e):
				if (j-1>=0)and(move.a[i][j-1]==e):   #horizontal
							if ((j-2>=0)and(move.a[i][j-2]==e)):# or((j+2<7)and(move.a[i][j+1]==e) ):
								count=count+1
								# print("horizontal")
								# print(i,j)
								
				if (i-1>=0)and(move.a[i-1][j]==e):       #vertical
							if ((i-2>=0)and(move.a[i-2][j]==e)): #or(((i+2<6)and(move.a[i+1][j]==e) )) :
								count=count+1
								# print("vertical")
								# print(i,j)

					 
				if (i-1>=0)and(j-1>=0)and(move.a[i-1][j-1]==e):  #principle diagonal       above
							if ((i-2>=0)and(j-2>=0)and(move.a[i-2][j-2]==e)) :
								count=count+1
								# print("principle diagonal above")
								# print(i,j)
								

					 
				if (i+1<6)and(j+1<7)and(move.a[i+1][j+1]==e):       #principle diagonal below
							if ((i+2<6)and(j+2<7)and(move.a[i-2][j-2]==e)) :
								count=count+1	
								# print("principle diagonal below")
								# print(i,j)
																

				if (i-1>=0)and(j+1<7)and(move.a[i-1][j+1]==e):       #off diagonal above
							if ((i-2>=0)and(j+2<7)and(move.a[i-2][j+2]==e)) :
								count=count+1
								# print("off diagonal above")
								# print(i,j)
								
								


				if (i+1<6)and(j-1>=0)and(move.a[i+1][j-1]==e):       #off diagonal below
							if ((i+2<6)and(j-2>=0)and(move.a[i+2][j-2]==e)) :
								count=count+1
								# print("off diagonal below")
								# print(i,j)
								
								
	# print("the no of 3 cases are")
	# print(count)
	return(count)							

def dual(move,e,f):
	count=0
	# move.a=[[0,0,1,0,0,0,0],
	# 	    [0,0,2,0,0,0,0],     #just for test pls comment out when doing the original
	# 	    [0,0,2,0,0,0,0],
	# 		[2,0,2,2,2,2,2],
	# 		[0,0,2,0,2,0,0],
	# 		[0,0,2,0,2,0,0]]		
	for i in range(0,6):
		for j in range(0,7):
			if move.a[i][j]== e:
				if (j-1>=0)and(move.a[i][j-1]==e):   #horizontal
						if (j-2>=0)and (move.a[i][j-2]==e):
							if ((j-3>=0)and(move.a[i][j-3]==0))and ((j+1<7)and(move.a[i][j+1]==0) ):
								count=count+1
								# print("horizontal")
								# print(i,j)

				if (i-1>=0)and(move.a[i-1][j]==e):       #vertical
						if (i-2>=0)and (move.a[i-2][j]==e):
							if ((i-3>=0)and(move.a[i-3][j]==0))and(((i+1<6)and(move.a[i+1][j]==0) )) :
								count=count+1
								# print("vertical")
								# print(i,j)

					 
				if (i-1>=0)and(j-1>=0)and(move.a[i-1][j-1]==e) and ((i+1<6)and(j+1<7)and((move.a[i+1][j+1]==e) or (move.a[i+1][j+1]==0))):  #principle diagonal       above
						#if (i+2<6)and(j+2<7)and (move.a[i+2][j+2]==e) and ((i-2>=0)and(j-2>=0)and (move.a[i-2][j-2]==0)) :	 # as we are checking the middle elements in the diagonal
							if ((i-2>=0)and(j-2>=0)and(move.a[i-2][j-2]==0)) and ((i+2<6)and(j+2<7)and(move.a[i-2][j-2]==0)) :
								count=count+1
								# print("principle diagonal")
								# print(i,j)

					 
				
				if ((i-1>=0)and(j+1<7)and(move.a[i-1][j+1]==e)) and ((i+1<6)and(j-1>=0)and((move.a[i+1][j-1]==e)or(move.a[i+1][j-1]==0))):       #off diagonal above
						#if ((i-2>=0)and(j+2<7)and (move.a[i-2][j+2]==e)) and ((i+2<6)and(j-2>=0)and ((move.a[i+2][j-2]==e))):	   # as we are checking the middle elements in the diagonal
							if ((i-2>=0)and(j+2<7)and(move.a[i-2][j+2]==0)) and (((i+2<6)and(j-2>=0)and(move.a[i+2][j-2]==0))) :
								count=count+1
								# print("off diagonal")
								# print(i,j)

								
	# print(count)
	return (count);


# c=Boardpos()							
# referee(c,2)
# class Temp():
#         def __init__(self):
#                 pass

# tmp = Temp()
# tmp.a=[[0,0,0,0,0,0,0],     #just for test pls comment out when doing the original
#        [0,0,0,2,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,0,0,0,0]]

# print("blocked ", block(tmp, 1, 2))
