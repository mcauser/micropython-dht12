# MicroPython DHT12 I2C

A MicroPython library for interfacing with an Aosong DHT12 temperature and humidity sensor over I2C.

This library focuses on using the I2C interface. The sensor also supports a 1-wire interface, available when pin 4 is connected to GND.

#### Pinout

```
+---------+
|xxxxxxxxx|
|xxxxxxxxx|
+---------+
  | | | |
  1 2 3 4
```

1=VDD, 2=SDA, 3=GND, 4=SCL

For full documentation see http://micropython-dht12.rtfd.io/.

![demo](docs/DHT12.jpg)