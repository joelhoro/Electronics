import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

class Screen():
    def __init__(self):
        RST = 24
        print("Initializing SSD1306 OLED screen... ", end='')
        self.active = False
        try:
            self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
            self.initialize()
            print("done")
            self.active = True
        except:
            pass
            #raise Exception("Could not connect to screen")

    def initialize(self):
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def clear(self):
        self.disp.clear()
        self.disp.display()

    def toggle(self):
        if self.active:
            self.clear()
        self.active = not self.active

    def drawer(self):
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        draw = ImageDraw.Draw(self.image)
        return draw

    def display(self):
        self.disp.image(self.image)
        self.disp.display()
