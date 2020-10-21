> * install impitool
```shell
sudo apt-get install ipmitool
```

> * get user id
```shell
sudo ipmitool channel getaccess 1
```

> * set password
```shell
sudo ipmitool user set password 2 ADMIN
```

> * get ip address
```shell
sudo ipmitool lan print  | grep "IP Address"
```

> * get fan speed
```shell
sudo ipmitool sensor list all | grep FAN
```
