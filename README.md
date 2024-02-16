# MicroPython DHT12 I2C

A MicroPython library for interfacing with an Aosong DHT12 temperature and humidity sensor over I2C.

This library focuses on using the I2C interface. The sensor also supports a 1-wire interface, available when pin 4 is connected to GND.

![demo](docs/demo.jpg)


## Installation

Using mip via mpremote:

```bash
$ mpremote mip install github:mcauser/micropython-dht12
$ mpremote mip install github:mcauser/micropython-dht12/examples
```

Using mip directly on a WiFi capable board:

```python
>>> import mip
>>> mip.install("github:mcauser/micropython-dht12")
>>> mip.install("github:mcauser/micropython-dht12/examples")
```

Manual installation:

Copy `src/dht12.py` to the root directory of your device.


## Examples

**Basic usage**

```python
from machine import I2C, Pin
import dht12

i2c = I2C(0)
sensor = dht12.DHT12(i2c)

sensor.measure()
print(sensor.temperature())
print(sensor.humidity())
```


## Methods

### __init__(i2c)

As with other modern Aosong sensors, this sensor supports an I2C interface and can be found at address 0x5C.

### check()

Scans the I2C bus looking for the sensor at it's fixed I2C address 0x5C. Raises a OSError if not found.

### measure()

Reads the temperature and humidity from the sensor over the I2C bus and persists for subsequent calls to `temperature()` and `humidity()`.
Received bytes contains a checksum to ensure the data is error free, otherwise an Exception is raised.

### temperature()

Returns the temperature in degrees Celsius from the data collected from the last `measure()` call.

### humidity()

Get the relative humidity as a percentage from the data collected from the last `measure()` call.


## Parts

* [DHT12 module](https://s.click.aliexpress.com/e/_DClODk9)
* [DHT12](https://s.click.aliexpress.com/e/_DCP2d1B)
* [DHT12](https://s.click.aliexpress.com/e/_DeFy39J)
* [TinyPICO](https://www.tinypico.com/)
* [WeMos D1 Mini](https://www.aliexpress.com/item/32529101036.html)


## Connections

DHT12 | TinyPICO (ESP32)
----- | ----------------
VIN   | 3V3
SDA   | 22
GND   | GND
SCL   | 21

DHT12 | Wemos D1 Mini (ESP8266)
----- | -----------------------
VIN   | 3V3
SDA   | GPIO4
GND   | GND
SCL   | GPIO5


## Links

* [micropython.org](http://micropython.org)
* [DHT12 datasheet](docs/DHT12.pdf)
* [TinyPICO Getting Started](https://www.tinypico.com/gettingstarted)


## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).

Copyright (c) 2016 Mike Causer
