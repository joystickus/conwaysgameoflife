col,row = 10,10
table = [[0 for y in range(col)] for x in range(row)]
dot1 = [3, 4]
dot2 = [4, 4]
dot3 = [5, 4]
pattern = [dot1, dot2, dot3]
for dot in pattern:
    table [dot[0]] [dot[1]] = 1

for i in range(row):
    print(table[i])

def check(y,x):
    count = 0
    result = ""
    for i in range(-1,2):
        for j in range(-1,2):
            if table[y+i][x+j] == 1:
                count += 1
    if table[y][x] == 1:
        count -= 1
    if table[y][x] == 1 and (count > 3 or count < 2):
        result = "die"
    elif table[y][x] == 0 and count == 3:
        result = "born"
    return result

die = []
born = []
for dot in pattern:
    if check(dot[0],dot[1]) == "die":
        die.append(dot)
    for i in range(-1,2):
        for j in range(-1,2):
            dotx = dot[0]+i,dot[1]+j
            if check(dotx[0],dotx[1]) == "born":
                born.append(list(dotx))
for dot in die:
    table [dot[0]] [dot[1]] = 0
    if dot in pattern:
        pattern.remove(dot)
for dot in born:
    table [dot[0]] [dot[1]] = 1
    pattern.append(dot)
print()
for i in range(row):
    print(table[i])

die = []
born = []
for dot in pattern:
    if check(dot[0],dot[1]) == "die":
        die.append(dot)
    for i in range(-1,2):
        for j in range(-1,2):
            dotx = dot[0]+i,dot[1]+j
            if check(dotx[0],dotx[1]) == "born":
                born.append(list(dotx))
for dot in die:
    table [dot[0]] [dot[1]] = 0
    if dot in pattern:
        pattern.remove(dot)
for dot in born:
    table [dot[0]] [dot[1]] = 1
    pattern.append(dot)

print()
for i in range(row):
    print(table[i])
