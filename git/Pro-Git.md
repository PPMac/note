## Pro Git Learn

* 初次运行git前的配置

系统级别：`git config --system` (配置文件保存在`/etc/gitconfig`)

用户级别：`git config --global` (配置文件保存在`~/.gitconfig`)

当前项目的配置文件保存在工作目录的`.git/config`文件中

如果上面的配置都存在的话，配置信息会依次覆盖，当前项目>用户级别>系统级别

配置文本编辑器（git commit时的文本编辑器很难用，用下面的配置使用VIM)

`git config --global core.editor vim`

配置差异分析工具
`git config --global merge.tool meld`

在有冲突时，使用`git mergetool`可以比较冲突


* 忽略某些文件

一般我们总会有些文件无需纳入Git的管理,也不希望它们总出现在未跟踪文件列表。通常都是些自动生
成的文件,像是日志或者编译过程中创建的等等。我们可以创建一个名为`.gitignore`的文件,列出要忽略的
文件模式,来看一个简单的例子

```
$ cat .gitignore
*.[oa]
*~
```

第一行告诉 Git 忽略所有以 .o 或 .a 结尾的文件。一般这类对象文件和存档文件都是编译过程中出现
的,我们用不着跟踪它们的版本。

第二行告诉 Git 忽略所有以波浪符(~)结尾的文件,许多文本编辑软件(比如 Emacs)都用这样的文件名保存副本。
此外,你可能还需要忽略 log,tmp 或者 pid 目录,以及自动生成的文档等等。

要养成一开始就设置好 .gitignore 文件的习惯,以免将来误提交这类无用的文件。

文件 .gitignore 的格式规范如下:

* 所有空行或者以注释符号 # 开头的行都会被 Git 忽略。
* 可以使用标准的 glob 模式匹配。
* 匹配模式最后跟反斜杠(/)说明要忽略的是目录。
* 要忽略指定模式以外的文件或目录,可以在模式前加上惊叹号(!)取反。

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。

<pre>
星号(*)匹配零个或多个任意字符

[abc] 匹配任何一个列在方括号中的字符(这个例子要么匹配一个 a,要么匹配一个 b,要么匹配一个 c)

问号(?)只匹配一个任意字符

如果在方括号中使用短划线分隔两个字符,表示所有在这两个字符范围内的都可以匹配, (比如[0-9]表示匹配所有 0 到 9 的数字)。
</pre>

我们再看一个 .gitignore 文件的例子:

