> * gitlab basic command
```shell
modify gitlab config
sudo vim /etc/gitlab/gitlab.rb

reconfigure gitlab
sudo gitlab-ctl reconfigure

start gitlab
sudo gitlab-ctl start

stop gitlab
sudo gitlab-ctl stop

restart gitlab
sudo gitlab-ctl restart

check gitlab status
sudo gitlab-ctl status
```

> * install git lfs
```shell
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

> * git lfs basic command
```shell
git lfs install --skip-smudge ## --skip-smudge to prevent LFS from downloading or cloning files (globally) unless explicitly specified


git lfs track YOUR_FILE

git lfs untrack YOUR_FILE
```
> * how to diff two folder on two different repo
```shell
in repo_a
git remote add -f b path/to/repo_b.git
git remote update
git diff master remotes/b/master -- path/to/repo
git remote rm b
```
