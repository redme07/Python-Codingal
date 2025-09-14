class Circle:
    def __init__(self, radius):
        self.radius = radius  # constructor with radius variable

    def area(self):
        return 3.1416 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.1416 * self.radius


# Taking radius as input from user
r = float(input("Enter the radius of the circle: "))

c1 = Circle(r)  # create object with user radius
print("Area:", c1.area())
print("Circumference:", c1.circumference())
