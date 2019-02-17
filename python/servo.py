from __future__ import division
import time

import Adafruit_PCA9685

class Servo():

    class_initialized = False
    @staticmethod
    def initialize_pwm():
        if Servo.class_initialized:
            return
        print("Initializing PCA9685 Servo controller... ", end='')

        try:
            pwm = Adafruit_PCA9685.PCA9685()
            print("done")
        except:
            print("failed")
            raise Exception("Error initializing - the device is probably not connected")

        Servo.servo_min, Servo.servo_max = [4096 * x for x in [0.02, 0.12]]
        
        # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)
        Servo.pwm = pwm

    def __init__(self,channel):
        Servo.initialize_pwm()
        self.channel = channel
        self.angle = 0
        self.alpha = 2
        self.timePer180 = 5
        self.interval = 0.025

    # go to a given angle directly    
    def set_angle(self,angle):
        angle = max(0,min(angle,180))
        pulse = Servo.servo_min + (Servo.servo_max-Servo.servo_min)/180.0 * angle
        Servo.pwm.set_pwm(self.channel, 0, int(pulse))
        self.angle = angle
    
    def _smoothing(self,x):
        return pow(x,self.alpha) / (pow(x,self.alpha) + pow(1-x,self.alpha))

    def __del__(self):
        Servo.pwm.set_pwm(self.channel,0,0)
    # go to a given angle in a smooth way
    def go_to_angle(self,angle):
        distance = angle-self.angle
        targetTime = abs(distance)/180.0*self.timePer180
        numberOfIntervals = int(targetTime/self.interval)
        initial_angle = self.angle
        for i in range(numberOfIntervals):
            smoothed = numberOfIntervals * self._smoothing(i / numberOfIntervals)
            #print(smoothed / numberOfIntervals)
            self.set_angle(initial_angle + smoothed * distance / numberOfIntervals)
            time.sleep(self.interval)



def oscillate(servo,n):
    for i in range(n):
        servo.go_to_angle(70)
#        time.sleep(0.5)
#        servo.go_to_angle(150)
        time.sleep(0.5)


if __name__ == "__main__":
    servos = [Servo(i) for i in [0,1,2,3]]

    servos[0].go_to_angle(130)
    servo = Servo(1)
    oscillate(servo,1)
    import pdb; pdb.set_trace()

