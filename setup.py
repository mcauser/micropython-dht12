from distutils.core import setup

setup(
    name='micropython-dht12',
    py_modules=['dht12'],
    version="1.0",
    description="MicroPython library for the DHT12 temperature and humidity sensor.",
    long_description="""\
This library lets you communicate with a DHT12 temperature and humidity sensor over I2C.
""",
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    classifiers = [
        'Development Status :: 6 - Mature',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)