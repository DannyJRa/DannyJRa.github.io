---
title: DSVM Part1
author: DannyJRa
date: '2018-06-07'
slug: dsvwpart1
categories:
  - Cloud
tags:
  - Azure
hidden: false
image: "img/07_DSVM_Part1_BLOG.jpg"
share: false
output:
  html_document:
    keep_md: yes
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




DSVM Part 1 ...
 
<!--more-->











>The Windows Data Science Virtual Machine (DSVM) is a powerful data science development environment that enables you to perform various data exploration and modeling tasks. The environment comes already built and bundled with several popular data analytics tools that make it easy to get started quickly with your analysis for On-premises, Cloud or hybrid deployments. The DSVM works closely with many Azure services and is able to read and process data that is already stored on Azure, in Azure SQL Data Warehouse, Azure Data Lake, Azure Storage, or in Azure Cosmos DB. It can also leverage other analytics tools such as Azure Machine Learning and Azure Data Factory.[^1]

In this article, I will adopt the tutorial to needs and learn how to use Azure (Linux) DSVM to perform various data science tasks and interact with other Azure services. Here are some of the things you can do on the DSVM:

1. Explore data and develop models locally on the DSVM using RStudio
2.  Use a Jupyter notebook to experiment with your data on a browser using Python 2, Python 3, Microsoft R an enterprise ready version of R designed for performance
3. Deploy models built using R and Python on Azure Machine Learning so client applications can access your models using a simple web service interface
4. Administer your Azure resources using Azure portal or Powershell
5. Extend your storage space and share large-scale datasets / code across your whole team by creating an Azure File storage as a mountable drive on your DSVM
6. Share code with your team using GitHub and access your repository using the pre-installed Git clients - Git Bash, Git GUI.
7. Access various Azure data and analytics services like Azure blob storage, Azure Data Lake, Azure HDInsight (Hadoop), Azure Cosmos DB, Azure SQL Data Warehouse & databases
8. Build reports and dashboard using the Power BI Desktop pre-installed on the DSVM and deploy them on the cloud
9. Dynamically scale your DSVM to meet your project needs
10. Install additional tools on your virtual machine


#1. Explore data and develop models locally on the DSVM using RStudio or Python

## Using RStudio Server


Prerequiesites are the set-up of Azure services, as accroind to Blog: ....

### Find the ip-adress of the DSVM e.g. by usins CLI 2.0

```r
library(jsonlite)
code="az vm list-ip-addresses"
a<-fromJSON(system(code,intern = TRUE))

a<-write(system(code,intern = TRUE),"test.json")
yelp <- fromJSON(file("test.json"))


yelp_flat <- jsonlite::flatten(yelp)
str(yelp_flat)
```

```
## 'data.frame':	2 obs. of  4 variables:
##  $ virtualMachine.name                      : chr  "adminWorkstation" "djrtest3685445209ac"
##  $ virtualMachine.resourceGroup             : chr  "ADMIN" "ml"
##  $ virtualMachine.network.privateIpAddresses:List of 2
##   ..$ : chr "10.0.0.4"
##   ..$ : chr "10.0.0.4"
##  $ virtualMachine.network.publicIpAddresses :List of 2
##   ..$ :'data.frame':	1 obs. of  5 variables:
##   .. ..$ id                : chr "/subscriptions/9317e370-3c1f-43a8-9ec0-4f1ad769dd53/resourceGroups/ADMIN/providers/Microsoft.Network/publicIPAd"| __truncated__
##   .. ..$ ipAddress         : chr "104.40.253.75"
##   .. ..$ ipAllocationMethod: chr "Static"
##   .. ..$ name              : chr "adminWorkstation-ip"
##   .. ..$ resourceGroup     : chr "ADMIN"
##   ..$ :'data.frame':	1 obs. of  5 variables:
##   .. ..$ id                : chr "/subscriptions/9317e370-3c1f-43a8-9ec0-4f1ad769dd53/resourceGroups/ml/providers/Microsoft.Network/publicIPAddre"| __truncated__
##   .. ..$ ipAddress         : logi NA
##   .. ..$ ipAllocationMethod: chr "Dynamic"
##   .. ..$ name              : chr "djrtest3685445209ac"
##   .. ..$ resourceGroup     : chr "ml"
```






[^1]: Addopted from https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/vm-do-ten-things
