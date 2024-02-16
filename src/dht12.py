# SPDX-FileCopyrightText: 2016 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython Aosong DHT12 I2C driver
https://github.com/mcauser/micropython-dht12
"""

from micropython import const

__version__ = "1.1.0"

I2C_ADDRESS = const(0x5C)  # fixed I2C address


class DHT12:
    def __init__(self, i2c):
        self._i2c = i2c
        self._buf = bytearray(5)

    def check(self):
        if self._i2c.scan().count(I2C_ADDRESS) == 0:
            raise OSError(f"DHT12 not found at I2C address {I2C_ADDRESS:#x}")
        return True

    def measure(self):
        buf = self._buf
        self._i2c.readfrom_mem_into(I2C_ADDRESS, 0, buf)
        if (buf[0] + buf[1] + buf[2] + buf[3]) & 0xFF != buf[4]:
            raise ValueError("Checksum error")

    def temperature(self):
        t = self._buf[2] + (self._buf[3] & 0x7F) * 0.1
        if self._buf[3] & 0x80:
            t = -t
        return t

    def humidity(self):
        return self._buf[0] + self._buf[1] * 0.1
