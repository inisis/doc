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
sed -i '/^-1/d' sample.txt
```
> * use shell to do replace string in line command
```shell
sed -i 's/^1/0/g' sample.txt
```
>  * to compute the difference between two files (a - b)
```shell
grep -F -v -f b.txt a.txt | sort | uniq
```
>  * to ls files in very large folder
```shell
ls -l -f folder (-f means do not sort)
```
>  * vim column 
```shell
ctrl-v
A (line tail append)

or

9360, 9362s/$/test/
```
>  * compile path
```shell
#gcc header
C_INCLUDE_PATH=/usr/include/
export C_INCLUDE_PATH

#g++ header
CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/
export CPLUS_INCLUDE_PATH

#dynamic libs
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/MyLib
export LD_LIBRARY_PATH

#static libs
LIBRARY_PATH=$LIBRARY_PATH:/MyLib
export LIBRARY_PATH
```

> * awk in for loop 
```shell
for number in 1.0 0.0 "" -1.0; do awk -v num="$number"  -F, '{if($2==num) print$2}' /data/Chexpert/CheXpert-v1.0/train_local.csv | wc -l; done
```
> * merger two files by columns
```shell
paste a.csv b.csv -d , (divide by ,)
```
> * split txt by percentage
```shell
split -l $[ $(wc -l oblique_all.csv|cut -d" " -f1) * 80 / 100 ] oblique_all.csv
```
