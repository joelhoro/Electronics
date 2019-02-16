from __future__ import division
import time

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

servo_min, servo_max = [4096 * x for x in [0.02, 0.12]]

# Helper function to make setting a servo pulse width simpler.

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

class Servo():
    def __init__(self,channel):
        self.channel = channel

    def set_servo_pulse(self, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(self.channel, 0, pulse)
    
    def set_angle(self,angle):
        angle = max(0,min(angle,180))
        pulse = servo_min + (servo_max-servo_min)/180.0 * angle
        pwm.set_pwm(self.channel, 0, int(pulse))
        self.angle = angle
# servo = Servo(2)

# import pdb; pdb.set_trace()



# channel = 2
# # print('Moving servo on channel 0, press Ctrl-C to quit...')
# while True:
#     # Move servo on channel O between extremes.
#     pwm.set_pwm(channel, 0, servo_min)
#     time.sleep(1)
#     pwm.set_pwm(channel, 0, servo_max)
#     time.sleep(1)
