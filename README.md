# CPU Utilization Service


## Install project

1. `git clone https://github.com/varfigstar/cpu_utilization_service.git` 

2. Create virtual env: `python3 -m vevn env`

3. Install packages: `env/bin/python -m pip install -r requirements.txt`

### Run backend

With command `env/bin/python cpu_utilization_service/manage.py runserver`


### Run client service

Edit `client/cpu_utilization.service` file

Run command `cp client/cpu_utilization.service /etc/systemd/system/cpu_util.service`

Enable service: `systemctl enable cpu_util.service`

Start service: `systemctl start cpu_util.service`