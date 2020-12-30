from tkinter import *

rows = 10
cols = 10

def main():
    mainwindow = Tk()
    mainwindow.geometry(str(rows*40)+"x"+str(cols*40))
    mainwindow.mainloop()

    NodeList = []
    
    for i in range (rows):
        for j in range (cols):
            NewNode = Node(i,j)
            NodeList.append(NewNode)



class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    





main()