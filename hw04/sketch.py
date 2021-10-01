#!/usr/bin/python3

#i2C comes from i2cmatrix.py example from Dr. Yoder
import smbus
import time
#from Dr. Yoder's presentation on gpioviaFlask, specifically app3
from flask import Flask, render_template, request
app=Flask(__name__)


#these are state variables
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
    #global board
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
    global board
    
    #clear terminal screen
    #fill array with zeros to keep track of board
    board=[[0 for i in range(width)] for j in range(height)]
    printBoard()
   
#this moves the cursor on the screen and prints an X at this new location    
def moveCursor(direction):
    global board
    global x
    global y
    
    if 'up' in direction:
        y=y+1;
    if 'down' in direction:
        y=y-1;
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

@app.route("/")#setup the landing page, a good place to put intialization
def index():
    global board
    global x
    global y
    #clearScreen()
    print(board)
    return render_template('index.html')


@app.route("/<deviceName>/<action>")
def catchButtons(deviceName, action):
    if not (deviceName=="sketch"):
        print("Unexpected Button")
        return render_template('index.html')
    if action == "CLEAR":
        clearScreen()
   
   
    moveCursor(action)
    printBoard()
    return render_template('index.html')

if __name__=="__main__": #if this is being run directly and not used as a library
    printStartInfo()
    time.sleep(1)
   
    clearScreen() #clear screen with initialization to array is correct size
    print(board)
    app.run(host='0.0.0.0', port=8081,debug=True)#use default ip, port 8081 to not conflict with cloud9
