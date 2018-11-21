import time
import arena
import pickle
import referee
import gametree
import boardpos
import movemaker
import ga2.gaDisc as gad
from gamecontrol import PLANK_DEPTH as pd


class Temp():
    def __init__(self):
        # self.dna = [1, 10**11, 10**3, 10**7, 10**9, -1*10**10, -1, -1*10**11, -1*10**3, -1*10**8, -1*10**9, 10**10]
        self.dna = [1, 10**11, 10**5, 10**7, 0, 0, -1, -1*10**13, -1*10**5, -1*10**8, 0, 0]
        self.fitness = 0


if(__name__=="__main__"):
    # fd = open("BAGENT.dna", 'rb')
    # playerObj1 = pickle.load(fd)
    # fd.close()
    playerObj1 = Temp()
    fd = open("BAGENT.dna", 'wb')
    pickle.dump(playerObj1, fd)
    fd.close()
    gameOver = False
    player = 1
    root = gametree.TreeNode(parent=None, player=player)
    root.makeTree(pd)
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
                # print("Agent {} won with fitness {}".format(playerObj1.agentID, playerObj1.fitness))
                pass
