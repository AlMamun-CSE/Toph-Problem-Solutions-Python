n, index1, index2 = map(int, input().split())
li = list(map(int, input().split()))[:n]
add = 0
for i in range(index1, index2+1):
    add = add + li[i]
print(add)