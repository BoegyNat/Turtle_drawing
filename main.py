print("hello")

print("hi My name is Boegy")

print("hi my name is Atom")

print("Auto: Hello!")


import turtle as t

t.speed(1)

t.width(5)
    
t.color("#ff0000")



def drawSquare(length):
    t.left(90)
    for _ in range(4):
        t.forward(100)
        t.left(360/4)

def drawRectangle(width, length):
    for _ in range(2):        
        t.forward(50)
        t.left(360/4)
        t.forward(100)  
        t.left(360/4)

def drawTriangle(length):
    for _ in range(3):
        t.forward(100)
        t.right(360/3)

def drawCircle(length):
    for _ in range(360):        
        t.forward(10)
        t.left(360/360)

def drawPentagon(length):
    for _ in range(5):
        t.forward(100)
        t.left(360/5)

def drawHexagon(length):
    for _ in range(6):
        t.forward(100)
        t.left(360/6)

def drawHouse():
    drawSquare(4)
    t.forward(100)
    t.left(90)
    drawTriangle(3)


# drawHouse()
# drawHexagon(100)

t. speed(10)

def draw_hexagon(lenght):
    t.forward(lenght)
    t.left(60)
    t.forward(lenght)
    t.left(60)
    t.forward(lenght)
    t.left(60)
    t.forward(lenght)
    t.left(60)
    t.forward(lenght)
    t.left(60)
    t.forward(lenght)
def draw_square(lenght):
    t.forward(lenght)
    t.left(90)
    t.forward(lenght)
    t.left(90)
    t.forward(lenght)
    t.left(90)
    t.forward(lenght)
drawHouse()
t.right(180)
t.penup()
t.forward(200)
t.pendown()
draw_hexagon(50)
drawRectangle(50)
# draw_square(50)
t.done()