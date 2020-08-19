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
