t = int(input())
for i in range(t):
    s = input()
    count = 0
    over = 0
    ball = 0
    for j in range(len(s)):
        if s[j] != 'N' and s[j] != 'W' and s[j] != 'D':
            count += 1
    ball = count % 6
    over = count // 6
    if ball == 0 and over != 0:
        if over > 1:
            print("%d" % over, "OVERS")
        else:
            print("%d" % over, "OVER")
    elif over == 0 and ball != 0:
        if ball > 1:
            print("%d" % ball, "BALLS")
        else:
            print("%d" % ball, "BALL")

    else:
        if over > 1 and ball > 1:
            print("%d" % over, "OVERS", "%d" % ball, "BALLS")
        else:
            print("%d" % over, "OVER", "%d" % ball, "BALL")

