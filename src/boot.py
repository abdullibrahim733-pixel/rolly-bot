# boot.py - Startup Configuration
# This runs on every boot of the ESP32

import machine
import gc

# Configure garbage collection
gc.collect()

# Configure serial communication
uart = machine.UART(0, 115200)
print("Rolly Bot booting...")

# Initialize I2C bus for OLED and sensors
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21), freq=400000)
print("I2C bus initialized")
print("I2C devices found:", i2c.scan())

# Optional: Load secrets (Wi-Fi credentials)
try:
    import secrets

    WIFI_SSID = secrets.WIFI_SSID
    WIFI_PASSWORD = secrets.WIFI_PASSWORD
    print("Secrets loaded successfully")
except ImportError:
    print("Warning: secrets.py not found")
    WIFI_SSID = None
    WIFI_PASSWORD = None

print("Boot complete - Starting main.py")
