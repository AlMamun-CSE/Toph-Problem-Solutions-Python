length, breadth = map(int, input().split())
field = []
free_spots = 0
for i in range(length):
    row = input()
    field.append(row)
    for i in field:
        for j in i:
# for the middle ones
            if length > field.index(i) >= 1 and breadth > i.index(j) >= 1:
                if i[i.index(j) - 1] == ‘.’ and i[i.index(j) + 1] == ‘.’ and field[field.index(i) + 1][i.index(j)] == ‘.’ and field[field.index(i) - 1][i.index(j)] == ‘.’:
                    free_spots += 1

    # for the top left corner
             elif field.index(i) == 0 and i.index(j) == 0:
        if i[i.index(j) + 1] == '.' and field[field.index(i) + 1][i.index(j)] == '.':
            free_spots += 1

    # for the bottom right corner
    elif field.index(i) == length and i.index(j) == breadth:
        if i[i.index(j) - 1] == '.' and field[field.index(i) - 1][i.index(j)] == '.':
            free_spots += 1

    # for the top right corner
    if field.index(i) == 0 and i.index(j) == breadth:
        if i[i.index(j) - 1] == '.' and field[field.index(i) + 1][i.index(j)] == '.':
            free_spots += 1

    # for the bottom left corner
    if field.index(i) == length and i.index(j) == 0:
        if i[i.index(j) + 1] == '.' and field[field.index(i) - 1][i.index(j)] == '.':
            free_spots += 1

    # for the top side
    elif field.index(i) == 0 and breadth > i.index(j) >= 1:
        if i[i.index(j) - 1] == '.' and i[i.index(j) + 1] == '.' and field[field.index(i) + 1][i.index(j)] == '.':
            free_spots += 1

    # for the bottom side
    elif field.index(i) == length and 1 <= i.index(j) < breadth:
        if i[i.index(j) - 1] == '.' and i[i.index(j) + 1] == '.' and field[field.index(i) - 1][i.index(j)] == '.':
            free_spots += 1

    # for the right side
    elif length > field.index(i) >= 1 and i.index(j) == breadth:
        if i[i.index(j) - 1] == '.' and field[field.index(i) + 1][i.index(j)] == '.' and field[field.index(i) - 1][i.index(j)] == '.':
            free_spots += 1

print(free_spots)