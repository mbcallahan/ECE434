#!/usr/bin/python3
import curses
import Adafruit_BBIO.GPIO as GPIO
import time
 
global board
global x
global y
global width
global height
global stayAlive

board=[]
x,y=0,0
width,height=0,0


buttonUp="P9_11"
buttonDown="P9_12"
buttonLeft="P9_13"
buttonRight="P9_14"

buttonDict= {buttonUp:'up', buttonDown:'down',buttonLeft:'left',buttonRight:'right'}

#clears screen, prints introduction message, then waits for a keypress in a blocked state
#mainscr is the screen variable it prints to
def printStartInfo(mainscr):
    global stayAlive
    stayAlive=True
    mainscr.clear()
    mainscr.addstr("Welcome to Matthew Callahan's terminal bassed etch-a-sketch\n use the buttons to move the currsor around, press opposite buttons to clear the screen, and all of them to exit\n the application will start in five seconds")
    mainscr.refresh()

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

    if 'up' in direction:
        y=y-1;
    elif 'down' in direction:
        y=y+1;
    elif 'right' in direction:
        x=x+1;
    elif 'left' in direction:
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

#this is the button intterupt handler. It checks all the buttons, checks to see if there is a command to override the buttons and make them do things other than move the cursor    
def catchKey(key):
    #go through eveyr button in case they are in combination, make variable to store this
    global commands
    commands=''
    #for loops go through the keys
    for button in buttonDict:
        if GPIO.input(button):
            commands+=buttonDict[button]
    #check for special commands to end the program
    if ('up' in commands) and ('down' in commands) and ('left' in commands) and ('right' in commands):
        global keepAlive
        keepAlive=False
        return
    if (('up' in commands) and ('down' in commands)) or(('left' in commands) and ('right' in commands)):
        global screenClear
        screenClear=True

def main(mainscr):
    global stayAlive
    GPIO.setup(buttonUp, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
    GPIO.setup(buttonDown, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
    GPIO.setup(buttonLeft, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
    GPIO.setup(buttonRight, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors

    #set event handlers for every button
    GPIO.add_event_detect(buttonUp, GPIO.BOTH, callback=catchKey)
    GPIO.add_event_detect(buttonDown, GPIO.BOTH, callback=catchKey)
    GPIO.add_event_detect(buttonLeft, GPIO.BOTH, callback=catchKey)
    GPIO.add_event_detect(buttonRight, GPIO.BOTH, callback=catchKey)

    printStartInfo(mainscr)
    for i in range(5):
        time.sleep(1)
    x,y=0,0
    global screenClear
    global commands
    clearScreen(mainscr)
    while stayAlive:
        if screenClear:
            clearScreen(mainscr)
        if not (commands==''):
            moveCursor(mainscr,commands)
            commands=''
    GPIO.cleanup()

        
    

curses.wrapper(main)
 
