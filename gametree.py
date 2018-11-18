import copy
import movemaker
import boardpos
import referee

class TreeNode():
    def __init__(self, parent, player, boardpos=boardpos.Boardpos()):
        self.parent = parent
        self.children = []
        self.boardpos = copy.deepcopy(boardpos)
        self.player = player
        self.leaf = True
        self.endPos = False
        rate(self.boardpos, self.player)
        
    def generateChildren(self):
        
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
                        newBoardPos.a[i][element] = self.player
                        break
                
                # rate(newBoardPos, self.player)
                # print("New players are ", newBoardPos.players)
                self.children.append(TreeNode(player=toggle(self.player), boardpos=newBoardPos,
                                              parent=self))
                
            if(count >= 7):
                self.endPos = True
            else:
                self.leaf = False

                
    def makeTree(self, plank):

        if(plank == 0):
            self.leaf = True
        
        elif(not self.endPos):
            self.leaf = False
            self.generateChildren()
            for child in self.children:
                child.makeTree(plank-1)
        else:
            self.leaf = True
                
                
def rate(boardPos, player):
    referee.referee(boardPos, player)


def toggle(t):
    if(t == 1):
        return(2)
    elif(t == 2):
        return(1)
    else:
        return(t)


def printB(root):
    print("This is board")
    if(not root.leaf):
        for row in root.boardpos.a:
            print(row)
        print()
    else:
        print("Empty")


def printTree(root):

    if(root is None):
        return

    print(root.endPos, root.leaf)
    for row in root.boardpos.a:
        print(row)
    print()

    for child in root.children:
        printTree(child)


if(__name__ == "__main__"):

    root = TreeNode(parent = None, player = 1)
    root.generateChildren()
    val, root = movemaker.move(10, root)
    printTree(root)
