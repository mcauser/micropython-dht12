import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-dht12',
    py_modules=['dht12'],
    version='1.0.0',
    description='MicroPython library for the DHT12 temperature and humidity sensor.',
    long_description='This library lets you communicate with an Aosong DHT12 temperature and humidity sensor over I2C.',
    keywords='dht12 aosong dht temperature humidity micropython',
    url='https://github.com/mcauser/micropython-dht12',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)