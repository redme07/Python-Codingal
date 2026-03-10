def itemprice(barcode):
    
    empty = []
    for i in barcode:
        n = ord(i)
        if n // 10:
            max = 0
            while n>0:
                if n%10 > max:
                    max = n%10

                n = n//10
            empty.append(max)
        else:
            empty.append(n)
    
    return sum(empty)
barcode = input("enter a barcode: ")
print(itemprice(barcode))