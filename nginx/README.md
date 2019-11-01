> * nginx will store lateset 15 days log as default, if you want to change that,
```shell
vim /etc/logrotate.d/nginx && change rotate to 10000
logrotate /etc/logrotate.d/nginx
```
