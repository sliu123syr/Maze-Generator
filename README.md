# Maze-Generator
This is a maze generator and game written on python and using the pygame library. 

The program is using a recursive implementation, using a depth-first search algorithm and implemented using backtracking. The program follows the following routine:

1. The program creates a grid of a certain height and width composed of cells, each with a top, left, right, and bottom wall.
2. While there are cells that have not been altered:
    1. If the current cell has neighbors (cells to its top, left, right, or bottom) that have not been visited:
      a) The current cell will be pushed to a stack.
      b) The program chooses one of the unvisited neighbors to the current cell.
      c) The walls between the current cell and the chosen neighbor will be removed.
      d) The chosen neighbor will become the current cell.
    2. If the current cell does not have any neighbors that have not been visited (and thus has reached a "dead-end"):
      a) The current cell will become a cell popped from the stack.

The program will allow you to initally choose how large the maze will be by determining the height and width of the maze in terms of the number of cells as well as determining the 
length, in pixels, of each cell. When running the program, the maze will be drawn cell by cell using the routine above in a new window. Hitting space will speed up the process and 
finish the maze generation. 

You are also able to navigate the maze. The player will control a circle generated at the top left corner of the maze using the up, down, left, and right keyboard keys. The exit 
to the maze is located at the bottom right. Finishing the maze will return you to the menu and allow you to select a new maze.

I had a lot of fun creating this program. I wanted to do this project mainly for two reasons: To learn pygame and learn to implement my code in a graphical user interface. 
Previously, I used the graphics.py file, which wasn't really powerful enough for me, at least not compared to pygame. I also wanted to learn algorithms and learn how to implement 
them in code. Implementing a maze generating algorithm was extremely challenging at first, but also really enjoyable and rewarding. I am really pleased as to how this project 
turned out.
