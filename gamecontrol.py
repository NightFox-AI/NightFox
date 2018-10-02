# This takes insanely large amount of time as this
# this is of the order n^2 and thus all the agents have
# to be updated. Possible solutions can be to parallelse
# these ?. The game playing ?, let us see what we can do
# a lot depends on how good sriniketh's fitness function
# is.

import time
import arena
import referee
import boardpos
import movemaker
import threading
import ga2.gaDisc as gad


if(__name__ == "__main__"):

    # Details on training flags
    NUM_OF_TRAINING_EPOCH = 10


    # Details on the ga2 agents
    NUMBER_OF_AGENTS = 10
    NUMBER_OF_PARAM = 50
    SPREAD = 1
    SURVIVAL_RATE = 0.02
    MUTATION_RATE = 0.03
    GENE_COPY = 0.95
    GEN_MODE = 'A'


    # Initialisation of the modules
    sess = gad.Session(agentCount=NUMBER_OF_AGENTS,
                       numParam=NUMBER_OF_PARAM,
                       spread=SPREAD,
                       genecopy=GENE_COPY,
                       survival=SURVIVAL_RATE,
                       mutation=MUTATION_RATE,
                       generateMode=GEN_MODE)

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
                
                if(player1ID != player2ID):
                    
                    # start the match here
                    player1Obj = sess.getAgent(player1ID)
                    player2Obj = sess.getAgent(player2ID)
                    '''
                    # initialise board
                    board = boardpos.Boardpos()

                    # send the board to movemaker
                    movemaker.board = board
                    movemaker.player1Obj = player1Obj
                    movemaker.player2Obj = player2Obj
                    
                    # let movemaker initialise its players
                    moveMaker1 = movemaker.Player(0)
                    moveMaker2 = movemaker.Player(1)

                    moveMaker1.start()
                    moveMaker2.start()

                    moveMaker1.join()
                    moveMaker2.join()        

                    board = movemaker.board
                    
                    #player1Obj, player2Obj = referee.referee(board)
                    '''
                    sess.updateAgent(player1Obj)
                    sess.updateAgent(player2Obj)
        

        trainEp += 1
        
        print("")
        print("Epoch number {} session {} ****************".format(trainEp, sess.sessID))
        print("Average fitness is      {}".format(sess.getAverageFitness()))
        print("maximum fitness is      {}".format(sess.getBestAgent().fitness))
        print("best agent agentID is   {}".format(sess.getBestAgent().agentID))
        
        sess.createNextGen()
