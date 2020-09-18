> * show gpu vendor
```shell
lspci -vnn | grep VGA -A 12
```

> * set gpu power limit
```shell
nvidia-smi -i 2 -pl 125
```

> * get gpu power info
```shell
nvidia-smi -q -d POWER
```
> * ppa china mirror
```shell
replace http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu with https://launchpad.proxy.ustclug.org/graphics-drivers/ppa/ubuntu
```
> * install nvidia gpu driver
```
1. download nvidia driver(.run appendix)

2. Ctrl+Alt+F1

3. sudo service lightdm stop

4. sudo bash ×××.run

5. sudo modprobe -r nvidia

6. lsof /dev/nvidia*

sudo vim /etc/modprobe.d/blacklist.conf

blacklist nouveau

sudo update-initramfs -u
```
