s = '1213'
lst = []
for charecter in s:
    lst.append(charecter)
print(max(lst, key=lst.count))

print(lst.count('1'))
