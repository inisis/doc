> * sftpgo
```
sudo apt update -y
sudo add-apt-repository ppa:sftpgo/sftpgo
sudo apt update -y
sudo apt install sftpgo -Y

vim /etc/sftpgo/sftpgo.json # modify ports

sudo systemctl restart sftpgo
sudo systemctl status sftpgo
sudo systemctl enable sftpgo

sudo ufw allow 17110/tcp
```
