import turtle

turtle.Screen().bgcolor("red")
turtle.Screen().setup(400, 500)

polygon = turtle.Turtle()

numsides = int(input("Enter the number of sides polygon should have"))

side = int(input("Enter the length of side"))

sumang = (numsides - 2)*180
intang = sumang/numsides

for i in range(numsides):
    polygon.forward(side)
    polygon.left(intang)

turtle.done()