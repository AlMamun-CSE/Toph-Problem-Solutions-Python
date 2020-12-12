a, b = map(int, input().split())
mat = []
for i in range(1, a, 1):
    for j in range(1, b, 1):
        mat[i][j] = input().split()
for i in range(1, a, 1):
    for j in range(1, b, 1):
        ans = 0
        if mat[i][j] == '.':
            if mat[i][j - 1] == '*':
                ans = ans + 1
            if mat[i - 1][j - 1] == '*':
                ans = ans + 1
            if mat[i - 1][j] == '*':
                ans = ans + 1
            if mat[i - 1][j + 1] == '*':
                ans = ans + 1
            if mat[i][j + 1] == '*':
                ans = ans + 1
            if mat[i + 1][j + 1] == '*':
                ans = ans + 1
            if mat[i + 1][j] == '*':
                ans = ans + 1
            if mat[i + 1][j - 1] == '*':
                ans = ans + 1
            if ans > 0:
                mat[i][j] = '0' + str(ans)

for i in range(1, a, 1):
    for j in range(1, b, 1):
        print(mat[i][j])

