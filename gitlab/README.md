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

> * git plot most productive time
```
git log --pretty=format:"%h|%an|%ad|%s" --date=format:'%Y-%m-%d %H:%M:%S' --all > commit_log.txt

import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# Read commit log from file
with open('commit_log.txt', 'r', encoding='utf-8') as file:
    commit_log = file.readlines()

# Dictionary to store commit counts by hour
commit_counts = defaultdict(int)

# Process commit timestamps
for line in commit_log:
    _, _, timestamp, _ = line.split('|')
    commit_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    hour = commit_time.hour
    commit_counts[hour] += 1

# Find the most productive hour
most_productive_hour = max(commit_counts, key=commit_counts.get)

# Plot commit counts by hour
hours = list(commit_counts.keys())
commit_values = list(commit_counts.values())

plt.bar(hours, commit_values, color='blue', alpha=0.7)
plt.title('Commit Activity by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Commits')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight the most productive hour
plt.annotate(f'Most Productive Hour: {most_productive_hour}', 
             xy=(most_productive_hour, commit_counts[most_productive_hour]),
             xytext=(most_productive_hour + 1, max(commit_values) * 0.8),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=9, color='red')

# Save the plot to disk
plt.savefig('commit_activity_plot.png')

# Display the plot
plt.show()
```

> * git ignore file mode change
```
git config core.fileMode false
```

> * git rebase
```
git fetch origin
git rebase origin/main
```

> * git patch
```
git apply --check a.patch
```
