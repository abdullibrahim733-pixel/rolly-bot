# Rolly Bot

A rugged, autonomous mechatronics robot designed for precision agriculture and survival tasks.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Platform](https://img.shields.io/badge/platform-ESP32-blue)
![Language](https://img.shields.io/badge/language-MicroPython-orange)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Overview

Rolly is an autonomous bot built with:
- **ESP32** microcontroller running MicroPython
- **OLED Display** for HMI (Human-Machine Interface)
- **Ultrasonic Sensor** for obstacle detection
- **Soil Moisture Sensor** for agricultural monitoring
- **VEX Motor Controller** for precise movement

## Features

- [ ] Autonomous navigation with obstacle avoidance
- [ ] Soil moisture monitoring and reporting
- [ ] OLED display with animated "face"
- [ ] Wi-Fi enabled remote control
- [ ] Timelapse capture capability

## Project Structure

```
rolly-bot/
├── src/              # MicroPython firmware
│   ├── main.py       # Main control loop
│   ├── boot.py       # Startup configuration
│   ├── sensors.py    # Sensor drivers
│   └── ui.py         # OLED display interface
├── hardware/         # CAD and schematics
│   ├── cad/          # 3D printable parts
│   └── schematics/   # Wiring diagrams
└── docs/             # Documentation
```

## Setup

### Hardware Requirements
- ESP32 DevKit
- 128x64 I2C OLED Display
- HC-SR04 Ultrasonic Sensor
- Soil Moisture Sensor
- VEX Motor Controller

### Software Setup
1. Flash MicroPython to your ESP32 using [Thonny](https://thonny.org)
2. Copy files from `src/` to the ESP32
3. Configure Wi-Fi credentials in `secrets.py`
4. Upload `secrets.py` to ESP32 (keep local copy gitignored)

## Development

```bash
# Connect via Thonny or use ampy
ampy put src/main.py /main.py
ampy put secrets.py /secrets.py
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
