# RPi RGB LED Matrix (RLM) Control
A webapp written in Python using the Flask framework for controlling an RGB LED Matrix connected to a Raspberry Pi.

*Please note: I'm still working on this project, so it's an unfinished broken mess right now. I'll remove this note when I think it's at a good place. This README is also unfinished and will probably change a lot as I continue working on this.*

This app allows a client to send requests to a Raspberry Pi (or any server) connected to a RGB LED Matrix. This project does not contain logic for displaying content to an RGB LED Matrix. Instead, a user can create their own implementation, or, more likely, use this existing implementation for actually displaying content: https://github.com/hzeller/rpi-rgb-led-matrix

The above link is also a great resource for information on configuring and wiring a Raspberry Pi to an RGB LED Matrix, so I highly recommend it for beginners.

## Project structure
- instance
  - resources
- app

- *instance*: Data specific to an instance of an app, such as databases, configuration, resources, etc.
- *instance/resources*: Typically where the content to display to the RLM should reside, if not specified elsewhere

## Installation
install pip
install flask (potentially just run setup)
See Flask documentation for deployment options

*Note: the image/video display binary (in the rpi-rgb-led-matrix project) needs root privileges in order to be able to nicely display content to the RLM for accessing specific hardware registers on the Raspberry Pi used for [WHAT?]. Since granting this Flask app root privileges for execution would be tricky and isn't a great idea in general, I've modified the rpi-rgb-led-matrix code to start a Unix domain socket, and listen for content published there. I also start the rpi-rgb-led-matrix executable as a systemd service, so it is always on in the background, and has the proper privileges to access the required hardware registers. This app then can just write configuration changes to the socket, and the service can modify its execution accordingly.*

*More notes: the original rpi-rgb-led-matrix project does require root privileges for accessing those specific hardware registers on the Raspberry Pi, but as soon as it is done accessing those registers as root, it drops the execution down to daemon:daemon. I've modified my execution to pi:pi (just happened to be the user I created for executing this app), but it is crucial that if you are running in a mode where privileges will be dropped, that the user and group being dropped to has read/write privileges to the socket.*

## Feature Ideas
Through the webapp, you can:
- Turn on/off the RLM display
- Control a slideshow of preloaded images/gifs
-
- Display time? date? temperature?
- Adjust brightness? Saturation? etc.
- Enter a custom string to write?
-
- Enter a URL of an image or video to display, or:
- Upload an image/video file to display

## Future Enhancements
- A systemd service to start on boot
- Containerizing this app for easier deployment
- A mobile app that can connect to the RPi via bluetooth
