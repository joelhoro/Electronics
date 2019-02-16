import math
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

from screen import Screen

bounds = [32700.0,20000.0,-200.0]

def convert_coordinates(x):
#    return x
    if x > bounds[1]:
        value = -1 + (x-bounds[0]) / (bounds[1]-bounds[0])
    else:
        value = (x-bounds[1]) / (bounds[2]-bounds[1])
    resolution = 0.1
    return math.floor(value/resolution)*resolution

class JoyStick():
    Address_Ox48 = 0x48

    GAIN = 1
    def __init__(self, address, channels, button_gpio_pin):
        self.address = address
        self.channels = channels
        self.button_gpio_pin = button_gpio_pin
        self.adc = Adafruit_ADS1x15.ADS1115(address=self.address)
        # not great to alter this setting here...
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    def position(self):
        reads = [
            self.adc.read_adc(i, gain=JoyStick.GAIN) for i in self.channels
        ]

        reads = [convert_coordinates(r) for r in reads]
        return reads + [ not GPIO.input(self.button_gpio_pin) ]
    


