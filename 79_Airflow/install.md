# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow[postgres]

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8003

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page


#Install packages
pip install 'apache-airflow[gcp]'




export AIRFLOW_HOME=/home/danny/airflow
pip install apache-airflow[postgres,gcp]
pip3 install werkzeug==0.15.4
airflow initdb
airflow webserver -p 8003


# Start Scheduler
airflow scheduler

# API

For example latest run

curl http://localhost:8003/api/experimental/latest_runs




# Systemd


sudo cp airflow-webserver.service /lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl disable airflow-webserver.service
sudo systemctl start airflow-webserver.service
sudo systemctl status airflow-webserver.service



sudo systemctl stop airflow-webserver
sudo systemctl stop airflow-scheduler


sudo cp airflow-scheduler.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl disable airflow-scheduler.service
sudo systemctl start airflow-scheduler.service
sudo systemctl status airflow-scheduler.service
sudo systemctl stop airflow-scheduler.service















#Update 

docker ps

docker run --name pgadmin -p 5050:5050 --network=host\
        -e "PGADMIN_DEFAULT_EMAIL=danny.rasch@outlook.com" \
        -e "PGADMIN_DEFAULT_PASSWORD=alfonstini" \
        -e "PGADMIN_LISTEN_PORT=5050" \
        -d dpage/pgadmin4 \
        -v "/home/danny/docker/volumes/pgadmin:/var/lib/pgadmin/shared"

## Pull
docker pull dpage/pgadmin4

docker stop pgadmin
docker rm pgadmin

# NEW
https://info.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker
mkdir postgres
cd postgres

docker volume create --driver local --name=pgvolume
docker volume create --driver local --name=pga4volume

docker network create --driver bridge pgnetwork

cat << EOF > pg-env.list
PG_MODE=primary
PG_PRIMARY_USER=postgres
PG_PRIMARY_PASSWORD=alfonstini
PG_DATABASE=testdb
PG_USER=insider_danny
PG_PASSWORD=alfonstini
PG_ROOT_PASSWORD=alfonstini
PG_PRIMARY_PORT=5435
EOF

cat << EOF > pgadmin-env.list
PGADMIN_SETUP_EMAIL=danny.rasch@outlook.com
PGADMIN_SETUP_PASSWORD=alfonstini
SERVER_PORT=5050
EOF

docker run --publish 5435:5432 \
  --volume=pgvolume:/pgdata \
  --env-file=pg-env.list \
  --name="postgres_new" \
  --hostname="postgres" \
  --network="pgnetwork" \
  --detach \
postgres

docker run --publish 5051:5050 \
  --volume=pga4volume:/var/lib/pgadmin \
  --env-file=pgadmin-env.list \
  --name="pgadmin4_new2" \
  --hostname="pgadmin4" \
  --network="pgnetwork" \
  --detach \
dpage/pgadmin4