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
