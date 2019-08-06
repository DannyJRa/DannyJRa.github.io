---
title: GCP - Cloud Scheduler
author: DannyJRa
date: '2019-04-14'
slug: gcp_cloudscheduler
categories:
  - Cloud
tags:
  - GCP
hidden: false
image: "img/63_GoogleCloudFunctions_Title.png"
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




Add summary desdcription here
 
<!--more-->








# Schedule Google Compute Engine via Cloud Scheduler

Google released Cloud Scheduler, which is a managed cron service that can perform tasks for other Google services. With that launch, Google also released a tutorial titled [Scheduling Instances with Cloud Scheduler](https://cloud.google.com/scheduler/docs/start-and-stop-compute-engine-instances-on-a-schedule), demonstrating how you can programmatically start and stop instances using Cloud Scheduler in conjunction with Cloud Functions. 

## Create PubSub Trigger


```bash
gcloud pubsub topics create start-instance-event
gcloud pubsub topics create stop-instance-event
```



```bash
git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

cd nodejs-docs-samples/functions/scheduleinstance/
```

## Create the start and stop functions



```bash
cd nodejs-docs-samples/functions/scheduleinstance/
gcloud functions deploy startInstancePubSub \
    --trigger-topic start-instance-event \
    --runtime nodejs6
```


```bash
cd nodejs-docs-samples/functions/scheduleinstance/
gcloud functions deploy stopInstancePubSub \
    --trigger-topic stop-instance-event \
    --runtime nodejs6
```
Testing the function with the helper of encoded zone and instance name:


```bash
echo '{"zone":"europe-west3-c", "instance":"cloudbreak"}' | base64
```


```bash
gcloud functions call stopInstancePubSub \
    --data '{"data":"eyJ6b25lIjoiZXVyb3BlLXdlc3QzLWMiLCAiaW5zdGFuY2UiOiJjbG91ZGJyZWFrIn0K"}'
```

Check that the instance has a status of TERMINATED. It may take up to 30 seconds to finish shutting down.



```bash
gcloud compute instances describe cloudbreak \
    --zone europe-west3-c \
    | grep status
```

## Set up the Cloud Scheduler jobs to call Cloud Pub/Sub


Create the start job.


```bash
gcloud beta scheduler jobs create pubsub startup-workday-instance \
    --schedule '35 9 * * 1-7' \
    --topic start-instance-event \
    --message-body '{"zone":"europe-west3-c", "instance":"cloudbreak"}' \
    --time-zone 'Europe/Zurich'
```


Create the stop job.



```bash
gcloud beta scheduler jobs create pubsub shutdown-workday-instance \
    --schedule '45 09 * * 1-7' \
    --topic stop-instance-event \
    --message-body '{"zone":"europe-west3-c", "instance":"cloudbreak"}' \
    --time-zone 'Europe/Zurich'
```

Verify the job works


```bash
gcloud beta scheduler jobs run shutdown-workday-instance
```


