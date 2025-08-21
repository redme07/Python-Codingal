tuple1 = ("Hello", 2, 2.5, False)
print(tuple1)

tuple2 = (2, 3, 4, 5, 6, 7, 2, 4)
tuple2 = tuple2 + (9, 7)
print(tuple2)

tuple3 = (2, 3, 3, 4, 3, 3, 3, 3, 5, 6, 1, 3)
count = tuple3.count(3)
print(count)

tuple4 = (2, 5, 3, 4, 5, 3, 5, 6, 1, 4)
slice1 = tuple4[3:6]
print(slice1)
slice2 = tuple4[:7]
print(slice2)