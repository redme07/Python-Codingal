import time
import random
startdate = input("The starting date in %d/%m/%Y: ")
enddate = input("The edning date in %d/%m/%Y: ")
def randomdate(startdate, enddate):
    randomgenerator = random.random()
    dateformat = "%d/%m/%Y"
#This is essential because you need to specify the format the date is in, order to conver it into time
    start = time.mktime(time.strptime(startdate, dateformat))
    #time.mktime converts converts time to seconds and time.strptime converts date into time
    end = time.mktime(time.strptime(enddate, dateformat))

    randomtime = start + randomgenerator * (end - start)

    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    #time.strftime converts time into dates and time.localtime converts seconds into time

    return randomdate

print(randomdate(startdate, enddate))