<pre>
# 此为注释 – 将被 Git 忽略
*.a # 忽略所有 .a 结尾的文件
!lib.a # 但 lib.a 除外
/TODO # 仅仅忽略项目根目录下的 TODO 文件,不包括 subdir/TODO
build/ # 忽略 build/ 目录下的所有文件
doc/*.txt # 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
</pre>


* 比较文件

git diff
git diff --cached


* 重命名文件

git mv
就相当于运行了下面三条命令:
```
$ mv README.txt README
$ git rm README.txt
$ git add README
```
* 提交记录查看

git log -p（显示每次提交的详细信息）

git log -p -2 （显示最近两次提交的信息）

git log --stat


| 选项                |  说明
| ------------------- | -----------------------------------
| -p                  |  按补丁格式显示每个更新之间的差异。
| --stat              |  显示每次更新的文件修改统计信息。
| --shortstat         |  只显示 --stat 中最后的行数修改添加移除统计。
| --name-only         |  仅在提交信息后显示已修改的文件清单。
| --name-status       |  显示新增、修改、删除的文件清单。
| --abbrev-commit     |  仅显示 SHA-1 的前几个字符,而非所有的 40 个字符。
| --relative-date     |  使用较短的相对时间显示(比如,“2 weeks ago”)。
| --graph             |  显示 ASCII 图形表示的分支合并历史。
| --pretty            |  使用其他格式显示历史提交信息。可用的选项包括 oneline,short,full,fuller 和 format(后跟指定格式)。
| -(n)                |  仅显示最近的 n 条提交
| --since, --after    |  仅显示指定时间之后的提交。
| --until, --before   |  仅显示指定时间之前的提交。
| --author            |  仅显示指定作者相关的提交。
| --committer         |  仅显示指定提交者相关的提交。


git log --pretty=format指定显示格式

git log --pretty=format:"%h - %an, %ar : %s"

| 选项    |  说明
| ------- | ----------------------------------------
| %H      |  提交对象(commit)的完整哈希字串
| %h      |  提交对象的简短哈希字串
| %T      |  树对象(tree)的完整哈希字串
| %t      |  树对象的简短哈希字串
| %P      |  父对象(parent)的完整哈希字串
| %p      |  父对象的简短哈希字串
| %an     |  作者(author)的名字
| %ae     |  作者的电子邮件地址
| %ad     |  作者修订日期(可以用 -date= 选项定制格式)
| %ar     |  作者修订日期,按多久以前的方式显示
| %cn     |  提交者(committer)的名字
| %ce     |  提交者的电子邮件地址
| %cd     |  提交日期
| %cr     |  提交日期,按多久以前的方式显示
| %s      |  提交说明

来看一个实际的例子,如果要查看 Git 仓库中,2008 年 10 月期间,Junio Hamano 提交的但未合并的测
试脚本(位于项目的 t/ 目录下的文件),可以用下面的查询命令:

```
$ git log --pretty="%h:%s" --author=gitster --since="2008-10-01" \
--before="2008-11-01" --no-merges -- t/
5610e3b - Fix testcase failure when extended attribute
acd3b9e - Enhance hold_lock_file_for_{update,append}()
f563754 - demonstrate breakage of detached checkout wi
d1a43f2 - reset --hard/read-tree --reset -u: remove un
51a94af - Fix "checkout --track -b newbranch" on detac
b0ad11e - pull: allow "git pull origin $something:$cur
```

* 修改最后一次的提交信息或添加几个遗忘的文件的

`git commit --amend`


* git 打标签

列出标签：`git tag`

git使用的标签有两种类型:轻量级的(lightweight)和含附注的(annotated)。

轻量级标签就像是个不会变化的分支,实际上它就是个指向特定提交对象的引用。

而含附注标签,实际上是存储在仓库中的一个独立对象,它有自身的校验和信息,包含着标签的名字,电子邮件地址和日期,以及标签说明,标签本身也允许使
用 GNU Privacy Guard (GPG) 来签署或验证。

一般我们都建议使用含附注型的标签,以便保留相关信息;当然,如果只是临时性加注标签,或者不需要旁注额外信息,用轻量级标签也没问题。

**含附注的标签**

创建一个含附注类型的标签非常简单,用-a(annotated的首字母)指定标签名字即可:
```
$ git tag -a v1.4 -m 'my version 1.4'
$ git tag
v0.1
v1.3
v1.4
```

而-m选项则指定了对应的标签说明,Git 会将此说明一同保存在标签对象中。如果在此选项后没有给出具
体的说明内容,Git 会启动文本编辑软件供你输入。
可以使用
`git show`
命令查看相应标签的版本信息,并连同显示打标签时的提交对象。

**签署标签**

如果你有自己的私钥,还可以用 GPG 来签署标签,只需要把之前的-a改为-s(Signed 的首字母)即可:

**轻量级标签**

轻量级标签实际上就是一个保存着对应提交对象的校验和信息的文件。要创建这样的标签,一个选项都不用,直接给出标签名字即可

**后期加注标签**

`git tag -a v1.2 "要添加标签那次提交的hash值"`


**分享标签**

默认情况下,git push并不会把标签传送到远端服务器上,只有通过显式命令才能分享标签到远端仓库。其
命令格式如同推送分支,运行
```
$ git push origin [tagname]
$ git push origin v1.5
```

如果要一次推送所有(本地新增的)标签上去,可以使用--tags选项:
`git push origin --tags`


* git自动补全

下载git源码`git clone git://git.kernel.org/pub/scm/git/git.git`

将源码源码目录下的`git/contrib/completion/git-completion.bash`

添加到~/.bashrc中也可以为系统上所有用户都设置默认使用此脚本。复制到`/etc/bash_completion.d/`目录中即可


* Git 命令别名

Git 并不会推断你输入的几个字符将会是哪条命令,不过如果想偷懒,少敲几个命令的字符,可以用设置别名。
来看看下面的例子:
```
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
可以看出,实际上 Git 只是简单地在命令中替换了你设置的别名。不过有时候我们希望运行某个外部命
令,而非 Git 的附属工具,这个好办,只需要在命令前加上`!`就行。如果你自己写了些处理 Git 仓库信息
的脚本的话,就可以用这种技术包装起来。

作为演示,我们可以设置用git visual启动gitk:
`git config --global alias.visual "!gitk"`

查看各个分支最后一次 commit 信息,运行
`git branch -v`


`git fetch origin`会拉去远程服务器的信息，包括新建的分支

切换到远程服务器的某个分支

```
git checkout -b serverfix origin/serverfix

git checkout -b [分支名] [远程名]/[分支名]
等效于
git checkout --track [远程名]/[分支名]
```


**删除远程分支**

如果不再需要某个远程分支了,比如搞定了某个特性并把它合并进了远程的master分支（或
稳定代码的地方),可以用这个非常无厘头的语法来删除它:
```
git push [远程名] :[分支名]
```

如果想在服务器上删除serverfix分支(或任何其他存放分支,运行下面的命令:
```
$ git push origin :serverfix
To git@github.com:schacon/simplegit.git
- [deleted]
serverfix
```

咚!服务器上的分支没了。你最好特别留心这一页,因为你一定会用到那个命令,而且你很可能会忘掉它的
语法。有种方便记忆这条命令的方法:记住我们不久前见过的
```
git push [远程名] [本地分支]:[远程分支]
```
如果省略[本地分支],那就等于是在说“在这里提取空白然后把它变成[远程分支]”。


一个分支整合到另一个分支的办法有两种: merge(合并)和rebase(衍合)
```
$ git checkout experiment
$ git rebase master
```
