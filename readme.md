# TootyFruityBot
A Python script to trigger audio from touch events on a MPR121

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

