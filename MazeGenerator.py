from graphics import *

rows = 10
cols = 10

def main():
    mainwindow = GraphWin("Maze Generator", cols*40, rows*40)
    mainwindow.setBackground("White")

    NodeList = []

    for i in range (rows):
        for j in range (cols):
            NewNode = Node(i,j)
            NodeList.append(NewNode)

    for i in NodeList:
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

            
    print("Test")




class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.top = True    
        self.left = False
        self.right = False
        self.bot = False
    





main()
