import numpy as np
import random
import gametree
from gamecontrol import PLANK_DEPTH as pd

INF = 1000000

def move(playerObj1, root, player):
    # print("FROM MOVEMAKER =====")
    # if(1):
    #     for i in range(0,6):
    #         print(root.boardpos.a[i])
    # print("====================")
    if(any([i is not None for i in root.children])):

        if(0):
            val = random.randint(0, len(root.children)-1)
            if(root.children[val] is None):
                val = 0
                while(root.children[val] is None):
                    val += 1

        else:
            worthc = []
            for child in root.children:
                worthc.append(minimax(child, pd, -INF, INF, player, player, playerObj1))
                
            # print("worthc is {}".format(worthc))
            maxv = max(worthc)
            finc = [chld for chld in range(len(worthc)) if worthc[chld]==maxv]
            # print("finc is ", finc)
            val = random.choice(finc)
            
            if(root.children[val] is None):
                print("WARNING !!!")
                val = 0
                while(root.children[val] is None):
                    val += 1

        root = root.children[val]
        root = addPlank(root)
        return(val, root)
    else:
        return(0, root)


def evaluation(playerObj, root, player):
    mixer = np.array(playerObj.dna).reshape(1, 10)
    res = np.ndarray.tolist(normalize(np.dot(mixer, np.array(list(root.boardpos.players[player].values()) + list(root.boardpos.players[gametree.toggle(player)].values())))))
    # print("RES IS {}".format(res))
    return(res[0])
        

def minimax(position, depth, alpha, beta, player, maxp, playerObj1):
    if(position is None):
        return(-INF)
    
    if((position.leaf) or (position.endPos) or (depth == 0)):
        if(maxp == player):
            return(evaluation(playerObj1, position, player))
        return(-evaluation(playerObj1, position, player))
    
    if(maxp == player):
        maxeval = -INF
        for child in position.children:
            el = minimax(child, depth-1, alpha, beta, gametree.toggle(player), maxp, playerObj1)
            maxeval = max(maxeval, el)
            alpha = max(alpha, el)
            if(beta <= alpha):
                break
        return(maxeval)
    
    else:
        mineval = INF
        for child in position.children:
            el = minimax(child, depth-1, alpha, beta, gametree.toggle(player), maxp, playerObj1)
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
