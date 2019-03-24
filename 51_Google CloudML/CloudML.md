---
title: "Untitled"
output: html_document
---



```R
library(reticulate)
```


Source: https://cloud.google.com/ml-engine/docs/scikit/getting-started-training


```python
# This file is for training on Cloud ML Engine with scikit-learn.

#%%
# [START setup]
import datetime
import os
import subprocess
import sys
import pandas as pd
#%%
from sklearn import svm
from sklearn.externals import joblib

# Fill in your Cloud Storage bucket name
#BUCKET_NAME = 'cloud_ml'
BUCKET_NAME = 'cloudml_test_djr'
# [END setup]

#%%
# [START download-data]
iris_data_filename = 'iris_data.csv'
iris_target_filename = 'iris_target.csv'
data_dir = 'gs://cloud-samples-data/ml-engine/iris'


subprocess.check_call(['gsutil', 'cp', os.path.join(data_dir,
                                                    iris_data_filename),
                       iris_data_filename])


```
```python



subprocess.check_call(['gsutil', 'cp', os.path.join(data_dir,
                                                    iris_target_filename),
                       iris_target_filename])
# [END download-data]
#%%

# [START load-into-pandas]
# Load data into pandas, then use `.values` to get NumPy arrays

test= pd.__version__
iris_data = pd.read_csv(iris_data_filename).values



iris_target = pd.read_csv(iris_target_filename).values

# Convert one-column 2D array into 1D array for use with scikit-learn
iris_target = iris_target.reshape((iris_target.size,))
# [END load-into-pandas]


# [START train-and-save-model]
# Train the model
classifier = svm.SVC(gamma='auto', verbose=True)
classifier.fit(iris_data, iris_target)

# Export the classifier to a file
model_filename = 'model.joblib'
joblib.dump(classifier, model_filename)
# [END train-and-save-model]


# [START upload-model]
# Upload the saved model file to Cloud Storage
gcs_model_path = os.path.join('gs://', BUCKET_NAME,
    datetime.datetime.now().strftime('iris_%Y%m%d_%H%M%S'), model_filename)
subprocess.check_call(['gsutil', 'cp', model_filename, gcs_model_path])
# [END upload-model]


```


```r
py$test
```

### Run trainer locally

n the command line, set the following environment variables, replacing [VALUES-IN-BRACKETS] with the appropriate values:

TRAINING_PACKAGE_PATH="./iris_sklearn_trainer/"
MAIN_TRAINER_MODULE="iris_sklearn_trainer.iris_training"
Test your training job locally:

```Bash
gcloud ml-engine local train \
  --package-path $TRAINING_PACKAGE_PATH \
  --module-name $MAIN_TRAINER_MODULE
```



### Run in the cloud


```
    BUCKET_NAME='cloudml_test_djr'
    JOB_NAME="iris_scikit_learn_$(date +"%Y%m%d_%H%M%S")"
    JOB_DIR=gs://$BUCKET_NAME/scikit_learn_job_dir
    TRAINING_PACKAGE_PATH="./iris_sklearn_trainer/"
    MAIN_TRAINER_MODULE="iris_sklearn_trainer.iris_training"
    REGION=us-central1
    RUNTIME_VERSION=1.13
    PYTHON_VERSION=2.7
    SCALE_TIER=BASIC
```

Submitting the job

gcloud ml-engine jobs submit training $JOB_NAME \
  --job-dir $JOB_DIR \
  --package-path $TRAINING_PACKAGE_PATH \
  --module-name $MAIN_TRAINER_MODULE \
  --region $REGION \
  --runtime-version=$RUNTIME_VERSION \
  --python-version=$PYTHON_VERSION \
  --scale-tier $SCALE_TIER


### Deploy your model to Cloud ML Engine for online predictions (optional)