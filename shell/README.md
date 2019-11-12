> * use shell to do for loop and find command
```shell
for each in $(cat file_minus.txt); do if [ ${each:0:3} = "p11" ]; then find /data/MIMIC/p11/ -type d -name $each -exec cp -r {} MIMIC \;; fi; done
```
> * use shell to do cut command
```shell
awk -F, '{OFS=","; print$1, $8, $11, $12, $14, $16}' train.csv > train_local.csv
```
> * use shell to do cp command
```shell
awk -F, '{print$1}'  /nas/csv/Q4_5751_2019.10.18.csv | xargs -i cp -sr {} /nas/user/xuehui/test/coco/images/
```
> * use shell to do delete string in line command
```shell
sed -i '/^-1/d' sample.tx
```
