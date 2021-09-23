#!/usr/bin/python3

#i2C comes from i2cmatrix.py example from Dr. Yoder
import smbus
import time
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1,eQEP0

#setup encoders
encoder1= RotaryEncoder(eQEP0)
encoder2=RotaryEncoder(eQEP2)
encoder1.setAbsolute()
encoder1.enable()
encoder2.setAbsolute()
encoder2.enable()

#these are state variables
global board
global x
global y
global width
global height


board=[]
x,y=0,0
width,height=8,8
bus=smbus.SMBus(2)
matrix=0x70#fixed address for led screen
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)


#start by changing all squares to yellow to verufy led matrix is plugged in and working
def printStartInfo():
    allyellow=[0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff]
    bus.write_i2c_block_data(matrix,0,allyellow)
    
#convert board variable to the message to send to the green leds on the dot matrix
def printBoard():
    global board
    printlist=[]
    for y in range(height):
        line=0
        for x in range(width):
            line|=board[x][y]<<x
        printlist.append(line)#print in green
        printlist.append(0)#leave red blank
        
    bus.write_i2c_block_data(matrix,0,printlist)
#clears the screen and the variables that stores its state
def clearScreen():
    global screenClear
    global board
    global x
    global y
    global width
    global height

    #clear terminal screen
    #fill array with zeros to keep track of board
    board=[[0 for i in range(width)] for j in range(height)]
    printBoard()
   
#this moves the cursor on the screen and prints an X at this new location    
def moveCursor(direction):
    global board
    global x
    global y
    global width
    global height

    if 'up' in direction:
        y=y-1;
    if 'down' in direction:
        y=y+1;
    if 'right' in direction:
        x=x+1;
    if 'left' in direction:
        x=x-1;
    #since this is a digital etch-asketch, the edges wrap
    if x>=width:
        x=0;
    if x<0:
        x=width-1;
    if y>=height:
        y=0
    if y<0:
        y=height-1
    board[y][x]=1

   

printStartInfo()
time.sleep(1)

clearScreen()
x,y=3,3
board[x][y]=1
printBoard()
time.sleep(.25)
moveCursor('upleft')
printBoard()
time.sleep(1)
moveCursor('downright')
printBoard()
time.sleep(.25)
moveCursor('downright')
printBoard()
time.sleep(.25)
moveCursor('downright')
printBoard()
time.sleep(.25)
time.sleep(1)
clearScreen()
prev1=0
prev2=0
tollerance=2
while True:
    command=''

    #check the encoder movements
    if(encoder1.position>(prev1+tollerance)):
        command+='left'
        print('left')
    if(encoder1.position<(prev1-tollerance)):
        command+='right'
        print('right')
    if(encoder2.position>prev2+tollerance):
        command+='up'
    if(encoder2.position<prev2-tollerance):
        command+='down'
    prev1=encoder1.position
    prev2=encoder2.position        
    moveCursor(command)
    printBoard()

    time.sleep(0.25)#poll at 4Hz
    
