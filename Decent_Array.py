input()
A = input()
A1 = A.split()
a = int(A1[0])
for i in A1:
    x = int(i)
    if x >= a:
        a = x
        bul = True
    else:
        bul = False
        break
if bul:
    print("Yes")
else:
    print("No")
