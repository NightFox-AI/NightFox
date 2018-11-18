import time
import arena
import pickle
import referee
import gametree
import boardpos
import movemaker
import ga2.gaDisc as gad

PLANK_DEPTH = 5

if(__name__=="__main__"):
    fd = open("BAGENT.dna", 'rb')
    playerObj1 = pickle.load(fd)
    fd.close()
    gameOver = False
    player = 1
    root = gametree.TreeNode(parent=None, player=player)
    root.makeTree(PLANK_DEPTH)
    board = boardpos.Boardpos()
    while(not gameOver):
        oldpos = root.boardpos
        move, root = movemaker.acceptmove(root, player)
        gameOver = arena.change_vals(oldpos, move, player)
        player = gametree.toggle(player)
        
        if(not gameOver):
            oldpos = root.boardpos
            move, root = movemaker.move(playerObj1, root, player)
            gameOver = arena.change_vals(oldpos, move, player)
            player = gametree.toggle(player)
            if(gameOver):
                print("Agent {} won with fitness {}".format(playerObj1.agentID, playerObj1.fitness))
