`dht12` module
*****************

.. module:: dht12

DHT12
=======

.. class:: DHT12(i2c, [address])

    The basic class for handling the communication with the sensor.

    The ``i2c`` parameter is an initialized I²C bus, and the optional address
    specifies which sensor to connect to, if you have more than one and have
    changed their addresses with the ``Addr`` pin.

    .. method:: temperature()

        Get the temperature in Celcius

    .. method:: humidity()

        Get the relative humidity as a percentage
