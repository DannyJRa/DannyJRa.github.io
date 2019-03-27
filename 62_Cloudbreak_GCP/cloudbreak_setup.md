## Create creditals

IAM 

## Launch from the quickstart template

git clone https://github.com/hortonworks/cbd-quickstart
cd cbd-quickstart
git checkout 2.7.1



gcloud deployment-manager deployments create cloudbreak-deployment --config=$HOME/Cloudbreak/cbd-quickstart/gcp/vm_template_config.yaml



gcloud deployment-manager deployments create cloudbreak --config=$HOME/Cloudbreak/cbd-quickstart/gcp/vm_template_config.yaml

gcloud deployment-manager deployments create cloudbreak-dev --config=$HOME/Cloudbreak/cbd-quickstart/gcp/vm_template_config.yaml




### Install CLI

