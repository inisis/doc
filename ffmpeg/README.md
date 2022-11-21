> * ffmpeg image sequence to video
```shell
ffmpeg -framerate 1 -r 1 -i %06d.jpg -vcodec mpeg4 output.mkv # names should start from 000000 and increment one by one
```
> * rename jpg
```shell
rename 's/\d+/sprintf("_%06d",$&)/e' *.jpg

a=0
for i in *.jpg; do
  new=$(printf "%06d.jpg" "$a") #06 pad to length of 6;
  mv -i -- "$i" "$new";
  let a=a+1;
done
```

> * mp4 to jpg
```
ffmpeg -i hq.mp4 input/%04d.png
```

> * jpgs to mp4
```
ffmpeg -framerate 30 -i stable-diffusion-webui/models/Stable-diffusion/input/%04d.png -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
```
