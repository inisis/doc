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
> * use shell to do replace string in line command; replace before first space
```shell
sed -i 's/^1/0/g' sample.txt
sed -i 's/[^ ]* /0 /' {}
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
> * show which system is using
```shell
lsb_release -a
cat /etc/os-release
```
> * awk print substring
```shell
awk -F, {'if($2>0.5) print substr($1, 5)'} predict.csv
```
> * awk calculate average
```shell
awk -F, '{if($2==12) {sum += $3; i+=1}};END {print sum; print sum/i; print i}' dcm_10_APPA_Bits_WindowLevel.csv 
```
> * rename
```shell
rename 's/\d+/sprintf("%05d",$&)/e' foo*
```
> * find file size
```shell
find . -type f -size -4096c
-size n[cwbkMG]

    File uses n units of space. The following suffixes can be used:

    `b'    for 512-byte blocks (this is the default if no suffix  is
                                used)

    `c'    for bytes

    `w'    for two-byte words

    `k'    for Kilobytes       (units of 1024 bytes)

    `M'    for Megabytes    (units of 1048576 bytes)

    `G'    for Gigabytes (units of 1073741824 bytes)

    The size does not count indirect blocks, but it does count
    blocks in sparse files that are not actually allocated. Bear in
    mind that the `%k' and `%b' format specifiers of -printf handle
    sparse files differently. The `b' suffix always denotes
    512-byte blocks and never 1 Kilobyte blocks, which is different
    to the behaviour of -ls.
```
> * rotate image
```shell
for each in $(cat keypoint_dev.csv); do convert $each -rotate "$((RANDOM%5*90))" rotate/$(basename $each); done
```
> * vim set tab to 4 space
```shell
vim ~/.vimrc
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent

:%retab
```

> * change file owner and group
```shell
chown 1000 jenkins/
chgrp 1000 jenkins/
```
> * generate file for python from proto
```shell
protoc -I. --python_out=. *.proto
```
> * delete ^M at the end of line
```shell
tr -d "\015" < tem.txt > temp.txt 
```
> * find proc running directory
```
ls -l /proc/$PID/exe
```
> * su very slow
```shell
hostname -f
sudo vim /etc/hosts
127.0.0.1 current_hostname
```

> * disk read/write
```shell
dd if=/root/data/dcm/1.3.6.1.4.1.9590.100.1.2.111127328611009826704705918831957848542.dcm of=/dev/null bs=1M count=1024
dd if=/dev/zero of=/root/data/test.dbf bs=8k count=3000
```
> * check linux version
```shell
cat /etc/issue
```

> * awk
```shell
awk -F, '{system("cp -sr "$1" train/"$2"")}' image.txt
```

> *
```
for directories
find /desired_location -type d -print0 | xargs -0 chmod 0755
for files
find /desired_location -type f -print0 | xargs -0 chmod 0644
```

> * awk
```
git rm $(awk -F: {'print$2'} <<< $(git status | grep deleted))
```

> * sed
```
sed -i 's/kata1.*gz/'$(echo $WEIGHTS)'/g' /katago/config/conf.yaml
```

> * undo local commit
```
git reset --soft # if you want to keep your changes
git reset --hard # if you don't care about keeping the changes you made
```

> * restore default bashrc
```
cp /etc/skel/.bashrc ~/
```

> * add user with home
```
useradd -m -s /bin/bash yao
```

> * centos add user to sudoer
```
sudo usermod -aG wheel test-user
```

> * shell for loop
```
for i in {1..100}; do echo $i; done
```

> * remove deleted
```
git rm $(git status | grep deleted | awk '{print $3}')
```

> * change display name on terminal
```
export PS1="Hello.Master$ "
```

> * delete all zero size file
```
find . -name "*" -type f -size 0c | xargs -n 1 rm -f
```

> * download without restart
```
wget -c 
```

> * ssh with rsa
```
ssh -i rsa_file
```

> * sshgen keys
```
sshgen keys
```

> * disable centos new mail
```
echo "unset MAILCHECK" >> ~/.bashrc
```

> * apt update failed
```
chmod 1777 /tmp
```

> * replace np.float with np.float32
```
find . -type f -exec sed -i 's/\bnp.float\b/np.float32/g' {} +
```

> * change bash prompt 
```
export PS1="\u:"
```

> * rsync without overwrite existing
```
rsync -avz --ignore-existing -e "ssh -p 2232" SRC/ user@remote.host:/DEST/ 
```

> * pkill by name
```
pkill -9 -f my_pattern
```

> * dynamic add disk space
```
resize2fs /dev/vda1
```

> * ddp multi node
```
python3 -m torch.distributed.launch --nproc_per_node=2 --nnodes=2 --node_rank=1 --master_addr=198.18.28.14 --master_port=1234 main.py --backend=nccl --use_syn --batch_size=8192 --arch=resnet152
```

> *  show all the arguments of a running Linux process
```
ps auxww | grep <process_name_or_pid>
```

> * get folder size and sort
```
du -h --max-depth=1 | sort -h
```

> * screen
```
screen -S name
screen -r name
```

> * get last arguments
```
alt + . or $_
```

> * get process up time
```
#!/bin/bash
  
# Get the PID (process ID). Use $$ for the current shell process, or replace it with another PID.
PID=$1

# Get the process start time in seconds since epoch
start_time=$(ps -o lstart= -p "$PID" | date -d "$(cat)" +%s)

# Get the current time in seconds since epoch
current_time=$(date +%s)

# Calculate uptime
uptime=$((current_time - start_time))

# Convert uptime to minutes (optional)
uptime_minutes=$((uptime / 60))

# Print uptime
echo "Process uptime: $uptime seconds ($uptime_minutes minutes)"
```

> * clear screen
```
ctrl + L
```

> * json format
```

```

> * rsync exclude
```
rsync -av --exclude='chip*/agent/data/' source/ destination/
```

> * cat with index
```
cat -n
```

> * sort
```
sort -n
```

> * mount
```

```

> * vim copy many times
```
yy100p
```

> * cal size and sort
```
du -hd 1 . | sort -hr
```
