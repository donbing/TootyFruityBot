## FFMPEG convert mp3 to wav
```sh
for f in *.mp3; do ffmpeg -i "${f}" -vn -c:a pcm_s16le  -ar 44100  "${f%.*}_mp3-to.wav" ; done 
```

## run
```sh
# exit any previous audio binds
aconnect -x
# run the script
python3 -m foo
```
