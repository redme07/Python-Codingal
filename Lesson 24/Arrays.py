import array as arr

arraynum = arr.array("i", (1,2,3,4,5,6,7,7,2,2,2,2,2,2,2,))
#This is how u make an array arrays cannot have chracters and you have to 
# specify data type befor i is for integer and f is for float

print(arraynum)

print("The number of 2 in arraynum are", arraynum.count(2))

arraynum.reverse()

print(arraynum)