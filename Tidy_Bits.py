a = int(input())
b = str(bin(a))
# print(b)
c = b[2:]
# print(c)
d = c.replace("0", "")
# print(d)
e = int(d, 2)
print(e)