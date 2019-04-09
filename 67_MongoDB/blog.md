# Docker: PostgreSQL 10 and pgAdmin 4

## Run Docker with PostgreSQL container

Make persistent volume to store config files and database files:

>mkdir -p $HOME/docker/volumes/postgres

Rund docker command to create postgresql database with User: postgres and POSTGRES_PASSWORD=docker:
# Exucute postgresql 



>docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5434:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres




### Install Docker Compose
This is the new stuff! Docker Compose helps you to run a network of several containers all at once thanks to configuration files instead of providing all arguments in Docker’s command line interface. It makes it easier to manage your containers as command lines can become very long and unreadable due to the high number of arguments.

Execute the following command in a terminal window to install it.

$ sudo apt install docker-compose

### Docker compose/stack

docker stack deploy -c stack.yml mongo

OR

docker-compose -f stack.yml up



docker exec -it 67_mongodb_mongo_1 /bin/bash


owever, if you want to see the mongo's admin web page, you could do it, with this command:

mongod --rest --httpinterface

browsing this url: http://localhost:28017/

the parameter httpinterface activate the admin web page, and the parameter rest its needed for activate the rest services the page require
