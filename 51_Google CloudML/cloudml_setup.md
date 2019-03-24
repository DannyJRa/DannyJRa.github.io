


Install  google cloud_sdk

sudo apt-get update && sudo apt-get install google-cloud-sdk

Install additional components
sudo pip install google-compute-engine
sudo apt-get install google-cloud-sdk-app-engine-java

## List 

gcloud ml-engine models list


### Install frameworks

pip install scikit-learn

### Set up your Cloud Storage bucket

BUCKET_NAME="cloudml_bucket"

REGION=us-central1

gsutil mb -l $REGION gs://$BUCKET_NAME