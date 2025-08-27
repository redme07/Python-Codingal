import turtle

turtle.Screen().bgcolor("red")

#This line intializes the turtle
star = turtle.Turtle()

#defines how many pixels to move
star.forward(100)

star.left(120)
#120 is the angle at which the turtle will turn till
star.forward(100)
star.left(120)
star.forward(100)

star.penup()
#This line means that the turtle will not print 
# anything on the screen untile turtle.pendown command is given
star.right(150)
#moves the curses to 150 degrees
star.forward(50)

star.pendown()
star.right(90)
star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()
#ends the turtle 