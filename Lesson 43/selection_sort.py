def selection(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
        
    return a
    
a = [43,67,33,24,77,84,12]
print(selection(a))
