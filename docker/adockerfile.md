# dockerfile


- 创建dockerfile
```
docker build -f 文件名 -t 镜像名:1.0 .
```


- ubuntu示例dockerfile
```
FROM ubuntu:
MAINTAINER umas 1970313791@qq.com
LABEL version="1.0" description="umas个人测试镜像" by="umas "

RUN apt-get update \
&& apt-get install --no-install-recommends -y \
make \
build-essential \
openssh-server \
vim \
net-tools

RUN echo "root:umas1970" | chpasswd

EXPOSE 22 80 8080 8081 8082 8083 8084 8085

RUN echo "PermitRootLogin yes"        >> /etc/ssh/sshd_config \
&& echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config \
&& ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa \
&& /etc/init.d/ssh start 

CMD ["sh", "-c", "/etc/init.d/ssh start"]
```


