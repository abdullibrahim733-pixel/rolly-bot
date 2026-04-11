# sensors.py - Sensor Drivers
# Handles ultrasonic and soil moisture sensors

import machine
import time


class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)
        self.trigger.value(0)

    def distance_cm(self):
        """Measure distance in centimeters"""
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)

        pulse_start = time.ticks_us()
        timeout = time.ticks_add(pulse_start, 30000)

        while self.echo.value() == 0:
            pulse_start = time.ticks_us()
            if time.ticks_diff(time.ticks_us(), timeout) > 0:
                return 500

        pulse_end = pulse_start
        timeout = time.ticks_add(pulse_end, 30000)

        while self.echo.value() == 1:
            pulse_end = time.ticks_us()
            if time.ticks_diff(time.ticks_us(), timeout) > 0:
                return 500

        duration = time.ticks_diff(pulse_end, pulse_start)
        distance = (duration * 0.0343) / 2
        return distance


class SoilMoistureSensor:
    def __init__(self, pin, threshold=3000):
        self.adc = machine.ADC(machine.Pin(pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.threshold = threshold

    def read_raw(self):
        """Read raw ADC value (0-4095)"""
        return self.adc.read()

    def read_percentage(self):
        """Read moisture as percentage (0=dry, 100=wet)"""
        raw = self.read_raw()
        percentage = max(0, min(100, int((1 - raw / 4095) * 100)))
        return percentage

    def is_dry(self):
        """Returns True if soil needs water"""
        return self.read_raw() > self.threshold
