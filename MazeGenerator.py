from graphics import *
import random

rows = 10
cols = 10

nodeList = []

def main():
    mainwindow = GraphWin("Maze Generator", cols*40, rows*40)
    mainwindow.setBackground("White")

    for i in range (rows):
        for j in range (cols):
            newNode = Node(i,j,len(nodeList)+1)
            nodeList.append(newNode)

    curNode = nodeList[0]
    draw(mainwindow)


def draw(mainwindow):
    for i in nodeList:
        if i.top:
            topline = Line(Point(i.col*40, i.row*40), Point(i.col*40+40, i.row*40))
            topline.draw(mainwindow)
        if i.left:
            topline = Line(Point(i.col*40, i.row*40), Point(i.col*40, i.row*40+40))
            topline.draw(mainwindow)
        if i.right:
            topline = Line(Point(i.col*40+40, i.row*40), Point(i.col*40+40, i.row*40+40))
            topline.draw(mainwindow)
        if i.bot:
            topline = Line(Point(i.col*40, i.row*40+40), Point(i.col*40+40, i.row*40+40))
            topline.draw(mainwindow)

class Node:
    def __init__(self, row, col, index):
        self.row = row
        self.col = col
        self.index = index
        self.top = True    
        self.left = True
        self.right = True
        self.bot = True
        self.visited = False

    def settop(self, value):
        self.top = value
        
    def setleft(self, value):
        self.left = value

    def setright(self, value):
        self.right = value

    def setbot(self, value):
        self.bot = value

    def setvisited(self, value):
        self.visited = value

    def getvisited(self):
        return self.visited

    def randomneighbor(self):
        while True:
            num = random.randint(1,4)
            if (num == 1) and self.index > self.col and nodeList[self.index - self.col].getvisited() == False:
                self.top = False
                nodeList[self.index - self.col].setbot(False)
                return nodeList[self.index - self.col]
            if num == 2 and self.index%self.col != 1 and nodeList[self.index - 1].getvisited() == False:
                self.left = False
                nodeList[self.index - 1].setright(False)
                return nodeList[self.index - 1]
            if num == 1 and self.index%self.col != 0 and nodeList[self.index + 1].getvisited() == False:
                self.right = False
                nodeList[self.index + 1].setleft(False)
                return nodeList[self.index + 1]
            if num == 1 and self.index+self.col <= self.row*self.col and nodeList[self.index + self.col].getvisited() == False:
                self.bot = False
                nodeList[self.index + self.col].settop(False)
                return nodeList[self.index + self.col]
            
        





main()
