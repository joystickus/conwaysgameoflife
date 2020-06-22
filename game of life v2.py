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
for i in range(len(pattern)):
    table [pattern[i][0]] [pattern[i][1]] = 1

# Show the pattern in the field.
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
    for i in range(len(pattern)):
        patternRows.append(pattern[i][0])
        patternColumns.append(pattern[i][1])
        topEdge = min(patternRows)
        bottomEdge = max(patternRows)
        leftEdge = min(patternColumns)
        rightEdge = max(patternColumns)
    edgesCoordinates = topEdge, bottomEdge, leftEdge, rightEdge
    return edgesCoordinates

# Function to check a cell.
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

# Function to check the dots of the pattern for changes
def checkPattern(rowDotPlace,colDotPlace):


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

# Center the pattern in the field.
edges = calcEdges() # get the edges of the pattern
mx = int(col / 2 - 0.5) # calculate the center of the matrix
my = int(row / 2 - 0.5)
py = int((edges[0] + edges[1]) / 2) # calculate the center of the pattern
px = int((edges[2] + edges[3]) / 2)
moveY = my - py # calculate the distance to move the pattern to the center
moveX = mx - px
for i in range(len(pattern)): # move the pattern to the center
    pattern[i][0] += moveY
    pattern[i][1] += moveX
# flush and redraw the field
table = [[0 for y in range(col)] for x in range(row)]
for i in range(len(pattern)):
    table [pattern[i][0]] [pattern[i][1]] = 1

print()
for i in range(row):
    print(table[i])

# Give it a try
for i in range(10):
    checkMatrix()
    time.sleep(0.3)
    print()
    for j in range(row):
        print(table[j])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
