def leap_year(y):
    if y % 4 == 0 and y % 400 != 0:
        print("Yes")
    else:
        print("No")


Y = int(input())
leap_year(Y)
