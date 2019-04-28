---
title: "<center><div class='mytitle'>VS-Code as a Server</div></center>"
author: "<center><div class='mysubtitle'>See the original code on [github](https://github.com/codercom/code-server).[^1] This tip is part of DJRs [blog.dannyrasch.com](http://www.blog.dannyrasch.com/).</div></center>"
output:
  html_document:
      keep_md: yes
      css: www/style.css
      toc: FALSE
      includes: 
        before_body: www/header.html
---

<br><br>

<div class="mycontent">

------------

# 1. VS-Code as a Server


Visit this github repo [Github](https://github.com/codercom/code-server)

# 1.1  Download 

Copy and download latest version to folder: /vs-code


```bash
cd $HOME/vs-code

#Replace link with latest version
#wget https://github.com/codercom/code-server/releases/download/1.32.0-310/code-server-1.32.0-310-linux-x64.tar.gz
wget https://github.com/codercom/code-server/releases/download/1.939-vsc1.33.1/code-server1.939-vsc1.33.1-linux-x64.tar.gz
```

# 1.2 Unzip the tar.gz file


```bash
cd $HOME/vs-code
tar xvzf code-server1.939-vsc1.33.1-linux-x64.tar.gz
```


The file code-server is generated and you can execute the file by using following command


```bash
Usage
code-server --help
code-server can be ran with a number of arguments to customize your working directory, host, port, and SSL certificate.

USAGE
  $ code-server [WORKDIR]

ARGUMENTS
  WORKDIR  [default: (directory to binary)] Specify working dir

OPTIONS
  -d, --data-dir=data-dir
  -h, --host=host          [default: 0.0.0.0]
  -o, --open               Open in browser on startup
  -p, --port=port          [default: 8443] Port to bind on
  -v, --version            show CLI version
  --allow-http
  --cert=cert
  --cert-key=cert-key
  --help                   show CLI help
  --no-auth
  --password=password
```


# 1.3 Start VS-Code

I am using the following options to set the port, data dir of all extensions and user data and a password to login to the server as the current user:


```bash
$HOME/VSCode/code-server -p 8086 --data-dir=/home/danny/vs-code/data/ --password=${S_pwd_vscode}
```

- Set S_pwd_vscode accordingly
- Give current user access to directories
  sudo chown -R danny $HOME//vs-code/


# 2. Run at startup

# 2.1 Via Systemd

```
sudo nano /etc/systemd/system/vscode.service


Description=Nifi start

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/home/danny/vs-code/code-server /home/danny/DannyJRa.github.io/ -p 8085 --data-dir=/home/danny/vs-code/data/ --password=insider > /home/danny/vs-code/vscode.log 2>&1
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target



Reload services

sudo systemctl daemon-reload
Enable the service

sudo systemctl enable vscode
Start the service
sudo systemctl start vscode
Check the status of your service
systemctl status vscode
```

Reboot your device and the program/script should be running. If it crashes it will attempt to restart



# 2.2 User

You can also use systemctl --user for managing and configuring the service(s), which will operate on your user's service manager, not the one of the system.


dataflow.service
sudo nano /etc/systemd/system/dataflow.service
sudo rm /etc/systemd/system/nifi.service

/home/danny/nifi/nifi/bin/nifi.sh start



```bash
sudo systemctl enable nifi
```


Start the service
sudo systemctl start nifi
Check the status of your service
systemctl status nifi
service status nifi



# 2.3 Check if enabled


```bash
systemctl list-unit-files | grep enabled
```



[^1]: Binary of vs-code from [codercom](https://github.com/codercom/code-server)
