> * nginx will store lateset 15 days log as default, if you want to change that,
```shell
vim /etc/logrotate.d/nginx && change rotate to 10000
logrotate /etc/logrotate.d/nginx
```
> * nginx will report 403 if you are not using a proper permission, to solve that,
```shell
change nginx user to root;
```
> * use map to filter unneeded info
```shell
map $request $log_request {
    ~*wado* 1;
    default 0;
}
```
> * static file is stored in $root/url/
```
root /root/static/;
           location /demo {
           index report_demo.html;
           }
should be /root/static/demo/report_demo.html
```
> * nginx http trim file name
```
vim src/http/modules/ngx_http_autoindex_module.c
change #define NGX_HTTP_AUTOINDEX_NAME_LEN     50
```
