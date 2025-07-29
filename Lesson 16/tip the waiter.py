
bill = float(input("Enter the bill amnount: "))
tipperc = float(input("Enter tip percentage: "))

def tip(bill, tipperc):
    total = bill * (1+0.01*tipperc)
    total = round(total, 2)
    print(total)

tip(bill, tipperc)
