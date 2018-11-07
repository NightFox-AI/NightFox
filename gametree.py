import copy
import boardpos

class TreeNode():
    def __init__(self, parent, boardpos=boardpos.Boardpos()):
        self.parent = parent
        self.children = []
        self.boardpos = boardpos
        self.pl1 = 0
        self.pl2 = 0
        self.leaf = False
        self.endPos = False
        
    def generateChildren(self, player):

        count = 0
        for element in range(len(self.boardpos.a[0])):
            if(self.boardpos.a[0][element] != 0):
                self.children.append(None)
                count += 1
            else:
                newBoardPos = boardpos.Boardpos()
                newBoardPos.a = copy.deepcopy(self.boardpos.a)
                for i in range(5, -1, -1):
                    if(newBoardPos.a[i][element] == 0):
                        newBoardPos.a[i][element] = player
                        break
                    
                rate(newBoardPos, player)
                rate(newBoardPos, toggle(player))
                self.children.append(TreeNode(boardpos=newBoardPos,
                                              parent=self))
            if(count == 7):
                self.endPos = True

    def makeTree(root, player, plank):

        if(plank == 0):
            return()
        
        else:
            root.generateChildren(player)
            for child in root.children:
                makeTree(child, toggle(player), plank-1)

                
def rate(boardPos, player):
    return(0)
                
def toggle(t):
    if(t == 1):
        return(2)
    elif(t == 2):
        return(1)
    else:
        return(t)
            
def printTree(root):

    if(root is None):
        return
    
    for row in root.boardpos.a:
        print(row)
    print()

    for child in root.children:
        printTree(child)
            
    
if(__name__ == "__main__"):

    root = TreeNode(parent = None)

    makeTree(root, 1, 2)
    printTree(root)
