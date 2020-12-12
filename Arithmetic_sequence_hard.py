n = int(input())
sum_of_n = n * (n + 1) // 2
m = int(input())
sub = 0
for i in range(m):
    x = int(input())
    sub += x
print(sum_of_n - sub)