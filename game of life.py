# Надо еще сделать масштабирование по результатам проверки вылезания за пределы поля. Но для этого надо будет
# переделывать всю логику программы. А я уже топчусь на месте. Когда разберусь с питоном больше,
# тогда и переделаю. Плюс надо будет изменить на работу с точками как с объектами и добавить обратную связь с
# пользователем (кнопки, масштабирование колесом, замедление/ускорение, паузу и перемотку назад/вперед). Возможно,
# перейти на другой модуль, чтобы интерфейс был лучше. Или нарисовать свой. Пока не умею, как.

import pygame, time, easygui
from copy import copy

pygame.init()

# offer user to choose resolution of the window
resolutions = {'640 × 480': [640, 480],
               '800 × 600': [800, 600],
               '1024 × 768': [1024, 768],
               '1280 × 1024': [1280, 1024],
               '1440 × 900': [1440, 900],
               '1680 × 1050': [1680, 1050],
               '1920 × 1080': [1920, 1080],
               '2560 × 1440': [2560, 1440]}
resolution_choice = easygui.choicebox("Please select resolution", choices = resolutions.keys(), preselect = 1)
resolution = resolution_x, resolution_y = resolutions[resolution_choice]
screen = pygame.display.set_mode(resolution)
screen.fill([255, 255, 255])

# resolution_x = resolution[0]
# resolution_y = resolution[1]

cell_size = 40
cell_size_work = copy(cell_size)

field0 = int(cell_size_work / 2)
step = cell_size_work
center_field_x = field0 + step * (int(resolution_x / step / 2) - 1)
center_field_y = field0 + step * (int(resolution_y / step / 2) - 1)
dot_radius = int((cell_size_work / 2) * 0.7)

# function to scale the field down
def scale():
    new_cell_size = int(resolution_x / (int(resolution_x / cell_size_work) + 2))
    return new_cell_size

# function to check a cell to change state
def check(x, y):
    dots = {"dot_top_left": [x - step, y - step],
            "dot_top_center": [x, y - step],
            "dot_top_right": [x + step, y - step],
            "dot_center_left": [x - step, y],
            "dot_center_right": [x + step, y],
            "dot_bottom_left": [x - step, y + step],
            "dot_bottom_center": [x, y + step],
            "dot_bottom_right": [x + step, y + step]}
    count = 0
    center = False
    future = ""
    if screen.get_at([x, y]) == (0, 0, 0, 255):
        center = True
    for value in dots.values():
        if screen.get_at(value) == (0, 0, 0, 255):
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

# function to check borders
def border_check():
    top_left_starting_point = field0 + step
    top_rignt_starting_point = top_left_starting_point + (step * (int(resolution_x / cell_size_work) - 3))
    bottom_left_starting_point = top_left_starting_point + (step * (int(resolution_y / cell_size_work) - 3))
    presence = False
    while not presence:
        for i in range(0, int(resolution_x / step - 3)):
            dot_place = [top_left_starting_point + i * step, top_left_starting_point]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(0, int(resolution_y / step - 3)):
            dot_place = [top_left_starting_point, top_left_starting_point + i * step]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(0, int(resolution_y / step - 3)):
            dot_place = [top_rignt_starting_point, field0 + step + i * step]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(0, int(resolution_x / step - 3)):
            dot_place = [field0 + step + i * step, bottom_left_starting_point]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
    return "yes" # temporary return, I'll think on it more.

# draw the field
for i in range(0, resolution_x, step):
    pygame.draw.lines(screen, [0, 0, 0], False, [[i, 0], [i, resolution_y]], 1)
    pygame.draw.lines(screen, [0, 0, 0], False, [[0, i], [resolution_x, i]], 1)

pygame.display.flip()

# dot0 = [center_field_x + step * 0, center_field_y + step * 0]
# dot1 = [center_field_x + step * 0, center_field_y - step * 1]
# dot2 = [center_field_x + step * 1, center_field_y - step * 1]
# dot3 = [center_field_x - step * 1, center_field_y + step * 0]
# dot4 = [center_field_x + step * 0, center_field_y + step * 1]
#
# r_pentomino = [dot0, dot1, dot2, dot3, dot4]
#
# for i in r_pentomino:
#     pygame.draw.circle(screen, [0, 0, 0], i, 15, 0)

dot1 = [field0 + step * 2, field0 + step * 1]
dot2 = [field0 + step * 3, field0 + step * 2]
dot3 = [field0 + step * 3, field0 + step * 3]
dot4 = [field0 + step * 2, field0 + step * 3]
dot5 = [field0 + step * 1, field0 + step * 3]
glider = [dot1, dot2, dot3, dot4, dot5]

for i in glider:
    pygame.draw.circle(screen, [0, 0, 0], i, dot_radius, 0)

pygame.display.flip()

time.sleep(1)
for k in range(20):
    born = []
    die = []
    time.sleep(0.1)
    starting_point = field0 + step
    for i in range(int(resolution_x / step - 2)):
        for j in range(int(resolution_y / step - 2)):
            dot_place = [starting_point + i * step, starting_point + j * step]
            result = check(*dot_place)
            if result == "born":
                born.append(dot_place)
            elif result == "die":
                die.append(dot_place)
    for i in born:
        pygame.draw.circle(screen, [0, 0, 0], i, dot_radius, 0)
    for i in die:
        pygame.draw.circle(screen, [255, 255, 255], i, dot_radius, 0)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
