def calculate(a,a_size):
    profit = 0
    loss = 0
    for i in range(1,a_size):
        if a[i]>a[i-1]:
            profit += a[i]-a[i-1]
        else:
            loss += a[i-1]-a[i]
    return loss,profit

a = (20,50,10,40,20,30,25,74)
a_size = len(a)

print(calculate(a,a_size))