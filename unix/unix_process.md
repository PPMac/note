3. 进程皆有标识

获取当前进程pid
os.getpid()

bash中 $$ 变量也表示当前的PID

4. 进程皆有父

获取父进程ppid
os.getppid()


5. 进程皆有文件描述符

f = open('/tmp/a')
print f.fileno()

6. 进程皆有资源限制

https://docs.python.org/2.7/library/resource.html

获取当前线程允许获取的最大文件描述符个数

import resource
print resource.getrlimit(resource.RLIMIT_NOFILE)

7. 进程皆有环境

8. 进程皆有参数

import sys
print sys.argv

9. 进程皆有名

10. 进程皆有退出码

11. 进程皆可衍生

import os
print "parent process id %d" % os.getpid()
if os.fork():
        print "enter if block process id %d" % os.getpid()
else:
        print "enter else block process id %d" % os.getpid()

// 输出
parent process id 22517
enter if block process id 22517
enter else block process id 22518

子进程从父进程处继承了其从内存中占用的所有内容，以及所有属于父进程的文件描述符。
如果一个占用了500M内存的进程fork出一个子进程，那么就有1G的内存被暂用，多操作几次，便很快会浩进内存，这就是fork炸弹

一个bash的fork炸弹
:(){ :|:& };:

12. 孤儿进程

import os
import time

print "prants process id %d" % os.getpid()

if os.fork() == 0:
        time.sleep(2)
        print "enter if block process id %d" % os.getpid()
print "parents died id %d" % os.getpid()

上面的命令会在主进程结束之后，再继续输出子进程的结果。

当父进程结束之后，子进程仍然安然无恙，操作系统并不会对子进程区别对待。因此父进程结束之后子进程照常运行，父进程不可能带着子进程同归于尽

那么如何管理子进程呢?

第一个是守护进程，守护进程是一种长期运行的进程，为了能够一直保持运行，它有意与孤儿进程存在。
另一个是与脱离终端会话的进程通信，可以通过Unix信号来做到这一点。

13. 友好的进程

当衍生一个子进程时， 它包含了父进程在内存中的一切，实实在在复制所有的数据产生的系统开销不容小觑，因此现代的Unix系统采用写时复制(copy-on-write, CoW)来克服这个问题，
CoW将实际的内存复制推迟到了需要真正写入的时候，所以说父进程和子进程实际上是在共享内存中的数据，直到它们其中的一个需要对数据进行修改时，才会进行内存复制，使得两个进程保持适当的距离。

14. 看顾

父进程等待所有子进程完成:
import os
import time
import random
import sys
for i in range(3):
    if os.fork() == 0:
        time.sleep(random.randint(1, 5))
        print "I am an orphan with pid %d" % os.getpid()
        sys.exit(0)

os.wait()
print "parent died id %d" % os.getpid()

输出:
I am an orphan with pid 14330
I am an orphan with pid 14329
I am an orphan with pid 14328
parent died id 14327

利用返回值，检查到底哪些子进程退出了。

import os
import time
import random
import sys
for i in range(3):
    if os.fork() == 0:
        time.sleep(random.randint(1, 5))
        print "I am an orphan with pid %d" % os.getpid()
        sys.exit(0)

for i in range(3):
    pid, status = os.wait()
    print pid, status
print "parent died id %d" % os.getpid()

输出：
I am an orphan with pid 14646
I am an orphan with pid 14645
I am an orphan with pid 14647
14646 0
14645 0
14647 0
parent died id 14644

竞争条件：
当一个子进程退出时，处理某个退出进程的代码还在运行，这时会怎么样？如果我还没有来得及从os.wait()返回，另一个进程也退出了会怎么样？

import os
import time
import sys
for i in range(3):
    if os.fork() == 0:
        # 子进程立即退出
        print "I am an orphan with pid %d" % os.getpid()
        sys.exit(0)

# 父进程等待第一个子进程退出然后休眠5秒
# 期间第二个子进程也退出，不再运行
pid, status = os.wait()
print pid, status
time.sleep(5)

# 父进程再一次等待，第二个子进程的退出信息加入队列并在此返回
pid, status = os.wait()
print pid, status
time.sleep(5)

pid, status = os.wait()
print pid, status
time.sleep(5)
print "parent died id %d" % os.getpid()

内核将退出信息加入队列，这样一来父进程总是能够按照子进程退出的顺序接受信息

15. 僵尸进程

从14中最后一个例子可以看出，如果没有调用os.wait().内核会一直保存已退出的子进程状态信息，直到父进程使用os.wait()来请求这些信息，如果父进程一直不发出请求，那么这些状态信息就会被内核一直保留着。所以任何子进程如果在结束之时父进程仍在运行，那么这个子进程很快就会变成为僵尸进程。


16. 进程皆可以获得信号

