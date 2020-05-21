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
```
sudo iptables -t filter -F
sudo iptables -t filter -X
systemctl restart docker
```
