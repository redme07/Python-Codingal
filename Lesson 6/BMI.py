height = float(input("Enter your height in meters"))
weight = float(input("Enter your weight in Kg"))

BMI = (weight / (height*height))

if(BMI<=18.4):
    print(f"Your BMI is {BMI} which is underweight")

elif(BMI<=24.9):
    print(f"Your BMI is {BMI} which is healthy")

elif(BMI<=29.9):
    print(f"Your BMI is {BMI} which is overweight")

elif(BMI<=34.9):
    print(f"Your BMI is {BMI} which is severly overweight")

elif(BMI<=39.9):
    print(f"Your BMI is {BMI} which is obese")

else:
    print(f"Your BMI is {BMI} which is severly obese")