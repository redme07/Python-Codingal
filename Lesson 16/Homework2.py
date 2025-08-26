method = int(input("If you have the diameter of the circle press 1 otherwise if you have the radius press 2: "))

def circumfrnce(method):
    if method == 1:
        diameter = float(input("Enter the diameter of the circle"))
        circumfrance = 3.1415 * diameter
        return circumfrance
    elif method == 3:
        radius = float(input("Enter the radius"))
        circumfrance2 = 2*3.1415*radius
        return circumfrance2
    else:
        return "Error"
    
print(circumfrnce(method))