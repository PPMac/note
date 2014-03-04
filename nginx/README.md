# Nginx 学习笔记

## 安装openresty

> http://openresty.org/#Installation

下载openrestry安装包, 解压后执行如下命令安装

```bash
sudo apt-get install libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make

$ ./configure --with-luajit
```

如果报下面的错误

<pre>
platform: linux (linux)
    you need to have ldconfig in your PATH env when enabling luajit.
</pre>

是因为找不到命令ldconfig, 这个命令一般是在/sbin/目录下的，所以先执行

```bash
export PATH=$PATH:/sbin
```

然后再执行
```
make
sudo make install
```
