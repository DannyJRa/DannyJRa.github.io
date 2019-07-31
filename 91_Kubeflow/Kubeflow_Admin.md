



# Install local Kubernetes
Source: https://www.kubeflow.org/docs/started/getting-started-multipass/

git clone https://github.com/canonical-labs/kubernetes-tools
sudo kubernetes-tools/setup-microk8s.sh

If you would like access to the Kubernetes dashboard, please run this command:

kubernetes-tools/expose-dashboard.sh

# Install Kubeflow
git clone https://github.com/canonical-labs/kubeflow-tools
kubeflow-tools/install-kubeflow.sh

#Access Jupyter
multipass list 
multipass info kubeflow





# Install on GCP KPE
Source: https://www.kubeflow.org/docs/gke/deploy/deploy-cli/
kubectl

gcloud auth application-default login

# If using basic authentication, create environment variables for
# username and password:


## Download kfctl

Choose latest release on 
https://github.com/kubeflow/kubeflow/releases/

wget https://github.com/kubeflow/kubeflow/releases/download/v0.6.1/kfctl_v0.6.1_linux.tar.gz

tar -xvf kfctl_v0.6.1_linux.tar.gz


#Try local remote 

git clone https://github.com/kubeflow/fairing 


#Microk8s manage local kubernetes cluster
#Source: https://microk8s.io/
kubectl config view
kubectl stop

microk8s.enable dns dashboard
sudo microk8s.stop
sudo microk8s.start