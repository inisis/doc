> * ssh pubkey fail
```
ssh-keygen -t rsa
ssh -vvv localhost
tail -f /var/log/auth.log
```

> * unable to mmap 72 bytes from file </torch_3232361_952479038_15558>: Cannot allocate memory (12)
```
sudo sysctl -w vm.max_map_count=368072 # increase size if persist
```
