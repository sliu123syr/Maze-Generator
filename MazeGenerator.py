import random
import pygame

rows = 10
cols = 10
nodelength = 30

nodeList = []

def main():
    pygame.init()
    startwindow = pygame.display.set_mode([750,800])
    startwindow.fill((255, 255, 255))

    global rows
    global cols
    global nodelength

    running = True
    while running:
        pygame.time.delay(20)
        drawcontents(startwindow)
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if increase_rows.isOver(pos):
                    rows = rows + 1
                if decrease_rows.isOver(pos) and rows > 1:
                    rows = rows - 1
                if increase_cols.isOver(pos):
                    cols = cols + 1
                if decrease_cols.isOver(pos) and cols > 1:
                    cols = cols - 1
                if increase_node.isOver(pos):
                    nodelength = nodelength + 1
                if decrease_node.isOver(pos) and nodelength > 1:
                    nodelength = nodelength - 1
                if Start_Game.isOver(pos):
                    running = False
                    pygame.quit()
                    createmaze()

            if event.type == pygame.MOUSEMOTION:
                if increase_rows.isOver(pos):
                    increase_rows.color = (255, 0, 0)
                else:
                    increase_rows.color = (255, 255, 255)
                if decrease_rows.isOver(pos) and rows > 1:
                    decrease_rows.color = (255, 0, 0)
                else:
                    decrease_rows.color = (255, 255, 255)
                if increase_cols.isOver(pos):
                    increase_cols.color = (255, 0, 0)
                else:
                    increase_cols.color = (255, 255, 255)
                if decrease_cols.isOver(pos) and cols > 1:
                    decrease_cols.color = (255, 0, 0)
                else:
                    decrease_cols.color = (255, 255, 255)
                if increase_node.isOver(pos):
                    increase_node.color = (255, 0, 0)
                else:
                    increase_node.color = (255, 255, 255)
                if decrease_node.isOver(pos) and nodelength > 1:
                    decrease_node.color = (255, 0, 0)
                else:
                    decrease_node.color = (255, 255, 255)
                if Start_Game.isOver(pos):
                    Start_Game.color = (255, 0, 0)
                else:
                    Start_Game.color = (255, 255, 255)

                    
def drawcontents(startwindow):
    startwindow.fill((255, 255, 255))
    
    increase_rows.draw(startwindow, (0, 0, 0))
    decrease_rows.draw(startwindow, (0, 0, 0))
    increase_cols.draw(startwindow, (0, 0, 0))
    decrease_cols.draw(startwindow, (0, 0, 0))
    increase_node.draw(startwindow, (0, 0, 0))
    decrease_node.draw(startwindow, (0, 0, 0))
    Start_Game.draw(startwindow, (0, 0, 0))

    textfont = pygame.font.SysFont('comicsans', 40)
    introfont = pygame.font.SysFont('comicsans', 60)

    RowsText = textfont.render('Number of Rows', 1, (0, 0, 0))
    ColsText = textfont.render('Number of Columns', 1, (0, 0, 0))
    NodeText = textfont.render('Size of Each Node', 1, (0, 0, 0))
    NumberOfRows = textfont.render(str(rows), 1, (0, 0, 0))
    NumberOfCols = textfont.render(str(cols), 1, (0, 0, 0))
    SizeOfNodes = textfont.render(str(nodelength), 1, (0, 0, 0))
    IntroText = introfont.render('Choose Your Options', 1, (0, 0, 0))
    WindowWidth = textfont.render('Width of Window: ' + str(cols*nodelength) + " Pixels", 1, (0, 0, 0))
    WindowHeight = textfont.render('Height of Window: ' + str(rows*nodelength)+ " Pixels", 1, (0, 0, 0))

    startwindow.blit(RowsText, (115, 160))
    startwindow.blit(ColsText, (400, 160))
    startwindow.blit(NodeText, (250, 310))
    startwindow.blit(NumberOfRows, (210, 210))
    startwindow.blit(NumberOfCols, (510, 210))
    startwindow.blit(SizeOfNodes, (360, 360))
    startwindow.blit(IntroText, (160, 60))
    startwindow.blit(WindowWidth, (180, 450))
    startwindow.blit(WindowHeight, (180, 500))

