# TootyFruityBot
A Python script to trigger audio from touch events on an MPR121

---

## Setup
```sh
# enable i2c
sudo raspi-config nonint do_i2c 0
# install dependencies
sudo apt update
sudo apt install -y python3-pip libsdl2-mixer-2.0-0 libgles2-mesa-dev
pip3 install adafruit-circuitpython-mpr121 pygame
```

## Add sounds
Drop samples into a directory next to the script and it will load the first 12 into banks for triggering on touch.

## TODO
- quantisation
- select specific files rather than first 12
- change sounds on the fly
- save sound mappings