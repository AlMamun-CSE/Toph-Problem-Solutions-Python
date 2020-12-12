li = []
A = input().capitalize()

for i in A:
    if i == 's':
        i = '$'
    if i == 'i':
        i = '!'
    if i == 'o':
        i = '()'
    li.append(i)

for j in li:
    print(j, end='')
print('.')
