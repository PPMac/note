* 可以直接使用diff命令比较两个文件
`diff -u file1 file2 >diff.txt`

* 使用patch将上面的比较结果应用到某一个文件
`patch -R file1 < diff.txt`

* 修改提交的commit信息
`git commit --amend`

git add -u 将所有修改的文件加入暂存区
git add -A 将本地删除和新增的添加添加到暂存区
git add -p 将对一个文件内的修改进行选择性的添加

如果在工作区的修改尚未完成时忽然有一个紧急任务，需要从一个干净的工作区域开始新的工作
，或要切换到别的分支进行工作，那么如何保存当前未完成的工作进度呢？
可以使用`git stash`新的工作分支修改完毕以后，再切换到当前分支，调用
`git stash pop`命令则可以恢复之前保存的工作进度

* 中文支持
`git config --global core.quotepath false`

使用
`starce -e 'trace=file' git status`
命令查看git status命令执行过程

* 修改配置文件
```
git config -e
git config -e --system
git config -e --global
```

* 查看暂存区与版本库中文件的差异
`git diff --cached 或 git diff --staged`

Redmine是一款实现需求管理和缺陷跟踪的项目管理软件，可以与Git版本库实现整合

git reset HEAD
暂存区的目录树会被重写，会被master分支指向的目录树所替换，但是工作区不受影响

git rm --cached filename
直接从暂存区中删除文件，工作区中则不会做出改变

git checkout . 或 git checkout -- <file> 时，会用暂存区全部的文件或指定的文件替换
工作区中的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动

git checkout HEAD . git checkout HEAD <file>
会用head指向master分支中的全部或部分文件替换暂存区和工作区中的文件。同时清除工作区和暂存区的未提交的改动

git diff 工作区与暂存区比较
git diff --cached 暂存区与HEAD比较
git diff HEAD 工作区与HEAD比较

用reflog挽救错误的重置
git relog show master | head -5  (tail -5 .git/logs/refs/master)
git reset --hard master@{2}

git reset --hard HEAD
--hard 表示将 working tree 和 index file 都撤销到以前状态
--soft 表示只撤销 commit,而保留 working tree 和 index file 的信息
--mixed 会撤销 commit 和index file,只保留 working tree 的信息

git reset 仅用HEAD指向目录树重置暂存区，工作区不会受影响，相当于将之前用git add
命令更新到暂存区的内容撤出暂存区。

git reset HEAD 同上
git reset -- filename 仅将对文件filename的修改撤出暂存区
git reset HEAD filename 同上

git checkout branch
git checkout -- filename 用暂存区中filename的文件覆盖工作区中的filename文件
git checkout -- . 或git checkout . 取消本地所有的修改


git cat-file -p HEAD

git rev-parse HEAD master
查看HEAD和master对应的提交ID

git stash list 查看保存的进度
git stash pop 从最近的保存回复进度
git stash pop [--index] [<stash>]
git stash save 这个命令是git stash 命令的完整版，即如果需要在保存工作中进度的时
候使用指定的说明
eg: git stash save "message.."

git stash apply [--index] [<stash>] 除了不删除恢复的进度之外，其余和git pop命令
一样

git drop stash [<stash>]  删除一个存储进度。默认删除最新的存储进度
git stash branch <branchname> <stash> 基于进度创建分支

git reflog show refs/stash
git stash apply stash@{1}

`git --exec-path`查看git安装在哪里


`git ls-files`查看暂存区中的文件


`cat > .gitignore <<EOF`配置要忽略的文件
同时也可以在.gitignore中添加对自己的忽略

`git status --ignored 查看被忽略的文件`

可以通过配置设置一个全局的忽略文件

`git cofig --global core.excludesfile filename`

git archive 将当前的项目归档，会自动除去.git文件
`git archive -o latest.tar HEAD`
