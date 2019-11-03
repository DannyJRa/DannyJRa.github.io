docker pull amancevice/superset

docker run -d -p 8891:8088 --name "superset" amancevice/superset

Volumes
The image defines two data volumes: one for mounting configuration into the container, and one for data (logs, SQLite DBs, &c).

The configuration volume is located alternatively at /etc/superset or /home/superset; either is acceptable. Both of these directories are included in the PYTHONPATH of the image. Mount any configuration (specifically the superset_config.py file) here to have it read by the app on startup.

The data volume is located at /var/lib/superset and it is where you would mount your SQLite file (if you are using that as your backend), or a volume to collect any logs that are routed there. This location is used as the value of the SUPERSET_HOME environmental variable.


Database Initialization
After starting the Superset server, initialize the database with an admin user and Superset tables using the superset-init helper script:

docker run --detach --name superset [options] amancevice/superset
docker exec -it superset superset-init


# Manuell

# Install superset
pip install superset

# Initialize the database
superset db upgrade

# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
export FLASK_APP=superset
flask fab create-admin

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# To start a development web server on port 8088, use -p to bind to another port
superset run -p 8891 --with-threads --reload --debugger


After installation, you should be able to point your browser to the right hostname:port http://localhost:8088, login using the credential you entered while creating the admin account, and navigate to Menu -> Admin -> Refresh Metadata. This action should bring in all of your datasources for Superset to be aware of, and they should show up in Menu -> Datasources, from where you can start playing with your data!
