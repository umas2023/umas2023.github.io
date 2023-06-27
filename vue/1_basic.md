# vue基本操作

- 推荐使用docker
```
docker pull vuejs/ci
sudo docker run -itd --name vue -p 11122:22 vuejs/ci /bin/bash
sudo docker exec -it vue  /bin/bash
apt update
apt install openssh-server
echo "root:umas1970" | chpasswd
echo "PermitRootLogin yes"        >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
npm install -g @vue/cli
```

