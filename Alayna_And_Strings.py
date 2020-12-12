# s = input()
# print(sum(1 for c in s if c.isupper()), "", sum(1 for c in s if c.islower()))
string = input()
count1 = 0
count2 = 0
for i in string:
    if i.islower():
        count1 = count1 + 1
    elif i.isupper():
        count2 = count2 + 1

print(count2, count1)
