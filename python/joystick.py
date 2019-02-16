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
    Address_Ox49 = 0x48
    Address_Ox4A = 0x4A
    Address_Ox4B = 0x4B

    GAIN = 1
    def __init__(self, bus, address, channels, button_gpio_pin):
        self.bus = bus
        self.address = address
        self.channels = channels
        self.button_gpio_pin = button_gpio_pin
        self.adc = Adafruit_ADS1x15.ADS1115(address=self.address,busnum=self.bus)
        print('Initializing ADS1115 on bus %s @ %s - channels %s and %s' % (self.bus, self.address, channels[0], channels[1]))
        # not great to alter this setting here...
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.last_position = [0,0,0]

    def position(self):
        reads = [
            self.adc.read_adc(i, gain=JoyStick.GAIN) for i in self.channels
        ]
        reads = [convert_coordinates(r) for r in reads]
        reads = reads + [ not GPIO.input(self.button_gpio_pin) ]
        self.last_position = reads
        return reads
    


