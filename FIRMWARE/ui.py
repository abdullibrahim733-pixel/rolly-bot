# ui.py - OLED Display Interface
# Handles all display rendering for Rolly's face

from ssd1306 import SSD1306_I2C
import framebuf


class RollyDisplay:
    def __init__(self, i2c, width=128, height=64):
        self.display = SSD1306_I2C(width, height, i2c)
        self.width = width
        self.height = height
        self.display.fill(0)
        self.display.show()

    def clear(self):
        self.display.fill(0)

    def show(self):
        self.display.show()

    def default_face(self):
        """Draw Rolly's default happy expression"""
        self.clear()

        # Left eye
        self.display.pixel(40, 25, 1)
        self.display.pixel(41, 25, 1)
        self.display.pixel(42, 25, 1)
        self.display.pixel(40, 26, 1)
        self.display.pixel(42, 26, 1)
        self.display.pixel(40, 27, 1)
        self.display.pixel(42, 27, 1)

        # Right eye
        self.display.pixel(85, 25, 1)
        self.display.pixel(86, 25, 1)
        self.display.pixel(87, 25, 1)
        self.display.pixel(85, 26, 1)
        self.display.pixel(87, 26, 1)
        self.display.pixel(85, 27, 1)
        self.display.pixel(87, 27, 1)

        # Mouth (smile)
        for x in range(45, 83):
            y = 40 + int(abs(x - 64) / 4)
            self.display.pixel(x, y, 1)

        # Antenna dots
        self.display.pixel(64, 8, 1)
        self.display.pixel(30, 12, 1)
        self.display.pixel(98, 12, 1)

        self.show()

    def alert_face(self):
        """Draw Rolly's alert/worried expression"""
        self.clear()

        # Wide eyes (concerned)
        self.display.pixel(40, 24, 1)
        self.display.pixel(41, 24, 1)
        self.display.pixel(42, 24, 1)
        self.display.pixel(43, 24, 1)
        self.display.pixel(40, 28, 1)
        self.display.pixel(41, 28, 1)
        self.display.pixel(42, 28, 1)
        self.display.pixel(43, 28, 1)

        self.display.pixel(84, 24, 1)
        self.display.pixel(85, 24, 1)
        self.display.pixel(86, 24, 1)
        self.display.pixel(87, 24, 1)
        self.display.pixel(84, 28, 1)
        self.display.pixel(85, 28, 1)
        self.display.pixel(86, 28, 1)
        self.display.pixel(87, 28, 1)

        # Worried mouth
        for x in range(50, 78):
            y = 42 - int(abs(x - 64) / 4)
            self.display.pixel(x, y, 1)

        # Sweat drop
        self.display.pixel(95, 20, 1)
        self.display.pixel(96, 20, 1)
        self.display.pixel(95, 21, 1)
        self.display.pixel(96, 21, 1)

        self.show()

    def text(self, message, x=0, y=0):
        """Display text message"""
        self.display.text(message, x, y, 1)
        self.show()

    def status(self, line1, line2=""):
        """Display two-line status"""
        self.clear()
        self.display.text(line1[:16], 0, 10, 1)
        if line2:
            self.display.text(line2[:16], 0, 30, 1)
        self.show()
