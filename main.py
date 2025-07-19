# Configuration Section
import turtle as t

t.speed(1000)

t.width(5)
    
t.color("#ff0000")


# Function shape Section
def drawSquare(length):
 for i in range(4):
    t.forward(length)
    t.left(90)

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

def Goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw any thing
def drawHouse():
    t.left(90)
    drawSquare(100)
    # t.left(90)
    t.forward(100)
    t.left(90)
    drawTriangle(100)

def drawTree():
    t.left(180)    
    drawRectangle(50, 100)
    t.left(90)  
    t.forward(100)
    t.right(90)
    t.backward(25)
    drawPentagon(100)

def drawGirl():
    drawCircle(0.5)
    t.right(60)
    drawTriangle(100)
    t.left(25)
    t.forward(75)
    t.backward(75)
    t.left(250)
    t.forward(75)
    t.backward(75)
    t.left(55)
    t.penup()
    t.forward(85)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.pendown()
    t.forward(45)
    t.backward(45)
    t.right(90)
    t.penup()
    t.forward(30)
    t.left(90)
    t.pendown()
    t.forward(45)
# Main Section
drawHouse()
Goto(300, 0)
drawTree()
drawGirl()
# t.right(180)
# t.penup()
# t.forward(200)
# t.pendown()
# drawHexagon(50)

t.done()
