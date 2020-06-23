# This time I'll try a matrix.

import time, pygame

pygame.init()

baseCol,baseRow = 20, 15

# Create a matrix.
multiplier = 0 # This number means the scale of the matrix: 0,1,2,3 = 20x15,40x30,80x60,160x120.
               # It will be changed by the user and depending on the visibility of the pattern.
col,row = baseCol*(2**multiplier),baseRow*(2**multiplier)
table = [[0 for y in range(col)] for x in range(row)]

# Open a white board window based on the matrix.
screen = pygame.display.set_mode([800,600])
screen.fill([255,255,255])
for i in range(col):
    pygame.draw.line(screen, [0,0,0], [i*int(800/col), 0], [i*int(800/col), 600], 1)
for i in range(row):
    pygame.draw.line(screen, [0,0,0], [0, i*int(600/row)], [800, i*int(600/row)], 1)
pygame.display.flip()

# Input the pattern.
# In the future it will be done by the mouse clicks in the field.
dot1 = [1, 1]
dot2 = [1, 2]
dot3 = [1, 3]
dot4 = [1, 4]
dot5 = [1, 5]
pattern = [dot1, dot2, dot3, dot4, dot5]
for dot in pattern:
    table [dot[0]] [dot[1]] = 1

# Show the field with pattern in it.
for i in range(row):
    print(table[i])

# Function to calculate the coordinates of the edges of the pattern.
def calcEdges():
    topEdge = 0
    bottomEdge = 0
    leftEdge = 0
    rightEdge = 0
    patternColumns = []
    patternRows = []
    for i in pattern:
        patternRows.append(i[0])
        patternColumns.append(i[1])
        topEdge = min(patternRows)
        bottomEdge = max(patternRows)
        leftEdge = min(patternColumns)
        rightEdge = max(patternColumns)
    edgesCoordinates = topEdge, bottomEdge, leftEdge, rightEdge
    return edgesCoordinates

# Function to check a cell.
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

# Function to make a move.
def move():
    die = []
    born = []
    for dot in pattern:
        if check(dot[0], dot[1]) == "die":
            die.append(dot)
        for i in range(-1, 2):
            for j in range(-1, 2):
                dotx = dot[0] + i, dot[1] + j
                if check(dotx[0], dotx[1]) == "born":
                    born.append(list(dotx))
    for dot in die:
        table[dot[0]][dot[1]] = 0
        if dot in pattern:
            pattern.remove(dot)
    for dot in born:
        table[dot[0]][dot[1]] = 1
        pattern.append(dot)
    print()
    for i in range(row):
        print(table[i])

# Center the pattern in the field.
edges = calcEdges() # get the edges of the pattern
mx = int(col / 2 - 0.5) # calculate the center of the matrix
my = int(row / 2 - 0.5)
py = int((edges[0] + edges[1]) / 2) # calculate the center of the pattern
px = int((edges[2] + edges[3]) / 2)
moveY = my - py # calculate the distance to move the pattern to the center
moveX = mx - px
for dot in pattern: # move the pattern to the center
    dot[0] += moveY
    dot[1] += moveX
# flush and redraw the field
table = [[0 for y in range(col)] for x in range(row)]
for i in pattern:
    table [i[0]] [i[1]] = 1
for i in range(row):
    print(table[i])

# Give it a try
for i in range(10):
    time.sleep(0.3)
    move()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
