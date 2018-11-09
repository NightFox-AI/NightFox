import random

def move(playerObj, root):
    if(any([i is not None for i in root.children])):
        val = random.randint(0, len(root.children)-1)
        if(root.children[val] is None):
            val = 0
            while(root.children[val] is None):
                val += 1
        root = root.children[val]
        root = addPlank(root)
        return(val, root)
    else:
        
        exit(0)

def addPlank(root):

    if((root is None)):
        pass

    elif((root.leaf) and (not root.endPos)):
        root.generateChildren()

    else:
        for child in range(len(root.children)):
            root.children[child] = addPlank(root.children[child])
    return(root)
