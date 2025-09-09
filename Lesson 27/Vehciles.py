class vehicles:
    def __init__(self,mileage,maxspeed):
#This is how u create constructor(which is every time an object is made)
#self is the place of the object it gets replaced by the object name
        self.mileage = mileage
        self.maxspeed = maxspeed

#This is how you use the constructor with the object
modelx = vehicles(20, 300)

print(f"The maximum speed of modelx is {modelx.maxspeed}")
print(f"The mileage of modelx is {modelx.mileage}")

