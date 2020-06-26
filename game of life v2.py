# This is the second version of the Conway's Game of Life. This time I'll try a matrix.
# Still have to make buttons to control and think of what to do when it reaches edges of the field.
# And it all of a sudden froze. Don't yet know what to do with that. :( -- Solved the problem getting back to
# matrix-check not pattern-check.

import time, pygame
pygame.init()
clock = pygame.time.Clock()

# Create a matrix.
baseCol,baseRow = 20, 15
multiplier = 1 # This number means the scale of the matrix: 0,1,2,3 = 20x15,40x30,80x60,160x120.
               # It will be changed by the user and depending on the visibility of the pattern.
col,row = baseCol*(2**multiplier),baseRow*(2**multiplier)
matrix = [[0 for y in range(col)] for x in range(row)]

# Prepare the field.
screen = pygame.display.set_mode([800,600])
cellSize = 800/col
dotRadius = int(cellSize/2*0.8)
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
screen.blit(background, (0,0))
for i in range(col):
    pygame.draw.line(screen, [0,0,0], [i*int(800/col), 0], [i*int(800/col), 600], 1)
for i in range(row):
    pygame.draw.line(screen, [0,0,0], [0, i*int(600/row)], [800, i*int(600/row)], 1)
pygame.display.flip()

# Classes for "born" and "die".
class Dot1:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        dotPlace = [int(x * cellSize + cellSize / 2), int(y * cellSize + cellSize / 2)]
        pygame.draw.circle(screen, [0, 0, 0], dotPlace, dotRadius, 0)
class Dot0:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        dotPlace = [int(x * cellSize + cellSize / 2), int(y * cellSize + cellSize / 2)]
        pygame.draw.circle(screen, [255, 255, 255], dotPlace, dotRadius, 0)

# Function to check a cell.
def check(y,x):
    count = 0
    result = ""
    for i in range(-1,2):
        for j in range(-1,2):
            if matrix[y+i][x+j] == 1:
                count += 1
    if matrix[y][x] == 1:
        count -= 1
    if matrix[y][x] == 1 and (count < 2 or count > 3):
        result = "die"
    elif matrix[y][x] == 0 and count == 3:
        result = "born"
    return result

# Function to make a move.
def move():
    die = []
    born = []
    for i in range(1, row-1):
        for j in range(1, col-1):
            if check(i,j) == "die":
                die.append([i,j])
            elif check(i,j) == "born":
                born.append([i,j])
    for i in die:
        matrix[i[0]][i[1]] = 0
        Dot0(i[0],i[1])
    for i in born:
        matrix[i[0]][i[1]] = 1
        Dot1(i[0],i[1])
    pygame.display.flip()

# Input the pattern.
# In the future it will be done by the mouse clicks in the field.
dot1 = [1, 1]
dot2 = [1, 2]
dot3 = [1, 3]
dot4 = [1, 4]
dot5 = [1, 5]
dot6 = [1, 6]
dot7 = [1, 7]
dot8 = [1, 8]
dot9 = [1, 9]
dot10 = [1, 10]
pattern = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10]
# pattern = [dot1, dot2, dot3, dot4, dot5]
for i in pattern:
    matrix[i[0]][i[1]] = 1
    Dot1(i[0], i[1])
pygame.display.flip()
print()
for i in range(row):
    print(matrix[i])

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
# pause, flush and redraw the field
clock.tick(1)
matrix = [[0 for y in range(col)] for x in range(row)]
screen.blit(background, (0,0))
for i in range(col):
    pygame.draw.line(screen, [0,0,0], [i*int(800/col), 0], [i*int(800/col), 600], 1)
for i in range(row):
    pygame.draw.line(screen, [0,0,0], [0, i*int(600/row)], [800, i*int(600/row)], 1)
for i in pattern:
    matrix[i[0]][i[1]] = 1
    Dot1(i[0], i[1])
pygame.display.flip()
print()
for i in range(row):
    print(matrix[i])

# Give it a try
for i in range(30):
    clock.tick(3)
    move()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()
            print("frame rate =", frame_rate)
pygame.quit()
