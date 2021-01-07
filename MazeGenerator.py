from graphics import *
import random

rows = 20
cols = 20

nodeList = []

def main():
    mainwindow = GraphWin("Maze Generator", cols*40, rows*40)
    mainwindow.setBackground("White")

    for i in range (rows):
        for j in range (cols):
            newNode = Node(i,j,len(nodeList)+1)
            nodeList.append(newNode)

    curNode = nodeList[0]
    nodeStack = Stack()
    fillednodes = 0
    while fillednodes <= (rows*cols - 2):
        print(curNode.index)
        nextNode = curNode.randomneighbor()
        if nextNode != False:
            nodeStack.push(curNode)
            curNode = nextNode
            fillednodes = fillednodes + 1
        else:
            curNode = nodeStack.pop()

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
        order = [1,2,3,4]
        random.shuffle(order)
        for num in order:
            if num == 1 and self.index > cols and nodeList[(self.index - cols) - 1].getvisited() == False:
                self.top = False
                self.visited = True
                nodeList[(self.index - cols) - 1].setvisited(True)
                nodeList[(self.index - cols) - 1].setbot(False)
                return nodeList[(self.index - cols) - 1]
            
            if num == 2 and self.index%cols != 1 and nodeList[self.index - 2].getvisited() == False:
                self.left = False
                self.visited = True
                nodeList[self.index - 2].setvisited(True)
                nodeList[self.index - 2].setright(False)
                return nodeList[self.index - 2]
            
            if num == 3 and self.index%cols != 0 and nodeList[self.index].getvisited() == False:
                self.right = False
                self.visited = True
                nodeList[self.index].setvisited(True)
                nodeList[self.index].setleft(False)
                return nodeList[self.index]
            
            if num == 4 and self.index+cols <= rows*cols and nodeList[(self.index + cols) - 1].getvisited() == False:
                self.bot = False
                self.visited = True
                nodeList[(self.index + cols) - 1].setvisited(True)
                nodeList[(self.index + cols) - 1].settop(False)
                return nodeList[(self.index + cols) - 1]
        return False

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

main()
