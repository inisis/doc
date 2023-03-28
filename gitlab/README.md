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

git lfs update after clone

git lfs fetch

git lfs pull
```
> * how to diff two folder on two different repo
```shell
in repo_a
git remote add -f b path/to/repo_b.git
git remote update
git diff master remotes/b/master -- path/to/repo
git remote rm b
```

> * git show Chinese character
```
git config --global core.quotepath false
```

> * git tag and push remote
```
git tag TAGNAME master
git push origin TAGNAME
```

> * store username and password
```
git config --global credential.helper store
```

> * git config username and email for single project
```
git config user.name
git config user.email
```

> git add with Chinese Character
```
git add $(awk -F： {'print$2'} <<< $(git status | grep '修改'))
```

> * git submodule
```
git submodule update --init --recursive
```

> * git stash(How to keep your local changes and switch to another branch in Git)
```
git stash
git stash apply or git stash pop
```

> * git 中文乱码
```
export LESSCHARSET=utf-8
```

> * gen ssh keys
```
ssh-keygen -t rsa -b 4096
```
