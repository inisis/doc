``` disk utils
1. fdisk -l
2. fdisk /dev/vdb  ##  n, p, 1, 回车, 回车, wq
3. mkfs.xfs -f /dev/vdb1
4. mount -t xfs /dev/vdb1 /mnt
5. umount /mnt
6. mount -t xfs /dev/vdb1 /data
7. vi /etc/fstab ##  /dev/vdb1 /data xfs auto 0 0
```
