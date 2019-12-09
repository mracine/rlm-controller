#!/usr/bin/evn python3
from distutils.core import setup

# TODO Make sure this setup works
setup(
        name='rlmcontroller',
        version='0.0.1',
        description='An app for controlling a RGB LED Matrix connected to a Raspberry Pi',
        license='BSD',
        author='mracine',
        author_email='mrracine23@gmail.com',
        packages=['rlmcontrol'],
        install_requires=['flask'],
)