os.wait是为父进程提供了一种很好的方法来管理子进程，但是它是一个阻塞调用：直到子进程结束，调用才返回。可是并不是每一个父进程都有闲暇一直等子进程结束。此时可以用Ｕnix信号。

这里有一点需要注意:
因为信号可以在任意时间到达，所以一定要等待处理了CHLD的信号个数等于衍生的子进程个数，不然会出现僵尸进程。
如果按照下面这种方式写的话：

import os
import time
import sys
import signal


def handler(signum, frame):
    pid, status = os.wait()
    print "pid: %d, status: %d" % (pid, status)

# 衍生３个子进程
for i in range(3):
    if os.fork() == 0:
        # 子进程立即退出
        print "I am an orphan with pid %d" % os.getpid()
        time.sleep(3)
        sys.exit(0)
signal.signal(signal.SIGCHLD, handler)

while True:
    print "father %d do something" % os.getpid()
    time.sleep(5)

输出：
I am an orphan with pid 24300
father 24299 do something
I am an orphan with pid 24301
I am an orphan with pid 24302
pid: 24300, status: 0
father 24299 do something
father 24299 do something
father 24299 do something

可以猜测子进程24301, 24302的CHLD信号在handler函数运行完之后发来，因此没法捕获。

正确写法应该是：
import os
import time
import sys
import signal

child_processes = 3
dead_processes = 0


def handler(signum, frame):
    global dead_processes
    while True:
        if dead_processes == child_processes:
            break
        pid, status = os.wait()
        dead_processes += 1
        print "pid: %d, status: %d" % (pid, status)
        print "dead_processes: %d" % dead_processes

# 衍生３个子进程
for i in range(3):
    if os.fork() == 0:
        # 子进程立即退出
        print "I am an orphan with pid %d" % os.getpid()
        time.sleep(3)
        sys.exit(0)
signal.signal(signal.SIGCHLD, handler)

while True:
    print "father %d do something" % os.getpid()
    time.sleep(5)

输出是：
I am an orphan with pid 24404
father 24403 do something
I am an orphan with pid 24405
I am an orphan with pid 24406
pid: 24405, status: 0
pid: 24404, status: 0
dead_processes: 2
pid: 24406, status: 0
dead_processes: 3
dead_processes: 1
father 24403 do something


信号入门

信号是一种异步通信机制，　当进程从内核那里收到信号的时候，它可以执行下列某一项操作：
１．忽略该信号
２．执行特定的动作
３．执行默认的操作

从技术上将，信号由内核发送，如同短信由手机用户发出一样。但短信有原始发送端，信号也是如此。
信号由一个进程发送到另一个进程，只不过借用内核作为中介。

进程间发送信息：
$ cat a.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

print os.getpid()
time.sleep(1000)

# 27334是上面脚本的pid
$ cat b.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import signal
os.kill(27334, signal.SIGTERM)

信号一览($ man 7 signal)

每一个信号都有默认的行为（Action）：
有如下一些Action:

Term   Default action is to terminate the process.

Ign    Default action is to ignore the signal.

Core   Default action is to terminate the process and  dump  core  (see core(5)).

Stop   Default action is to stop the process.

Cont   Default  action  is  to  continue the process if it is currently stopped.


Signal     Value     Action   Comment
──────────────────────────────────────────────────────────────────────
SIGHUP        1       Term    Hangup detected on controlling terminal
                                or death of controlling process
SIGINT        2       Term    Interrupt from keyboard
SIGQUIT       3       Core    Quit from keyboard
SIGILL        4       Core    Illegal Instruction
SIGABRT       6       Core    Abort signal from abort(3)
SIGFPE        8       Core    Floating point exception
SIGKILL       9       Term    Kill signal
SIGSEGV      11       Core    Invalid memory reference
SIGPIPE      13       Term    Broken pipe: write to pipe with no
                                readers
SIGALRM      14       Term    Timer signal from alarm(2)
SIGTERM      15       Term    Termination signal
SIGUSR1   30,10,16    Term    User-defined signal 1
SIGUSR2   31,12,17    Term    User-defined signal 2
SIGCHLD   20,17,18    Ign     Child stopped or terminated
SIGCONT   19,18,25    Cont    Continue if stopped
SIGSTOP   17,19,23    Stop    Stop process
SIGTSTP   18,20,24    Stop    Stop typed at tty
SIGTTIN   21,21,26    Stop    tty input for background process
SIGTTOU   22,22,27    Stop    tty output for background process

注意: The signals SIGKILL and SIGSTOP cannot be caught, blocked, or ignored.


暂时没有发现python 中如何处理忽略信号,　可以考虑使用atexit模块
<http://code.activestate.com/recipes/577997-handle-exit-context-manager/>

import os
import time
import signal


def handler(signum, frame):
    print 'xxxxxx'

print os.getpid()
signal.signal(signal.SIGINT, handler)
time.sleep(1000)
