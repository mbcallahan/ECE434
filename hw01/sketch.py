#!/usr/bin/python3
import curses
 
global board
global x
global y
global width
global height

board=[]
x,y=0,0
width,height=0,0

#clears screen, prints introduction message, then waits for a keypress in a blocked state
#mainscr is the screen variable it prints to
def printStartInfo(mainscr):
    mainscr.clear()
    mainscr.addstr("Welcome to Matthew Callahan's terminal bassed etch-a-sketch\n use the w-a-s-d keys to move the currsor around, press c to clear the screen, and x to exit\n press any key to continue")
    mainscr.refresh()
    mainscr.getkey()
#clears the screen and the variables that stores its state
def clearScreen(mainscr):
    global board
    global x
    global y
    global width
    global height

    #clear terminal screen
    mainscr.clear()
    width=curses.COLS
    height=curses.LINES-1 #the screen has one fewer lines than it reports
    #fill array with zeros to keep track of board
    board=[[' ' for i in range(width)] for j in range(height)]
    mainscr.move(y,x)
    mainscr.refresh()
#this moves the cursor on the screen and prints an X at this new location    
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
    board[y][x]='X'

    #reprint the entire screen, since I don't trust all the screens to have memory
    mainscr.clear()
    boardstr=''.join([str(item) for innerlist in board for item in innerlist])
                     
    mainscr.addstr(boardstr)
    mainscr.move(y,x)
    mainscr.refresh()
    
    

def main(mainscr):
    printStartInfo(mainscr)
    x,y=0,0
    clearScreen(mainscr)
    while True:
        s= mainscr.getkey()#wait for key press on active window, implicitly interrupt driven
        #since only one key is accepted, this  can be a switch statement and diagonal movement is not possible
        
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
 
