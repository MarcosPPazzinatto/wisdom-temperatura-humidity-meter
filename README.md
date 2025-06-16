# Temperature and Humidity Meter

This project uses a MicroPython-based board and an HTU21D sensor to measure temperature and humidity. It provides a visual representation of the environmental conditions using discrete LEDs and an RGB LED.

## Features

- Reads temperature and humidity using the HTU21D sensor over I2C  
- Displays temperature level using 4 discrete LEDs (25%, 50%, 75%, 100%)  
- Displays humidity level using an RGB LED:  
  - Red for low humidity (< 30%)  
  - Green for optimal humidity (30% - 70%)  
  - Blue for high humidity (> 70%)

## Hardware Requirements

- HTU21D temperature and humidity sensor  
- Microcontroller with MicroPython support (e.g., ESP32)  
- 4 LEDs for temperature indicators  
- 1 RGB LED for humidity level  
- Resistors, breadboard, and wiring  
- Optional: Seaflow water pump integration for trailer use

## Pin Configuration

| Function         | GPIO Pin |
|------------------|----------|
| I2C SDA          | 21       |
| I2C SCL          | 22       |
| LED 25%          | 13       |
| LED 50%          | 4        |
| LED 75%          | 16       |
| LED 100%         | 17       |
| RGB LED - Red    | 19       |
| RGB LED - Green  | 23       |
| RGB LED - Blue   | 18       |

## Setup

1. Connect all components according to the pin configuration.
2. Upload the `temperatura_humidity_meter.py` script to your MicroPython board.
3. Run the script to start monitoring temperature and humidity.

## License

This project is open-source. No specific license has been applied yet.
