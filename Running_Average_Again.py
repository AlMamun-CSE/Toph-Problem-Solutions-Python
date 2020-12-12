n = int(input())
li = list(map(int, input().strip().split()))[:n]
add = 0
j = 1
avg = 0
for i in range(n):
    add += li[i]
    avg = add/j
    j += 1
    print(avg)
