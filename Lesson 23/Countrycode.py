codeinp = input("Enter a country whose code you want: ")

countrycode = {"India": "0091", "Australia": "0025", "Nepal": "00977"}

get = countrycode.get(codeinp, "Not Found")
# If the first input value returns false then "Not Found will print"

print(get)