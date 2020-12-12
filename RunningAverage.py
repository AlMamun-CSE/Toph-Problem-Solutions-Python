N = int(input())
li = list(map(int, input().strip().split()))[:N]
for i in range(N):
    a = sum(li[:i + 1]) / (i + 1)
    print(a)
