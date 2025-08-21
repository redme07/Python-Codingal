days = int(input("Enter number of days at hotel: "))
city = input("Which city do you want to travel: banglore, delhi, mumbai or hyderabd: ")
days2 = int(input("Enter number of days used of rental car: "))
price = float(input("Enter the amnount of rental car per day: "))
price2 = float(input("Enter the cost of hotel per day: "))
spending = float(input("Enter spending money: "))
def hotel(days, price2):
    return price2 * days
def plane(city):
    if city == "hyderabad":
        return 5000
    elif city == "delhi":
        return 6000
    elif city == "banglore":
        return 7000
    elif city == "mumbai":
        return 8000
    else:
        return "invalid"
    
def car(days2, price):
    if days >= 7:
        return price * days2 - 100
    elif days >= 3:
        return price * days2 - 75
    else:
        return price * days2
    
def tripcost(days, price2, price, days2, city, spending):
    return hotel(days, price2) + plane(city) + car(days2, price) + spending

print(tripcost(days, price2, price, days2, city, spending))
        