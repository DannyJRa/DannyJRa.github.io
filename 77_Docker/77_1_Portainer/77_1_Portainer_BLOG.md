---
title: Portainer
author: DannyJRa
date: '2019-05-21'
slug: portainer
categories:
  - Python
tags:
  - Engineering
hidden: false
image: "img/77_portainer_BLOG.png"
share: false
output:
  html_document:
    keep_md: yes
    includes:
      #before_body: header.html
      #after_body: footer.html
    theme: cerulean
    highlight: tango
    code_folding: show
    toc: yes
    toc_float: yes
  pdf_document:
    number_sections: yes
geometry: margin = 1.2in
fontsize: 10pt
always_allow_html: yes

---










<a href="https://github.com/DannyJRa/DannyJRa.github.io/tree/master/77_Docker/77_1_Portainer/" target="_blank"><img src="img/forkme_right_orange_ff7600.svg" style="position:absolute;top:1;right:0;" alt="Fork me on GitHub"></a>


# Portainer: Managing Docker Containers

Although I’m comfortable with the command line, it is nice to have a GUI to manage the containers. 

Portainer is an open-source management UI for Docker, including Docker Swarm environment. Portainer makes it easier for you to manage your Docker containers, it allows you to manage containers, images, networks, and volumes from the web-based Portainer dashboard.

## Prerequisites

- Ubuntu 18
- Root privielges
- docker

## What we will do

- Install and Configure Portainer
- Docker Environment Management

# What is Portainer?[^1]

>Portainer is an open-source web-based management user interface for Docker. It allows you to manage images, networks, and volumes in addition to containers. One really cool thing about Portainer is that it is a Docker container itself!

## How Do You Install Portainer?

Portainer is easy to install because it is a Docker container. If you’ve installed other Docker containers (and if you haven’t you’re probably not interested in a Docker container management tool) this is just as easy. Assuming you already have Docker installed, create a volume and run the container:

```bash
docker volume create portainer_data
docker run -d -p 8999:8999 --name portainer2 --restart always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $HOME/docker/volumes/portainer:/data portainer/portainer
```

Portainer is now running as a container, check it using the docker ps command.

```bash
docker ps
```

And you will get the result as below.
#TODO
Screenshot

You can then access the UI at http://yourip:9000/ and see a screen similar to:
#TODO
Portainer Home Screen

Next, we will configure the Admin password for the Portainer.

Open your web browser and type the server IP address with port 9000.

http://192.168.33.10:9000/

You will get the page about the admin user and password configuration.

Portainer UI

Type your strong admin password and click the 'Create user' button.

Now we need to define which environment Portainer will connect. Portainer offers support for standalone Docker environment, Docker Swarm, and Swarm mode.

## What Can You Do With Portainer?
I won’t pretend to be an expert, but there are few features that caught me eye as a novice to Docker:

- Start, stop, remove and create containers
- Open up a console for direct command line interface with containers
- Manage images (download, delete, etc.)
- View container logs

In addition to viewing container information, you can also see stats like memory usage and process utilization:

- Container stats
- Container Memory and CPU Utilization

One really useful feature is the ability to recreate a container. Images for containers are updated all the time. In order to update your container with a new image you usually have to:

- Stop the container
- Remove the container
- Pull a new image
- Recreate and run the container with the same options as before
  
This isn’t too complicated, but it can get tedious for frequently updated containers. Portainer allows you to do this all in one click with the Recreate functionality. See the recreate button in image below:
#TODO
Portainer Container Screen

## Final Thoughts

It is very convinient to have a centralized web-based management and monitoring tool for all of my Docker containers, images, volumes, and network settings. 


[^1]: References ttps://portainer.readthedocs.io/en/stable/

Original post on Github Pages: <a href="https://dannyjra.github.io/77_Docker/77_1_Portainer/77_1_Portainer_BLOG.html" target="_blank">https://dannyjra.github.io/77_Docker/77_1_Portainer/77_1_Portainer_BLOG.html</a>

