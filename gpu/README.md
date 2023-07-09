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
> * find gpu process
```shell
sudo fuser -v /dev/nvidia*
```
> * uninstall nvidia
```shell
nvidia-uninstall
```
> * kill gnome-shell autorestart
```
(base) vipuser@ubuntu1804:~$ sudo lsof -n -w  /dev/nvidia*
COMMAND     PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
gnome-she 11861  gdm   12u   CHR 195,255      0t0  457 /dev/nvidiactl
gnome-she 11861  gdm   13u   CHR   195,0      0t0  458 /dev/nvidia0
gnome-she 11861  gdm   14u   CHR   195,0      0t0  458 /dev/nvidia0

sudo service gdm stop
```

> * check nvidia device
```
lspci | grep -i nvidia
```

> * CUDA_HOME
```
export CUDA_HOME=/usr/local/cuda
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
```

> * device order
```
export CUDA_DEVICE_ORDER=PCI_BUS_ID
```

> * A100 Nvlink
```
sudo apt-get install cuda-drivers-fabricmanager-525
sudo nvidia-smi -pm 1
sudo nvidia-smi -mig 0
sudo systemctl status nvidia-fabricmanager
```

> * nsys-ui in docker
```
sudo apt-get install libxcb-xinerama0
sudo apt-get install libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 libegl1-mesa
sudo apt install openjdk-8-jre
```
