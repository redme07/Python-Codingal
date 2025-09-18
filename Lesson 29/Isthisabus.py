class vehicle:
    def __init__(self,name,mileage,speed):
        self.name = name
        self.mileage = mileage
        self.speed = speed

class bus(vehicle):
    pass

obj = bus("Volvo",25,90)
print(obj.name,obj.mileage,obj.speed)