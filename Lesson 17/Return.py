def maxdigit(n):

    maxd = 0

    while n>0:

        digit = n % 10

        if digit > maxd:
            maxd = digit

        if maxd == 9:
            return 9
        
        n = n // 10

    return maxd

print(maxdigit(1239))