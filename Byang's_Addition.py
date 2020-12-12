x = input()

m, n = x.split()

a = list(m)
b = list(n)

a = a[::-1]
b = b[::-1]

count = 0

if len(a) >= len(b):
    n = len(b)
else:
    n = len(a)

for i in range(0, n):
    sum = int(a[i]) + int(b[i])
    if sum > 9:
        count = count + 1
        sum = 0

if count != 0:
    print("Yes")
else:
    print("No")