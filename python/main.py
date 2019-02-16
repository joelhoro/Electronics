from screen import Screen
from joystick import JoyStick
from servo import Servo
import math, time

def are_equal(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True        

class Robot():
    speeds = [1,5,10,50]
    def __init__(self):
        self.speed = 5

    def toggleSpeed(self):
        idx = ( Robot.speeds.index(self.speed) + 1 ) % len(Robot.speeds)
        print("Setting speed to %s" % self.speed)
        self.speed = Robot.speeds[idx]


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

servos = [Servo(channel) for channel in [0,1,2,3]]
joyStick = JoyStick(1,JoyStick.Address_Ox48,[1,0],4)
joyStick2 = JoyStick(1,JoyStick.Address_Ox48,[3,2],17)



robot = Robot()

for servo in servos:
    servo.set_angle(90)

def applyPosition(servo, joyStick, axis, multiplier=1):
    position = joyStick.last_position[axis]
    threshhold = 0.11
    if position > threshhold or position < -threshhold:
        servo.set_angle(servo.angle + robot.speed*multiplier*position)
        return True
    return False

previous_position = []
i = 0

showDisplay = False

def toggleDisplay():
    global showDisplay
    showDisplay = not showDisplay
    print("Toggling display to %s" % showDisplay)
    if not showDisplay:
        screen.clear()


position = joyStick.position()
position2 = joyStick2.position()

start = time.time()
showDisplay=True
print("Starting")

while i<50:#True:
    position = joyStick.position()
    position2 = joyStick2.position()
    if True:# not are_equal(position, previous_position):
        moved = applyPosition(servos[0],joyStick,1)
        moved = moved or applyPosition(servos[1],joyStick,0, -1)
        moved = moved or applyPosition(servos[2],joyStick2,0,10)
        moved = moved or applyPosition(servos[3],joyStick2,1)

        if joyStick2.last_position[-1]:
            toggleDisplay()
        elif joyStick.last_position[-1]:
            robot.toggleSpeed()
        #print(position)
        if not(i % 5) and showDisplay:
            draw = screen.drawer()
            drawCircle(draw,(20,20),20,position)
            drawCircle(draw,(80,20),20,position2)
            draw.text((10,50), '# %s' % i, fill=255)
            draw.text((70,50), 'Speed=%s' % robot.speed, fill=255)
            screen.display()
        
    i += 1
#    print(".", end='', flush=True),
    #print('*' * int(position[0]/1000))

    #previous_position = position


    #time.sleep(0.5)

end = time.time()
print(end - start)
