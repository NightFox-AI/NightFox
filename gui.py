#! /usr/bin/env python3

import gametree
import pickle
import boardpos
from gamecontrol import PLANK_DEPTH as pd
from tkinter import *
from gui_arena import Boardposs
import ga2
import arena
import movemaker

class AgentClass():
    def __init__(self):
        self.dna = []
        self.fitness = 0
    
class GUI:
    elementSize = 50
    gridBorder = 3
    gridColor = "#AAA"
    p1Color = "#4096EE"
    p2Color = "#FF1A00"
    backgroundColor = "#ffffff"
    gameOn = False
    
    def __init__(self, master):
        self.master = master

        master.title('Connect Four')
        
        label = Label(master, text="NightFox")
        label.grid(row=0)

        button = Button(master, text="New Game!", command=self._newGameButton)
        button.grid(row=1)
        
        self.canvas = Canvas(master, width=200, height=50, background=self.backgroundColor, highlightthickness=0)
        self.canvas.grid(row=2)

        self.currentPlayerVar = StringVar(self.master, value="")
        self.currentPlayerLabel = Label(self.master, textvariable=self.currentPlayerVar, anchor=W)
        self.currentPlayerLabel.grid(row=3)

        self.canvas.bind('<Button-1>', self._canvasClick)
        self.state=True

        # from here 
        fd = open("BAGENT.dna", 'rb')
        self.playerObj1 = AgentClass()
        self.playerObj1.dna = pickle.load(fd)
        fd.close()
        self.gameOver = False
        self.player = 1
        self.root = gametree.TreeNode(parent=None, player=self.player)
        self.root.makeTree(pd)
        self.board = boardpos.Boardpos()
        
        self.newGame()

    def draw(self):       
        for self.c in range(self.game.size['c']):
            for r in range(self.game.size['r']):
                if r >= len(self.game.grid[self.c]): continue
                
                x0 = self.c*self.elementSize
                y0 = r*self.elementSize
                x1 = (self.c+1)*self.elementSize
                y1 = (r+1)*self.elementSize
                fill = self.p1Color if self.game.grid[self.c][r] == self.game.players[True] else self.p2Color
                self.canvas.create_oval(x0 + 2,
                                        self.canvas.winfo_height() - (y0 + 2),
                                        x1 - 2,
                                        self.canvas.winfo_height() - (y1 - 2),
                                        fill = fill, outline=self.gridColor)

    def drawGrid(self):
        x0, x1 = 0, self.canvas.winfo_width()
        for r in range(1, self.game.size['r']):
            y = r*self.elementSize
            self.canvas.create_line(x0, y, x1, y, fill=self.gridColor)

        y0, y1 = 0, self.canvas.winfo_height()
        for self.c in range(1, self.game.size['c']):
            x = self.c*self.elementSize
            self.canvas.create_line(x, y0, x, y1, fill=self.gridColor)

    def drop(self, column):
        return self.game.drop(column)

    def newGame(self):
        # Ask for players' names
        self.p1 = 'Blue'
        self.p2 = 'Red'

        # Ask for grid size
        columns = 7
        rows = 6
        
        #self.game = ConnectFour(columns=columns, rows=rows)
        self.game = Boardposs()

        self.canvas.delete(ALL)
        self.canvas.config(width=(self.elementSize)*self.game.size['c'],
                           height=(self.elementSize)*self.game.size['r'])
        self.master.update() # Rerender window
        self.drawGrid()
        self.draw()

        self._updateCurrentPlayer()

        self.gameOn = True
        fd = open("BAGENT.dna", 'rb')
        self.playerObj1 = AgentClass()
        self.playerObj1.dna = pickle.load(fd)
        fd.close()
        self.gameOver = False
        self.player = 1
        self.root = gametree.TreeNode(parent=None, player=self.player)
        self.root.makeTree(pd)
        self.board = boardpos.Boardpos()
        
    def _updateCurrentPlayer(self):
        p = self.p1 if self.game.first_player else self.p2
        self.currentPlayerVar.set('Current player: ' + p)

    def _canvasClick(self, event):
        if not self.gameOn: return
        if self.game.game_over: return
        
        if self.state == True:
            self.c = event.x // self.elementSize
            move = self.c
            self.oldpos = self.root.boardpos
            #print("pos = c ", self.c, self.root.children)
            move, self.root = movemaker.acceptmove(self.root, move)
            gameOver = arena.change_vals(self.oldpos, move, self.player)
            self.player = gametree.toggle(self.player)

            if (0 <= self.c < self.game.size['c']):
                self.drop(self.c)

                #send data to function

                self.draw()
                self._updateCurrentPlayer()

            if self.game.game_over:
                x = self.canvas.winfo_width() // 2
                y = self.canvas.winfo_height() // 2
                if self.game.game_over == 'draw':
                    t = 'DRAW!'
                else:
                    winner = self.p1 if self.game.first_player else self.p2
                    t = winner + ' won!'
                self.canvas.create_text(x, y, text=t, font=("Helvetica", 32), fill="#333")
                self.state=False

            else:
                oldpos = self.root.boardpos
                move, self.root = movemaker.move(self.playerObj1, self.root, self.player)
                gameOver = arena.change_vals(self.oldpos, move, self.player)
                self.player = gametree.toggle(self.player)
                self.c = move
                if (0 <= self.c < self.game.size['c']):
                    self.drop(self.c)

                    #send data to function

                    self.draw()
                    self._updateCurrentPlayer()

                if self.game.game_over:
                    x = self.canvas.winfo_width() // 2
                    y = self.canvas.winfo_height() // 2
                    if self.game.game_over == 'draw':
                        t = 'DRAW!'
                    else:
                        winner = self.p1 if self.game.first_player else self.p2
                        t = winner + ' won!'
                    self.canvas.create_text(x, y, text=t, font=("Helvetica", 32), fill="#333")
                    self.state=True

    def _newGameButton(self):
        self.newGame()

    def _play_gat(self):
        playerObj1 = Temp()
        # fd = open("BAGENT.dna", 'wb')
        # pickle.dump(playerObj1, fd)
        # fd.close()
        
        oldpos = root.boardpos
        #move, root = movemaker.acceptmove(root, player)
        move = self.c
        root = root.childfren[self.c]
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

root = Tk()
app = GUI(root)

root.mainloop()
