def calculateSum(n):
    # Initialize sum with 0
    summ = 0

    # Loop to calculate power of 2
    # upto n and add them
    for row in range(n-1):
        summ = summ + (1 << row)

    return summ+1


n = int(input())
print(calculateSum(n))