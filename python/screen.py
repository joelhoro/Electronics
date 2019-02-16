import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

class Screen():
    def __init__(self):
        RST = 24
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        font = ImageFont.load_default()
        self.initialize()

    def initialize(self):
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def drawer(self):
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        draw = ImageDraw.Draw(self.image)
        return draw

    def display(self):
        self.disp.image(self.image)
        self.disp.display()
