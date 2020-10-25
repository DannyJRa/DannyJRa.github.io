# Turning it into a service

Let’s create a file called 

sudo nano /etc/systemd/system/glances.service

cd /etc/systemd/system/


[Unit]
Description=Glances
After=network.target

[Service]
ExecStart=/usr/local/bin/glances -w
Restart=on-abort
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target

sudo systemctl enable glances.service

sudo systemctl start glances.service



