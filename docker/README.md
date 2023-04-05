> * docker show full command
```docker
docker ps -a --no-trunc
```
> * install docker in China
```docker
1.follow instruction in https://mirror.tuna.tsinghua.edu.cn/help/docker-ce/ to install docker ce
2.to use gpu, install nvidia-container-runtime then, use nvidia-container-runtime-script.sh
3.to speed up docker pull, use alibaba to accelerate it. https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors
4.sudo systemctl restart docker if gpu cannot be used.
```
> * user add group
```docker
usermod -a -G docker ubuntu
newgrp docker
sudo -u ubuntu -H docker info
```
> * CMD ENTRYPOINT
```docker
CMD ["python"] will create pid 1 with cmd, this won't get environment variable
CMD python will create pid 1 with /bin/sh -c python and another process called python

ENTRYPOINT is the same

if user needs to source env first, it's recommended to use ENTRYPOINT['run.sh'], 
run.sh is like this
#! /bin/bash
source env
python ***.py
```
> * iptables:No chain/target/match by the name
```docker
sudo iptables -t filter -F
sudo iptables -t filter -X
systemctl restart docker
```
> * docker registry harbor
```shell
tar zxvf harbor-offline-installer-v2.0.0.tgz 
cd harbor
cp harbor.yml.tmpl harbor.yml
change http && https ports accordingly
change data_volume
sudo ./install.sh
```
> * install certificate on linux
```shell
## ubuntu
cp registry.crt /usr/local/share/ca-certificates/
chmod 644 /usr/local/share/ca-certificates/registry.crt
update-ca-certificates
systemctl restart docker.service # better set "live-restore": true
## centos
cp registry.crt /etc/ssl/certs/
update-ca-trust enable
update-ca-trust extract
systemctl restart docker.service # better set "live-restore": true
```
> * rm /var/lib/docker Device or resource busy
```shell
umount /path
```
> * change data root
```shell
vim /etc/docker/daemon.json
{
    "data-root": "/new/docker/root"
}
```
> * container created time
```shell
docker inspect -f '{{ .Created }}' IMAGE_OR_CONTAINER
```
> * modify docker inspect data
```shell
vim /var/lib/docker/containers/<containerID>/config.v2.json
sudo systemctl restart docker
```

> * gpu
```
--gpus device=0,1 or --gpus all
```

> * docker rm using regex
```
docker ps -aqn 10 -f name=stable* | xargs docker rm -f
```

> * docker save with gzip
```
docker save myimage:latest | gzip > myimage_latest.tar.gz
```
