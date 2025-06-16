from machine import Pin
from machine import SoftI2C
from RoboCore_HTU21D import HTU21D
from machine import PWM

i2c_21_22 = SoftI2C(sda=Pin(21), scl=Pin(22))

led_25   = Pin(13, Pin.OUT)
led_50   = Pin(4, Pin.OUT)
led_75   = Pin(16, Pin.OUT)
led_100  = Pin(17, Pin.OUT)

led_25.off()
led_50.off()
led_75.off()
led_100.off()

led_red = PWM(Pin(19))
led_green = PWM(Pin(23))
led_blue = PWM(Pin(18))

led_red.duty_u16(0)
led_green.duty_u16(0)
led_blue.duty_u16(0)

def rgb_color(red_value, green_value, blue_value):
    if red_value < 0:
        red_value = 0
    if red_value > 100:
        red_value = 100

    led_red.duty_u16(red_value * 65535 // 100)

    if green_value < 0:
        green_value = 0
    if green_value > 100:
        green_value = 100

    led_green.duty_u16(green_value * 65535 // 100)

    if blue_value < 0:
        blue_value = 0
    if blue_value > 100:
        blue_value = 100

    led_blue.duty_u16(blue_value * 65535 // 100)

#Author: 'Marcos Paulo Pazzinatto'
#Description: 'Temperature Humidity Meter'

htu21d = HTU21D(i2c_21_22)
while True:
  if (htu21d.temperature) < 15:
    led_25.on()
    led_50.off()
    led_75.off()
    led_100.off()
  elif (htu21d.temperature) >= 15 and (htu21d.temperature) < 25:
    led_25.on()
    led_50.on()
    led_75.off()
    led_100.off()
  elif (htu21d.temperature) >= 25 and (htu21d.temperature) < 35:
    led_25.on()
    led_50.on()
    led_75.on()
    led_100.off()
  else:
    led_25.on()
    led_50.on()
    led_75.on()
    led_100.on()
  if (htu21d.humidity) < 30:
    rgb_color(100, 0, 0)
  elif (htu21d.humidity) >= 30 and (htu21d.humidity) < 70:
    rgb_color(0, 100, 0)
  else:
    rgb_color(0, 0, 100)

