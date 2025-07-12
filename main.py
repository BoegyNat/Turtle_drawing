print("hello")

print("hi My name is Boegy")

print("hi my name is Atom")

print("Auto: Hello!")


import turtle as t

t.speed(0.1)

t.width(5)
    
t.color("#ff0000")

xx = -360
yy= 260
t.penup()
t.goto(xx, yy)
t.pendown()

def drawTriangle(length):
    for _ in range(3):
        t.forward(10)
        t.left(360/3)


def drawSquare(length):
    for _ in range(4):
        t.forward(10)
        t.left(360/4)

def drawHouse():
    drawTriangle(3)
    t.right(90)
    drawSquare(4)

def drawSoi(space):
    for _ in range(5):
        drawHouse()
        t.left(90)
        t.penup()
        t.forward(20)
        t.pendown()

def drawPhase(space):
    for _ in range(4):
        drawSoi(0)
        t.penup()
        t.goto(t.xcor()-100, t.ycor()-30)
        t.pendown()

def drawVillage():
    for _ in range(2):
        drawPhase(0)
        t.penup()
        t.goto(t.xcor(), t.ycor()-20)
        t.pendown()
    t.penup()
    t.goto(-230, 260)
    t.pendown()
    for _ in range(2):
        drawPhase(0)
        t.penup()
        t.goto(-230, t.ycor()-20)
        t.pendown()

drawVillage()

t.done()

