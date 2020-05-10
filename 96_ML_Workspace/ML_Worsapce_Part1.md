---
output:
  html_document:
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

```{r cache, include=FALSE}
#Caching of all chunks
knitr::opts_chunk$set(cache=TRUE)
# Ten things you can do on the Windows Data Science Virtual Machine
```



>The Windows Data Science Virtual Machine (DSVM) is a powerful data science development environment that enables you to perform various data exploration and modeling tasks. The environment comes already built and bundled with several popular data analytics tools that make it easy to get started quickly with your analysis for On-premises, Cloud or hybrid deployments. The DSVM works closely with many Azure services and is able to read and process data that is already stored on Azure, in Azure SQL Data Warehouse, Azure Data Lake, Azure Storage, or in Azure Cosmos DB. It can also leverage other analytics tools such as Azure Machine Learning and Azure Data Factory.[^1]

# ML Workspace

https://github.com/ml-tooling/ml-workspace#faq

# Spark

docker run -d -p 8891:8080 --name "WS_spark3" -v "${PWD}:/workspace" mltooling/ml-workspace-spark:latest

docker stop "WS_spark3"


# Add new workspace

docker run -p 8891:8080 mltooling/ml-workspace:latest

docker run -d -p 8891:8080 --name "ml-workspace2" -v "${PWD}:/workspace" mltooling/ml-workspace:latest


docker build -t workspace .


```{r, eval=F}
docker run -p 5763:8080 --name "ml-workspace12" -v "/home/dannyOneDrive/DataScience/41_DannyJRa.github.io/96_ML_Workspace/test:/root/Documents" mltooling/ml-workspace-spark:latest
```
where ...

cd /home/danny/OneDrive/DataScience/41_DannyJRa.github.io/96_ML_Workspace/Root_Workspace/ && ls -a

## File permissions

The whole issue with file permissions in docker containers comes from the fact that the Docker host shares file permissions with containers (at least, in Linux). Let me remind you here that file permissions on bind mounts are shared between the host and the containers (of course, there are also a few other ways that file permissions are transferred between host and containers). Whenever we create a file on host using a user with UID x, this files will have x as owner UID inside the container, too. And this will happen no matter if there is a user with UID equal to x inside the container. The same holds whenever a file is created inside the container by a user with UID equal to y (or a process running under this user). This file will appear on the host with owner UID equal to y.[^2]











$ docker run -it --rm -v ~/alpine/appdir:/workdir --workdir /workdir  --user $(id -u) local_alpine touch alpinefile


docker run -p 8080:8080 

docker stop "ml-workspace3"



# Spark

>docker run -d -p 8891:8080 --name "WS_spark3" -v "${PWD}:/workspace" mltooling/ml-workspace-spark:latest

docker stop "WS_spark3"

### Start R server

```{r, eval=F}
cmd <- paste(ssh, "sudo rstudio-server start")
(b<-system(cmd, intern=TRUE))
```

Remove folder if create already

```{r, eval=F}
cmd <- paste(ssh, "sudo rm -r /home/insider/R")
cmd

b<-system(cmd, intern=TRUE)
```

Create folder

```{r, eval=F}
cmd <- paste(ssh, "sudo mkdir /home/insider/R")
cmd

b<-system(cmd, intern=TRUE)
```

Mount drive

```{r, eval=F}
cmd <- paste(ssh, "sudo mount /dev/sdd /home/insider/R")
cmd

b<-system(cmd, intern=TRUE)
```


```{r, eval=F}
browseURL(paste0("http://",ip,":8787"))
```


#2.  Use a Jupyter notebook to experiment

Simply open browser with port 8000 to open Juypter Hub. 
```{r, eval=F}
browseURL(paste0("https://",ip,":8000"))
```

Enter your ID and password and will see ...

![Juypter Hub](img/jupyter_hub_BLOG.png)



... to be continued

[^1]: Addopted from https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/vm-do-ten-things

[^2]: Addopted from https://blog.gougousis.net/file-permissions-the-painful-side-of-docker/