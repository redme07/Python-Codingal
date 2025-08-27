import turtle

turtle.Screen().bgcolor("red")

mypen = turtle.Turtle()

size = 0

while 1 > 0:
    mypen.forward(size+1)
    mypen.left(90)
    size += 1

