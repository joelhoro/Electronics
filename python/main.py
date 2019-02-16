from screen import Screen
from joystick import JoyStick
import math, time

def are_equal(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True        

joyStick = JoyStick(JoyStick.Address_Ox48,[1,0],4)
joyStick2 = JoyStick(JoyStick.Address_Ox48,[3,2],17)

def drawCircle(draw,center,radius,coordinates):
    #draw.ellipse((0,50),10,100),outline=255,fill=255)
    rescale = math.sqrt(coordinates[0]*coordinates[0]+coordinates[1]*coordinates[1])
    draw.ellipse((center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius), outline=255, fill=255*coordinates[2])
#    draw.ellipse((center[0]-rescale*radius, center[1]-rescale*radius, center[0]+rescale*radius, center[1]+rescale*radius), outline=255, fill=0)
#    draw.line((center, (center[0]+coordinates[0]*radius/rescale,center[1]-coordinates[1]*radius/rescale)), fill=255)
#    print(coordinates)
    circleCenter = (center[0]+coordinates[0]*radius/2, center[1]-coordinates[1]*radius/2)
    smallRadius = radius / 3.0
    draw.ellipse((circleCenter[0]-smallRadius,circleCenter[1]-smallRadius,circleCenter[0]+smallRadius,circleCenter[1]+smallRadius), outline=255)
    #draw.ellipse((center[0]+coordinates[0]*radius/rescale,center[1]-coordinates[1]*radius/rescale)), fill=255)

screen = Screen()

previous_position = []
i = 0
while True:
    position = joyStick.position()
    #position2 = joyStick2.position()
    if False:# not are_equal(position, previous_position):
        #print(position)
        draw = screen.drawer()
        drawCircle(draw,(20,20),20,position)
        drawCircle(draw,(80,20),20,position2)
        #drawCircle(draw,(80,20),10,position)
        #drawCircle(draw,(20,50),10,position)
        #drawCircle(draw,(50,50),10,position)
        draw.text((80,50), str(i), fill=255)
        screen.display()
    i += 1
    print(".", end='', flush=True),

    #previous_position = position


    #time.sleep(0.5)
