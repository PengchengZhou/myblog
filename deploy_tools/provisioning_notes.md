## 需要安装的包

* nginx
* python3
* git
* pip
* virtualenv

以ubuntu为例,可以执行下面的命令安装:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## 配置nginx虚拟主机

* 参考nginx.template.conf

## upstart任务

* 参考gunicorn-upstart.template.conf

## 文件夹结构

假设有用户账户,home目录为/home/username

/home/username/
    myblog/
        database/
        source/
        static/
        virtualenv/
