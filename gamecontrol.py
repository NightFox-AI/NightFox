# This takes insanely large amount of time as this
# this is of the order n^2 and thus all the agents have
# to be updated. Possible solutions can be to parallelse
# these ?. The game playing ?, let us see what we can do
# a lot depends on how good sriniketh's fitness function
# is.

import time
import arena
import referee
import gametree
import boardpos
import movemaker
import ga2.gaDisc as gad

import random

if(__name__ == "__main__"):

    # Details on training flags
    NUM_OF_TRAINING_EPOCH = 100


    # Details on the ga2 agents
    NUMBER_OF_AGENTS = 10
    NUMBER_OF_PARAM = 50
    SPREAD = 1
    SURVIVAL_RATE = 0.02
    MUTATION_RATE = 0.03
    GENE_COPY = 0.95
    GEN_MODE = 'A'
    MODE = 'UNSAFE'
    VAL_TYPE = 'FLOAT'

    # Initialisation of the modules
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
    
    # start training
    trainEp = 0
    while(trainEp < NUM_OF_TRAINING_EPOCH):

        # One set of tournament starts
        # each agent plays with another agent in
        # the current generation twice.
        # total number of plays per tournament
        # is numOfAgents^2. (phew this will take long)

        currGen = sess.getAllAgents()
        for player1ID in currGen:
            for player2ID in currGen:

                playerObj1 = sess.getAgent(player1ID)
                playerObj2 = sess.getAgent(player2ID)
                
                if(player1ID != player2ID):

                    gameOver = False
                    root = gametree.TreeNode(parent=None)
                    board = boardpos.Boardpos()
                    player = 1
                    while(not gameOver):
                        move = movemaker.move(playerObj1, root)
                        gameOver = arena.change_vals(board, move, player)
                        playerObj1.fitness = referee.referee(board,  player)

                        player = gametree.toggle(player)
                        
                        if(not gameOver):
                            move = movemaker.move(playerObj2, root)
                            gameOver = arena.change_vals(board, move, player)
                            playerObj2.fitness = referee.referee(board,  player)

                            player = gametree.toggle(player)
                            
                    sess.updateAgent(playerObj1)
                    sess.updateAgent(playerObj2)
                    
            
        trainEp += 1
        
        print("")
        print("Epoch number {} session {} ****************".format(trainEp, sess.sessID))
        print("Average fitness is      {}".format(sess.getAverageFitness()))
        print("maximum fitness is      {}".format(sess.getBestAgent().fitness))
        print("best agent agentID is   {}".format(sess.getBestAgent().agentID))
        
        sess.createNextGen()
