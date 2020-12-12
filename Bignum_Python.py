base = 2 ** 30


def add(x, y):
    # making sure x is larger than y
    if len(x) < len(y):
        x, y = y, x

    # result list is one digit longer than x
    z = [0] * (len(x) + 1)
    carry = 0
    i = 0
    while i < len(y):
        total = x[i] + y[i] + carry
        z[i] = total % base
        carry = total // base
        i += 1

    while i < len(x):
        total = x[i] + carry
        z[i] = total % base
        carry = total // base
        i += 1

    z[i] = carry
    # removing leading 0's.
    if z[i] == 0:
        z = z[:-1]

    return z


a, b = list(map(str, input().split()))
add(a, b)