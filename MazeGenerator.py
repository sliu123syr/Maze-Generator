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
            newNode = Node(i,j)
            nodeList.append(newNode)

    curNode = nodeList[0]

    draw(mainwindow)


def draw(mainwindow):
    for i in nodeList:
        if i.top:
            topline = Line(Point(i.row*40, i.col*40), Point(i.row*40+40, i.col*40))
            topline.draw(mainwindow)
        if i.left:
            topline = Line(Point(i.row*40, i.col*40), Point(i.row*40, i.col*40+40))
            topline.draw(mainwindow)
        if i.right:
            topline = Line(Point(i.row*40+40, i.col*40), Point(i.row*40+40, i.col*40+40))
            topline.draw(mainwindow)
        if i.bot:
            topline = Line(Point(i.row*40, i.col*40+40), Point(i.row*40+40, i.col*40+40))
            topline.draw(mainwindow)

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
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
        index = 2*self.row + self.col
        while True:
            num = random.randint(1,4)
            if (num == 1) and index > self.col and nodeList[index - self.col].getvisited() == False:
                self.top = False
                nodeList[index - self.col].setbot(False)
                return nodeList[index - self.col]
            if num == 2 and index%self.col != 1 and nodeList[index - 1].getvisited() == False:
                self.left = False
                nodeList[index - 1].setright(False)
                return nodeList[index - 1]
            if num == 1 and index%self.col != 0 and nodeList[index + 1].getvisited() == False:
                self.right = False
                nodeList[index + 1].setleft(False)
                return nodeList[index + 1]
            if num == 1 and index+self.col <= self.row*self.col and nodeList[index + self.col].getvisited() == False:
                self.bot = False
                nodeList[index + self.col].settop(False)
                return nodeList[index + self.col]
            
        





main()