def createmaze():

    global nodeList
    nodeList = []
    for i in range (rows):
        for j in range (cols):
            newNode = Node(i,j,len(nodeList)+1)
            nodeList.append(newNode)

    curNode = nodeList[0]
    nodeStack = Stack()
    fillednodes = 0

    pygame.init()
    mainwindow = pygame.display.set_mode([cols*nodelength+50, rows*nodelength+50])
    
    delay = 60
    running = True
    while running:
        pygame.time.delay(delay)
        nextNode = curNode.randomneighbor()
        if nextNode != False:
            nodeStack.push(curNode)
            curNode = nextNode
            fillednodes = fillednodes + 1
        elif nodeStack.size() > 0:
            curNode = nodeStack.pop()
        else:
            running = False

        mainwindow.fill((255, 255, 255))
        draw(mainwindow, curNode)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    delay = -1

    playinggame(mainwindow, curNode)

def draw(mainwindow, curNode):
    Color_line=(0,0,0)
    for i in nodeList:
        if i == curNode:
            pygame.draw.rect(mainwindow, (0,0,255), pygame.Rect(i.col*nodelength+25, i.row*nodelength+25, nodelength, nodelength))
        if i.top and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+25))
        if i.left and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+25), (i.col*nodelength+25, i.row*nodelength+nodelength+25))
        if i.right and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+nodelength+25, i.row*nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+nodelength+25))
        if i.bot and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+nodelength+25))

def playinggame(mainwindow, curNode):
    running = True
    while running:
        pygame.time.delay(0)
        mainwindow.fill((255, 255, 255))
        drawgame(mainwindow, curNode)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                main()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and curNode.left == False:
                    curNode = curNode.returnneighbor('Left')
                if event.key == pygame.K_RIGHT and curNode.right == False:
                    curNode = curNode.returnneighbor('Right')
                if event.key == pygame.K_UP and curNode.top == False:
                    curNode = curNode.returnneighbor('Top')
                if event.key == pygame.K_DOWN and curNode.bot == False:
                    curNode = curNode.returnneighbor('Bot')
                    
        if curNode == nodeList[-1]:
            running == False
            pygame.quit()
            main()
            break


def drawgame(mainwindow, curNode):
    Color_line=(0,0,0)
    for i in nodeList:
        if i == curNode:
            pygame.draw.circle(mainwindow, (0,0,0), (i.col*nodelength+25+(nodelength/2), i.row*nodelength+25+(nodelength/2)),nodelength/2)
        if i == nodeList[-1]:
            pygame.draw.rect(mainwindow, (255,255,0), pygame.Rect(i.col*nodelength+25, i.row*nodelength+25, nodelength, nodelength))
        if i.top and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+25))
        if i.left and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+25), (i.col*nodelength+25, i.row*nodelength+nodelength+25))
        if i.right and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+nodelength+25, i.row*nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+nodelength+25))
        if i.bot and i.visited == True:
            pygame.draw.line(mainwindow, Color_line, (i.col*nodelength+25, i.row*nodelength+nodelength+25), (i.col*nodelength+nodelength+25, i.row*nodelength+nodelength+25))


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

    def returnneighbor(self, direction):
        if direction == 'Top':
            return nodeList[(self.index - cols) - 1]
        if direction == 'Left':
            return nodeList[self.index - 2]
        if direction == 'Right':
            return nodeList[self.index]
        if direction == 'Bot':
            return nodeList[(self.index + cols) - 1]

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

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4),0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

increase_rows = Button((255,255,255,), 275, 200, 50, 50, '+')
decrease_rows = Button((255,255,255,), 125, 200, 50, 50, '-')
increase_cols = Button((255,255,255,), 575, 200, 50, 50, '+')
decrease_cols = Button((255,255,255,), 425, 200, 50, 50, '-')
increase_node = Button((255,255,255,), 425, 350, 50, 50, '+')
decrease_node = Button((255,255,255,), 275, 350, 50, 50, '-')
Start_Game = Button((255,255,255,), 250, 600, 250, 70, 'Start Game')

main()






















