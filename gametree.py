"""
This is the game tree class
"""
import copy
import boardpos

class TreeNode():
    """
    Each node in the game tree is an object
    of this class
    """
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
                self.children.append(TreeNode(boardpos=newBoardPos,
                                              parent=self))
            if(count == 7):
                self.endPos = True

class Tree():
    """
    This is the game tree class
    """
    def __init__(self, root=TreeNode(parent=None)):
        self.root = root
        self.depth = 1

    def resetRoot(self, treeNode):
        pass
        
    def generateTrees(self, tree, plankNo):

        while(self.depth < plankNo):
            break
        
            
        
        



    
if(__name__ == "__main__"):

    node = TreeNode(parent = None)
    node.generateChildren(1)

    for child in node.children:
        for row in child.boardpos.a:
            print(row)
        print()
