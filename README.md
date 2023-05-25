
# ZK monitor

1 - pip install -r requirements.txt

2 - pip install supervisor

3 - setup the supervisord.conf with every machine section

4 - Run with :  "supervisord -c  supervisord.conf"




pour demarer comme systeme


1 - sudo touch /etc/systemd/system/supervisord.service


2 Add contents

[Unit]

Description=Supervisor daemon

Documentation=http://supervisord.org

After=network.target



[Service]

ExecStart=/usr/local/bin/supervisord -n -c PATH  ##path to supervisord.conf

ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown

ExecReload=/usr/local/bin/supervisorctl $OPTIONS reload

KillMode=process

Restart=on-failure

RestartSec=42s

[Install]

WantedBy=multi-user.target

Alias=supervisord.service
