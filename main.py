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
    drawSquare(200)
    t.forward(200)
    t.left(90)
    drawTriangle(200)
    t.left(90)
    t.forward(50)
    t.right(90)
    drawWindow()
    t.left(90)
    t.forward(110)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(120)
    t.left(90)
    drawDoor()
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.penup()
    t.forward(15)
    t.pendown()
    drawCircle(0.1)
def drawTree():
    t.left(180)    
    drawRectangle(50, 100)
    t.left(90)  
    t.forward(100)
    t.right(90)
    t.backward(25)
    drawPentagon(100)

def drawGirl():
    t.color("pink")
    t.right(180)
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

def drawMan():
    t.color("blue")
    t.left(90)
    t.pendown()
    drawCircle(0.5)
    t.right(30)
    t.forward(75)
    t.backward(75)
    t.left(240)
    t.forward(75)
    t.backward(75)
    t.left(60)
    t.forward(90)
    t.left(30)
    t.forward(75)
    t.backward(75)
    t.left(300)
    t.forward(75)
    t.backward(75)
    t.right(60)
    

def drawSun():
    t.color("orange")
    drawCircle(0.5)
    t.penup()
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    for _ in range(12):
        t.penup()
        t.forward(40)
        t.pendown()
        t.forward(20)
        t.penup()
        t.backward(60)
        t.right(30)

def drawPlatypus():
    t.left(90)
    # body
    drawRectangle(100, 50)
    # tail    
    t.forward(100)
    t.left(90)
    t.forward(35)
    t.right(90)
    drawTriangle(50)
    # mouth
    t.left(90)
    t.backward(35)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    # legs    
    t.right(90)
    t.forward(50)        
    t.backward(25)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(25)
    t.backward(25)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(25)
    t.backward(25)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(25)
    # eye
    t.backward(60)
    t.right(90)
    t.penup()
    t.forward(80)
    t.pendown()
    drawCircle(0.1)

def drawChair():
    t.right(90)
    t.forward(80)
    t.right(180)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)

def drawTable():
    t.left(90)
    t.forward(140)
    t.right(90)
    t.forward(40)
    t.backward(40)
    t.right(90)
    t.forward(140)
    t.left(90)
    t.forward(40)
    
def drawChair2():
    t.forward(80)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

def drawDino():
# head
    drawSquare(100)
# eyes
    t.left(90)
    t.forward(60)
    t.penup()
    t.right(90)    
    t.forward(25)
    t.pendown()
    drawCircle(0.2)
    t.penup()
    t.forward(50)
    t.pendown()
    drawCircle(0.2)
# tongue
    t.penup()
    t.backward(75)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.pendown()
    t.right(90)
    drawRectangle(60, 40)
 # necks
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.left(90)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
 # back   
    t.forward(50)
    drawSquare(100)
# body
    t.left(90)
    t.forward(100)
    t.right(90)
    drawRectangle(200, 100)
# legs
    t.left(90)
    t.forward(100)
    t.right(90)
    drawRectangle(50, 100)
    t.forward(150)
    drawRectangle(50, 100)
# tails
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.left(90)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    t.left(90)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    drawSquare(50)
    t.forward(50)
    t.right(180)
    drawSquare(50)

def drawWindow():
    drawSquare(80)
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.backward(80)
def drawDoor():
    t.left(180)
    t.forward(70)
    t.right(90)
    t.forward(120)
    # Goto(-185,60)


# Main Section
Goto(-1000, 0)
t.forward(10000)
Goto(0, 0)
drawHouse()
Goto(60, 80)
drawChair()
Goto(120, 40)
drawTable()
Goto(320, 80)
drawChair2()
Goto(-400, 25)
drawPlatypus()
Goto(-550, 130)
drawGirl()
Goto(-680, 160)
drawMan()
Goto(500, 0)
drawTree()
Goto(200, -150)
drawDino()
Goto(400, 0)
t.right(90)
drawHexagon(20)
Goto(300, 300)
drawSun()


# Goto(-120, 0)
# drawDino()


t.done()
