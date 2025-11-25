class DATA:
    def __init__(self,index,value,count=0):
        self.index = index
        self.value = value
        self.count = count
    
def sortbyfrequencyandindex(a):
    if a is None or len(a) < 2:
        return
    hm = {}

    for i in range(len(a)):
        hm.setdefault(a[i], DATA(a[i],i)).count += 1

    values = [*hm.values()]
    values.sort(key = lambda x : (-x.count,x.index))
    k = 0

    for i in values:
        for j in range(i.count):
            a[k] = i.value
            k+=1


if __name__ == "__main__":
    a = [0,3,4,2,2,4,6,6,7,3,4,4,0]
    print(a)
    sortbyfrequencyandindex(a)
    print(a)


    

