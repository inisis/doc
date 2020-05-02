> * install impitool
```shell
apt-get install ipmitool
```

> * get user id
```shell
ipmitool channel getaccess 1
```

> * set password
```shell
ipmitool user set password 2 ADMIN
```

> * get ip address
```shell
ipmitool lan print  | grep "IP Address"
```
