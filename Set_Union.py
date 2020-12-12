a, b = map(int, input().split())
arr1 = set(list(map(int, input().split()))[:a])
arr2 = set(list(map(int, input().split()))[:b])
z = arr1 | arr2
print(' '.join(map(str, sorted(z))))
