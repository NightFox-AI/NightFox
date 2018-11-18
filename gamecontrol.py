import time
import arena
import pickle
import referee
import gametree
import boardpos
import movemaker
import ga2.gaDisc as gad

import random


NUM_OF_TRAINING_EPOCH = 10
NUMBER_OF_AGENTS = 5
NUMBER_OF_PARAM = 10
SPREAD = 1
SURVIVAL_RATE = 0.4
MUTATION_RATE = 0.1
GENE_COPY = 0.90
GEN_MODE = 'A'
MODE = 'UNSAFE'
VAL_TYPE = 'FLOAT'

PLANK_DEPTH = 4

if(__name__=="__main__"):
    sess = gad.Session(agentCount=NUMBER_OF_AGENTS,
                       numParam=NUMBER_OF_PARAM,
                       spread=SPREAD,
                       genecopy=GENE_COPY,
                       survival=SURVIVAL_RATE,
                       mutation=MUTATION_RATE,
                       generateMode=GEN_MODE,
                       mode=MODE,
                       valType=VAL_TYPE)
    
    sess.init()
    
    trainEp = 0
    gameID = 0
    while(trainEp < NUM_OF_TRAINING_EPOCH):
        
        currGen = sess.getAllAgents()
        for player in currGen:
            agent = sess.getAgent(player)
            agent.fitness = 0
            sess.updateAgent(agent)
        for player1ID in currGen:
            for player2ID in currGen:

                playerObj1 = sess.getAgent(player1ID)
                playerObj2 = sess.getAgent(player2ID)
                
                if(player1ID != player2ID):
                    print("GAME {}".format(gameID))
                    gameOver = False
                    player = 1
                    root = gametree.TreeNode(parent=None, player=player)
                    root.makeTree(PLANK_DEPTH)
                    board = boardpos.Boardpos()
                    while(not gameOver):
                        oldpos = root.boardpos
                        move, root = movemaker.move(playerObj1, root, player)
                        gameOver = arena.change_vals(oldpos, move, player)
                        playerObj1.fitness += referee.referee(root.boardpos,  player)
                        
                        player = gametree.toggle(player)
                        
                        if(not gameOver):
                            oldpos = root.boardpos
                            move, root = movemaker.move(playerObj2, root, player)
                            gameOver = arena.change_vals(oldpos, move, player)
                            playerObj2.fitness += referee.referee(root.boardpos,  player)
                            if(gameOver):
                                print("Agent {} won with fitness {}".format(playerObj2.agentID, playerObj2.fitness))
                                print("Agent {} fitness {}".format(playerObj1.agentID, playerObj1.fitness))
                            player = gametree.toggle(player)
                            
                        else:
                            print("Agent {} won with fitness {}".format(playerObj1.agentID, playerObj1.fitness))
                            print("Agent {} fitness {}".format(playerObj2.agentID, playerObj2.fitness))
                            
                    sess.updateAgent(playerObj1)
                    sess.updateAgent(playerObj2)
                    gameID += 1
                    
        trainEp += 1
        
        print("")
        print("Epoch number {} session {} ****************".format(trainEp, sess.sessID))
        print("Average fitness is      {}".format(sess.getAverageFitness()))
        print("maximum fitness is      {}".format(sess.getBestAgent().fitness))
        print("best agent agentID is   {}".format(sess.getBestAgent().agentID))
        sess.createNextGen()
        
    print("The best agent Dna is {}".format(sess.getBestAgent().dna))
    fd = open("BAGENT.dna", 'wb')
    pickle.dump(sess.getBestAgent(), fd)
    fd.close()
