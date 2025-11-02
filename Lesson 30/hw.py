class BMW:
    def max_speed(self):
        return "BMW: Maximum speed is 250 km/h"

    def fuel_type(self):
        return "BMW: Uses petrol"

class Ferrari:
    def max_speed(self):
        return "Ferrari: Maximum speed is 340 km/h"

    def fuel_type(self):
        return "Ferrari: Uses premium petrol"


def car_details(car):
    print(car.max_speed())
    print(car.fuel_type())


bmw_car = BMW()
ferrari_car = Ferrari()


car_details(bmw_car)
print()
car_details(ferrari_car)