from datetime import date, time, datetime

dt = date.today()#.today from the date library print the date
now = datetime.now()#datetime.now prints the time and date currently

print("The date today is", dt)
print("The time and date today is", now)
print(dt.year)
#When you use .year with the variable where you stored.today it will print the year currntly
print(dt.month)
#When you use .month with the variable where you stored.today it will print the month currntly
print(dt.day)
#When you use .day with the variable where you stored.today it will print the day currntly