# Project Overview

## Project Name
Temperature and Humidity Meter

## Summary
This project monitors temperature and humidity using the HTU21D sensor connected to a MicroPython board. Based on the sensor readings, it provides visual feedback through four discrete LEDs (temperature levels) and one RGB LED (humidity status). It's ideal for educational purposes and for integrating into environments like smart trailers or off-grid systems.

## Motivation
The goal of this project is to create a simple yet effective way to visually track environmental conditions using common electronic components and MicroPython.

## How it Works
- The HTU21D sensor communicates via I2C.
- Temperature thresholds activate one or more discrete LEDs to represent temperature levels.
- Humidity ranges are color-coded using an RGB LED.
- The system runs continuously in a loop, updating values in real-time.

## Application Examples
- Embedded systems education
- Smart trailer environment monitoring
- Home IoT temperature/humidity tracking
- Off-grid or mobile sensor stations

