def fibonacci_number(n):
    F1 = 1
    F2 = 1
    if n == 1:
        return 1
    else:
        for i in range(n-2):
            result = F1 + F2
            F1 = F2
            F2 = result

    return result


N = int(input())
print(fibonacci_number(N))
