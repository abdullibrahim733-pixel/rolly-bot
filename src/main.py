# main.py - Main Control Loop
# Rolly Bot - Autonomous Agricultural Robot

print("Rolly Bot starting...")

import machine
import time
import network
from ui import RollyDisplay
from sensors import UltrasonicSensor, SoilMoistureSensor

WIDTH = 128
HEIGHT = 64
I2C_SCL = 22
I2C_SDA = 21
ULTRASONIC_TRIG = 5
ULTRASONIC_ECHO = 18
SOIL_PIN = 34


class RollyBot:
    def __init__(self):
        self.i2c = machine.I2C(
            0, scl=machine.Pin(I2C_SCL), sda=machine.Pin(I2C_SDA), freq=400000
        )
        self.display = RollyDisplay(self.i2c, WIDTH, HEIGHT)
        self.ultrasonic = UltrasonicSensor(ULTRASONIC_TRIG, ULTRASONIC_ECHO)
        self.soil = SoilMoistureSensor(SOIL_PIN)
        self.station = network.WLAN(network.STA_IF)

        self.display.default_face()
        print("Rolly initialized successfully")

    def connect_wifi(self):
        """Connect to Wi-Fi network"""
        try:
            import secrets

            if not hasattr(secrets, "WIFI_SSID") or not secrets.WIFI_SSID:
                print("Wi-Fi credentials not configured")
                return False

            self.station.active(True)
            self.station.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

            print(f"Connecting to {secrets.WIFI_SSID}...")
            self.display.status("Connecting", secrets.WIFI_SSID)

            for attempt in range(20):
                if self.station.isconnected():
                    print(f"Wi-Fi connected: {self.station.ifconfig()}")
                    self.display.status("Wi-Fi OK!", self.station.ifconfig()[0])
                    return True
                time.sleep(0.5)

            print("Wi-Fi connection failed")
            self.display.alert_face()
            return False
        except Exception as e:
            print(f"Wi-Fi error: {e}")
            return False

    def check_sensors(self):
        """Read and display sensor data"""
        distance = self.ultrasonic.distance_cm()
        moisture = self.soil.read_percentage()

        print(f"Distance: {distance:.1f}cm | Soil Moisture: {moisture}%")
        self.display.status(f"Dist:{distance:.0f}cm", f"Moisture:{moisture}%")

        return distance, moisture

    def run(self):
        """Main control loop"""
        print("Entering main loop...")
        self.display.default_face()

        while True:
            try:
                distance, moisture = self.check_sensors()

                if distance < 20:
                    self.display.alert_face()
                    print("Obstacle detected!")

                time.sleep(2)

            except Exception as e:
                print(f"Error in main loop: {e}")
                self.display.alert_face()
                time.sleep(1)


if __name__ == "__main__":
    bot = RollyBot()
    bot.connect_wifi()
    bot.run()
