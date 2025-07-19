# Configuration Section
import turtle as t

t.speed(1)

t.width(5)
    
t.color("#ff0000")


# Function shape Section
def drawRectangle(width, length):
    for _ in range(2):        
        t.forward(width)
        t.left(360/4)
        t.forward(length)  
        t.left(360/4)

def drawTriangle(length):
    for _ in range(3):
        t.forward(length)
        t.right(360/3)

def drawCircle(length):
    for _ in range(360):        
        t.forward(length)
        t.left(360/360)

def drawPentagon(length):
    for _ in range(5):
        t.forward(length)
        t.left(360/5)

def drawHexagon(length):
 for i in range(6):
    t.forward(length)
    t.left(60)

def drawSquare(length):
 for i in range(4):
    t.forward(length)
    t.left(90)

def Goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw any thing
def drawHouse():
    drawSquare(4)
    t.forward(100)
    t.left(90)
    drawTriangle(3)

# def drawGirl():


# Main Section
drawHouse()
t.right(180)
t.penup()
t.forward(200)
t.pendown()
drawHexagon(50)
t.penup()
t.backward(100)
t.pendown()
drawSquare(50)
t.done()
commit crime scene is bad ok