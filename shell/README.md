> * use shell to do for loop and find command
```shell
for each in $(cat file_minus.txt); do if [ ${each:0:3} = "p11" ]; then find /data/MIMIC/p11/ -type d -name $each -exec cp -r {} MIMIC \;; fi; done
```
> * use shell to do cut command
```shell
awk -F, '{OFS=","; print$1, $8, $11, $12, $14, $16}' train.csv > train_local.csv
```
