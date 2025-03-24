import ipyturtle3 as t3

def Turtle(width = 500, height = 500):
    myCanvas=t3.Canvas(width, height)
    display(myCanvas)
    myTS = t3.TurtleScreen(myCanvas)
    myTS.clear()
    return t3.Turtle(myTS)

def testIt():
    t = Turtle()

    t.color("blue")
    t.pensize(3)
    t.penup()
    t.goto(-200, -50)
    t.pendown()
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.color("green")
    t.pensize(10)
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.goto(-100, 0)
    t.goto(-30, 120)
