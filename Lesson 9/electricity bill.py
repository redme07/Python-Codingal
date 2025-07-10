units = int(input("Enter the amnount of units consumed"))

if(units <= 50):
    amnount = units * 2.60
    surcharge = 25

elif(units <= 100):
    amnount = 130 + ((units - 50)* 3.25)
    surcharge = 35

elif(units <= 200):
    amnount = 130 + 162.5 + ((units - 100)* 5.26)
    surcharge = 45

else:
    amnount = 130 + 162.5 + 526 + ((units - 200)* 8.45)
    surcharge = 75

total = amnount + surcharge

print(f"Your electricity bill is {total}")