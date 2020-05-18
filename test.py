import easygui

# offer user to choose resolution of the window
resolution_x = 0
resolution_y = 0
resolution_choices = ['640 × 480', '800 × 600', '1024 × 768', '1280 × 1024', '1440 × 900', '1680 × 1050',
                      '1920 × 1080', '2560 × 1440']
resolution_choice = easygui.choicebox("Please select resolution", choices = resolution_choices, preselect = 1)
if resolution_choice == '640 × 480':
    resolution_x = 640
    resolution_y = 480
elif resolution_choice == '800 × 600':
    resolution_x = 800
    resolution_y = 600
elif resolution_choice == '1024 × 768':
    resolution_x = 1024
    resolution_y = 768
elif resolution_choice == '1280 × 1024':
    resolution_x = 1280
    resolution_y = 1024
elif resolution_choice == '1440 × 900':
    resolution_x = 1440
    resolution_y = 900
elif resolution_choice == '1680 × 1050':
    resolution_x = 1680
    resolution_y = 1050
elif resolution_choice == '1920 × 1080':
    resolution_x = 1920
    resolution_y = 1080
elif resolution_choice == '2560 × 1440':
    resolution_x = 2560
    resolution_y = 1440
screen = pygame.display.set_mode([resolution_x, resolution_y])
screen.fill([255, 255, 255])