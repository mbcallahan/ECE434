import curses
import time
global board
global x
global y
global width
global height

board=[]
x,y=0,0
width,height=0,0

def printStartInfo(mainscr):
    mainscr.clear()
    mainscr.addstr("Welcome to Matthew Callahan's terminal bassed etch-a-sketch\n use the w-a-s-d keys to move the currsor around, press c to clear the screen, and x to exit\n press any key to continue")
    mainscr.refresh()
    mainscr.getkey()

def clearScreen(mainscr):
    global board
    global x
    global y
    global width
    global height

    #clear terminal screen
    mainscr.clear()
    width=curses.COLS-1
    height=curses.LINES-1
    #fill array with zeros to keep track of board
    board=[[' ' for i in range(width)] for j in range(height)]
    x,y=0,0
    mainscr.move(y,x)
    mainscr.refresh()
    
def moveCursor(mainscr, direction):
    global board
    global x
    global y
    global width
    global height

    if direction=='up':
        y=y-1;
    elif direction=='down':
        y=y+1;
    elif direction=='right':
        x=x+1;
    elif direction=='left':
        x=x-1;
    #since this is a digital etch-asketch, the edges wrap
    if x>=width-1:
        x=0;
    if x<0:
        x=width-1;
    if y>=height-1:
        y=0
    if y<0:
        y=height-1
    board[x][y]='X'

    #reprint the entire screen, since I don't trust all the screens to have memory
    mainscr.clear()
    boardstr=''.join([str(item) for innerlist in board for item in innerlist])
                     
    mainscr.addstr(boardstr)
    mainscr.move(y,x)
    mainscr.refresh()
    
    

def main(mainscr):
    printStartInfo(mainscr)
    clearScreen(mainscr)
    while True:
        s= mainscr.getkey()
        if s=="x":
            break #exit loop
        elif s=="c":
            clearScreen(mainscr)
        elif s=="w":
            moveCursor(mainscr, 'up')
        elif s=="a":
            moveCursor(mainscr, 'left')
        elif s=="d":
            moveCursor(mainscr, 'right')
        elif s=="s":
            moveCursor(mainscr, 'down')
    
        

        
    

curses.wrapper(main)
 
