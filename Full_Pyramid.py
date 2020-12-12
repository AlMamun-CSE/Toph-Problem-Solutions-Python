# a = int(input())
# for i in range(1, a + 1):
#     for j in range(0, a - i):
#         print(" ", end='')
#     for j in range(1, i + 1):
#         print("*", end='')
#     print()

a = int(input())
for i in range(a):
    for j in range(a - i - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end='')
        if j < i:
            print(' ', end='')
    print()
