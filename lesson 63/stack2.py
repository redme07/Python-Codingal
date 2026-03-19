
def calculate(price, s):
    n = len(s)
    stack = []
    stack.append(0)
    s[0] = 1
    for i in range(1,n):
        while len(stack) > 0 and price[stack[-1]] <= price[i]:
            stack.pop()
        s[i] = i + 1 if len(stack) == 0   else i - stack[-1]
        stack.append(i)
        return s

def print_arr(arr,size):
    for i in range(size):
        print(arr[i],end=" ")

price = [10, 4, 5, 90, 120, 80]
s = [0 for i in range(len(price)+1)]
s = calculate(price, s)
print_arr(s, len(s))