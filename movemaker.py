import numpy as np
import random
import gametree
import referee
from gamecontrol import PLANK_DEPTH as pd
import arena
import time

# print("pd is {}".format(pd))
INF = 10**25

def move(playerObj1, root, player):
    if(any([i is not None for i in root.children])):

        if(1):
            think = 4
            start = time.time()
            pld = 1
            while(time.time()-start < think):
                # if(1):
                # print("At depth {}".format(pld))
                worthc = []
                # print("PLD is ", pd)
                for pos, child in enumerate(root.children):
                    if(child is not None):
                        # print("child is ", child)
                        worthc.append(minimax(child, pld-1, -INF, INF, gametree.toggle(player), player, playerObj1, pos))
                    else:
                        worthc.append(-INF)
                maxv = max(worthc)
                finc = [chld for chld in range(len(worthc)) if worthc[chld]==maxv]
                val = random.choice(finc)
                if(root.children[val] is None):
                    print("WARNING !!!")
                    val = 0
                    while(root.children[val] is None):
                        val += 1
                if(pld == pd):
                    break
                pld += 1
            # print("values are {}".format(worthc))
        else:
            pass
            # worthc = []
            # for pos, child in enumerate(root.children):
            #     worthc.append(minimax(child, pd, -INF, INF, gametree.toggle(player), player, playerObj1, pos))
            
            # # print("worthc is {}".format(worthc))
            # maxv = max(worthc)
            # finc = [chld for chld in range(len(worthc)) if worthc[chld]==maxv]
            # # print("finc is ", finc)
            # val = random.choice(finc)
            # # val = random.randint(0, len(root.children)-1)            
            # if(root.children[val] is None):
            #     print("WARNING !!!")
            #     val = 0
            #     while(root.children[val] is None):
            #         val += 1

        root = root.children[val]
        root = addPlank(root)
        return(val, root)
    else:
        return(0, root)


def evaluation(playerObj, root, player):
    
    # print("from eval ")
    # print("for player ", player)
    # print("arr is ", list(root.boardpos.players[player]) + list(root.boardpos.players[gametree.toggle(player)]))
    # print(" 0  1  2  3  4  5  6")
    # for i in range(0,6):
    #     print(root.boardpos.a[i])
    
    mixer = np.array(playerObj.dna).reshape(1, 12)
    res = np.ndarray.tolist((np.dot(mixer, np.array(list(root.boardpos.players[player]) + list(root.boardpos.players[gametree.toggle(player)])))))
    # print("RES IS {}".format(res))
    # res = referee.referee(root.boardpos, player)
    # print("The last vec is ", list(root.boardpos.players[player].values()))
    # print("boardpos.players[player] ", root.boardpos.players[player])
    # print("boardpos.players[toggle-player] ", root.boardpos.players[gametree.toggle(player)])
    return(res[0])
        

def minimax(position, depth, alpha, beta, player, maxp, playerObj1, pos):
    # if(position is None):
    #     return(0)
    
    res = arena.check_for_win(position.boardpos, pos,player)
    if(not res):
        res = arena.check_for_win(position.boardpos, pos, gametree.toggle(player))
    if(res or (position.leaf) or (position.endPos) or (depth == 0)):
        if(maxp != player):
            return(-(10**(depth))*evaluation(playerObj1, position, player))
        return((10**depth)*evaluation(playerObj1, position, player))
    
    if(maxp == player):
        maxeval = -INF
        for pos,child in enumerate(position.children):
            if(child is not None):
                el = minimax(child, depth-1, alpha, beta, gametree.toggle(player), maxp, playerObj1, pos)
                maxeval = max(maxeval, el)
                alpha = max(alpha, el)
                if(beta <= alpha):
                    break
        return(maxeval)
    
    else:
        mineval = INF
        for pos, child in enumerate(position.children):
            if(child is not None):
                el = minimax(child, depth-1, alpha, beta, gametree.toggle(player), maxp, playerObj1, pos)
                mineval = min(mineval, el)
                beta = min(beta, el)
                if(beta <= alpha):
                    break
        return(mineval)

    
def addPlank(root):
    if((root is None)):
        pass

    elif((root.leaf) and (not root.endPos)):
        root.generateChildren()
    else:
        # print("Added {} children ".format(len(root.children)))
        for child in range(len(root.children)):
            root.children[child] = addPlank(root.children[child])
    return(root)

def normalize(val):
    return(1/(1+val))

def acceptmove(root, player):
    move = int(input("Your move ? : "))
    root = root.children[move]
    addPlank(root)
    return(move, root)
