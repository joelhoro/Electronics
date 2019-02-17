import math
from screen import Screen
screen = Screen()


t = 0
center = [50,50]
while True:

    draw = screen.drawer()

    t += math.pi / 10
    r = abs(math.sin(t)*10)

    center[0] += 5
    if center[0]>128:
        center[0] = 0
    center[1] = 30 + math.sin(t)*10
    draw.ellipse((center[0]-r,center[1]-r,center[0]+r,center[1]+r), outline=255, fill = 255)

    screen.display()