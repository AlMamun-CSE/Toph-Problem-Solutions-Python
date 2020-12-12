s = input()
arr = list(s)
count1 = 0
count2 = 0
for i in range(len(arr)):
    if arr[i] == '(':
        count1 += 1
    if arr[i] == ')':
        count2 += 1
if count2 == count1:
    print("Yes")
else:
    print("No")