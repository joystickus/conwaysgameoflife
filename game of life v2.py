# This time I'll try a matrix.

import time

# Create a matrix.
col,row = 30,30
table = [[0 for y in range(col)] for x in range(row)]
# Show an empty matrix.
for i in range(row):
    print(table[i])

# Function to check a cell to change state.
def check(rowDotPlace,colDotPlace):
    neighbours = {"top": table [rowDotPlace-1] [colDotPlace],
                "bottom": table [rowDotPlace+1] [colDotPlace],
                "left": table [rowDotPlace] [colDotPlace-1],
                "right": table [rowDotPlace] [colDotPlace+1],
                "topLeft": table [rowDotPlace-1] [colDotPlace-1],
                "topRight": table [rowDotPlace-1] [colDotPlace+1],
                "bottomLeft": table [rowDotPlace+1] [colDotPlace-1],
                "bottomRight": table [rowDotPlace+1] [colDotPlace+1]}
    count = 0
    center = False
    future = ""
    if table [rowDotPlace] [colDotPlace] == 1:
        center = True
    for value in neighbours.values():
        if value == 1:
            count += 1
    if center and 2 <= count <= 3:
        future = "live"
    elif center and (count < 2 or count > 3):
        future = "die"
    elif not center and count == 3:
        future = "born"
    else:
        future = "nothing"
    return future

# Function to check the whole matrix and change its state.
def checkMatrix():
    born = []
    die = []
    for i in range(1, row-1):
        for j in range(1, col-1):
            result = check(i,j)
            if result == "born":
                born.append([i,j])
            elif result == "die":
                die.append([i,j])
    for i in range(len(born)):
        table [born[i][0]] [born[i][1]] = 1
    for i in range(len(die)):
        table [die[i][0]] [die[i][1]] = 0

# Calculate the center of the matrix.
x = int(col / 2 - 0.5)
y = int(row / 2 - 0.5)

# Draw an example pattern.
table [y] [x] = 1
table [y] [x-1] = 1
table [y] [x-2] = 1
table [y] [x-3] = 1
table [y] [x-4] = 1
table [y] [x+1] = 1
table [y] [x+2] = 1
table [y] [x+3] = 1
table [y] [x+4] = 1
table [y] [x+5] = 1

# Give a pause and show the renewed matrix.
# time.sleep(1)
# print()
# for i in range(row):
#     print(table[i])

# Lists of dots
live = []
born = []
die = []

# Give it a try
for i in range(30):
    checkMatrix()
    time.sleep(1)
    print()
    for j in range(row):
        print(table[j])
