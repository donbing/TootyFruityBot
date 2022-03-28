
## setup
```sh
sudo raspi-config nonint do_i2c 0
sudo apt update
sudo apt install -y python3-pip 
pip3 install adafruit-circuitpython-mpr121
pip3 install pygame
sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
sudo apt-get install libgles2-mesa-dev
```

## convert mp3 to wav
```sh
for f in *.mp3; do ffmpeg -i "${f}" -vn -c:a pcm_s16le  -ar 44100  "${f%.*}_mp3-to.wav" ; done 
```

## run
```sh
aconnect -x
python3 -m foo
```
