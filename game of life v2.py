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
pattern = [] # Empty container for for pattern.

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

# Function to get the mouse clicks.
def click(eventPos):
    y, x = int(eventPos[1] / cellSize), int(eventPos[0] / cellSize)
    if matrix[y][x] == 0:
        matrix[y][x] = 1
        Dot1(y,x)
        pattern.append([y,x])
        pygame.display.flip()
    elif matrix[y][x] == 1:
        matrix[y][x] = 0
        Dot0(y,x)
        pattern.remove([y,x])
        pygame.display.flip()

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

# Input the pattern.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

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
# Flush and redraw the field. And pause.
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
time.sleep(1)

# It'll work until the window is X-button closed.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()
            print("frame rate =", frame_rate)
    clock.tick(10)
    move()
pygame.quit()
