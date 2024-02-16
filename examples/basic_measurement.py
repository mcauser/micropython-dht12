# SPDX-FileCopyrightText: 2016 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython Aosong DHT12 I2C driver
https://github.com/mcauser/micropython-dht12

Prints the temperature and humidity
"""

from machine import I2C, Pin
import dht12

i2c = I2C(0)
sensor = dht12.DHT12(i2c)

if sensor.check():
    print(f"DHT12 found at I2C address {dht12.I2C_ADDRESS:#x}")

sensor.measure()
print(f"Temperature: {sensor.temperature()} C")
print(f"Humidity: {sensor.humidity()} RH")
