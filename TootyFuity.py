import time
import board
import busio
import adafruit_mpr121
import pygame
import os

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

pygame.init()
pygame.mixer.set_num_channels(12)

# todo: make this dynamic
path = '/home/pi/TootyFruityBot/'

clips = {}

def play():
    while True:
        for i in range(12):
            if mpr121[i].value:
                print('Input {} touched!'.format(i))
                pygame.mixer.Channel(i).play(clips[i])
                # while pygame.mixer.music.get_busy() == True:
                #     continue
                print('played!'.format(i))


def invalid():
   print("INVALID CHOICE!")

def select_sounds_dir():
    sub_dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    for idx, file in enumerate(sub_dirs):
        print(f"{idx}:{file}")
    selected = input("pick a sounds folder:") 
    selected_folder = os.path.join(path, sub_dirs[int(selected)]) 
    selected_files = [f for f in os.listdir(path) if f.endswith('wav') and os.path.isfile(os.path.join(path, f))]
    filelist = []
    for root, dirs, files in os.walk(selected_folder):
        wavs = [file for file in files if file.endswith('wav')]
        for file in wavs:
            filelist.append(os.path.join(root, file))

    for idx, file in enumerate(filelist):
        print(idx)
        print(os.path.join(path, file))
        clips[idx] = pygame.mixer.Sound(os.path.join(path, file))
    play()


menu = {
    "1": ("Load", select_sounds_dir),
}
for key in sorted(menu.keys()):
     print(key + ":" + menu[key][0])

ans = input("Make A Choice:")
menu.get(ans, [None, invalid])[1]()


# # Use touched_pins to get current state of all pins.
# touched = mpr121.touched_pins
# # Test if 0 and 11 are touched.
# if touched[0] and touched[11]:
#     print('Input 0 and 11 touched!')
#sudo apt-get install gstreamer-1.0
# apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0