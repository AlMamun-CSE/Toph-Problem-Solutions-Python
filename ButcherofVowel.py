T = int(input())
li = [0]*T
list1 = ["a","e","i","o","u"]
for i in range(T):
    name = input()
    namelower = name.lower()
    li[i] = namelower

for char in li:
    for i in range(0, len(char)):
        if char[i] in list1:
            print("Yes")
            break
    else:
        print("No")