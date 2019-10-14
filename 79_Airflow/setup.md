airflow webserver -p 8003


https://airflow.apache.org/start.html
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)


sudo su

apt update
apt upgrade

apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev postgresql-client

pip3 install virtualenv

cd /srv
virtualenv airflow
cd airflow
source bin/activate
export AIRFLOW_HOME=/home/danny/airflow 
airflow --disabled-login --disabled-password --gecos "Airflow system user"

# With activated virtual environement
export SLUGIFY_USES_TEXT_UNIDECODE=yes
pip install apache-airflow[postgres,crypto]==1.10.5


chown airflow.airflow . -R
chmod g+rwx . -R



sudo su airflow
cd /srv/airflow
source bin/activate
#export AIRFLOW_HOME=/srv/airflow
export AIRFLOW_HOME=/home/danny/airflow
export AIRFLOW__WEBSERVER__RBAC=true
airflow initdb

sudo nano /srv/airflow/airflow.cfg

sql_alchemy_conn = postgresql+psycopg2://airflow-user:airflowInsider@localhost:5434/airflow

sudo nano /srv/airflow/webserver_config.py

airflow initdb

# Creat new airflow admin user

Add a new airflow admin user (activated virtual environment):

airflow create_user -r Admin -u danny -e danny.rasch@outlook.com -f Danny -l Snow
You can now start the airflow web server:
test123
airflow webserver -p 8002
and scheduler:

sudo su


cd /srv/airflow

source bin/activate
airflow scheduler


# First dag

python /home/danny/airflow/dags/Tut1.py
cd /home/danny/airflow/dags
airflow list_tasks
airflow list_tasks Tut1

airflow list_tasks tut1 --tree

airflow test tutorial print_date 2015-06-01
airflow test tutorial templated 2015-06-01

airflow webserver -p 8003

#Startup at boot
https://medium.com/grensesnittet/install-apache-airflow-on-a-google-cloud-platform-virtual-machine-f9a5b01b6c33
sudo systemctl enable airflow-webserver.service


#REST API
Source: https://airflow.apache.org/api.html#endpoints

curl -X POST \
  http://localhost:8080/api/experimental/dags/<DAG_ID>/dag_runs \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"conf":"{\"key\":\"value\"}"}'

curl -X GET \
  http://localhost:8003/api/experimental/latest_runs 


docker stop 78_airflow_webserver_1
docker stop 78_airflow_webserver_1
docker image ls

docker rmi 3e0a97163722

docker rm 8819a15a6c16

docker images -a

Purging All Unused or Dangling Images, Containers, Volumes, and Networks
Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are dangling (not associated with a container):

docker system prune
To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:

docker system prune -a






