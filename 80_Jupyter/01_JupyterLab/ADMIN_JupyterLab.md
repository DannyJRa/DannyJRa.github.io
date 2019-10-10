#WORKS on this port: Start JupyterLab without password/token request

jupyter lab --port=8891 --NotebookApp.token='' --NotebookApp.password=''







Setting up python, pipenv and jupyter notebook on Ubuntu 18.04
05 May 2018
Ubuntu 18.04 Bionic Beaver (the latest LTS version) was released last week. The little script below will get pip3 and pipenv up and running.

# Install pip and pipenv
sudo apt install python3-pip python3-dev
pip3 install --user pipenv

# Add pipenv (and other python scripts) to PATH
echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
Create a new project and install some dependencies (include jupyter)

mkdir project-name && cd project-name
pipenv install numpy matplotlib jupyter
Start a jupyter notebook

pipenv run jupyter notebook




#%%
pattern = [('.|.'*(2*i + 1)).center(30, '-') for i in range(10//2)]
print('\n'.join(pattern + ['I LOVE DATA'.center(30, '-')] + pattern[::-1]))


pandoc --version



# Add Virtual Environment to Jupyter Notebook
Jupyter Notebook makes sure that the IPython kernel is available, but you have to manually add a kernel with a different version of Python or a virtual environment. First, you need to activate your virtual environment. Next, install ipykernel which provides the IPython kernel for Jupyter:

pipenv install ipykernel
Next you can add your virtual environment to Jupyter by typing:

python -m ipykernel install --name=Test
This should print the following:

Installed kernelspec myenv in /home/user/.loca

82_ML with Python) (base) danny@workstation:~/OneDrive/DataScience/02_CloudComputing/82_ML with Python$ sudo chown danny /usr/local/share/jupyter/
(82_ML with Python) (base) danny@workstation:~/OneDrive/DataScience/02_CloudComputing/82_ML with Python$ python -m ipykernel install --name=Test
# CHart editor
    https://www.youtube.com/watch?v=zR7G2tNVo1Q





BLOG:
Jupyter Lab extensions for Data Scientist
https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1
# Plotly extensions
https://github.com/jupyterlab/jupyter-renderers/tree/master/packages/plotly-extension

jupyter lab --port=8891

#
Useful Tools and Extensions for JupyterLab
MAY 09, 2019
Things on this page are fragmentary and immature notes/thoughts of the author. It is not meant to readers but rather for convenient reference of the author and future improvement.


# Using plotly
Source: https://github.com/jupyterlab/jupyter-renderers/tree/master/packages/plotly-extension

jupyter labextension install @jupyterlab/plotly-extension
## Plotly Express
pip install plotly_express
Blog
    https://towardsdatascience.com/its-2019-make-your-data-visualizations-interactive-with-plotly-b361e7d45dc6


Current talk
https://www.youtube.com/watch?v=cuTMbGjN2GQ

I’m a big fan of the Zen of Python’s one clear way: “There should be one — and preferably only one — obvious way to do it.” Two ways leads to research time, choice fatigue, and errors.

# Using Bokeh
https://github.com/bokeh/jupyterlab_bokeh

Tut
https://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/index.ipynb

# Shortcut UI
https://github.com/jupyterlab/jupyterlab-shortcutui
https://github.com/bokeh/jupyterlab_bokeh


ValueError: This extension does not yet support the current version of JupyterLab.
jupyter labextension install @jupyterlab/shortcutui

#Celltags
https://github.com/jupyterlab/jupyterlab-celltags

jupyter labextension install @jupyterlab/celltags

#TOC
https://github.com/jupyterlab/jupyterlab-toc
jupyter labextension install @jupyterlab/toc

# DrawIO
https://github.com/QuantStack/jupyterlab-drawio
jupyter labextension install jupyterlab-drawio


#Export
https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/exporting.html
https://github.com/ipython-contrib/jupyter_contrib_nbextensions
pip install jupyter_contrib_nbextensions

## Server
https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator

pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable

Metedata


https://github.com/yuvipanda/jupyterlab-nbmetadata

jupyter labextension install jupyterlab_nbmetadata
#Jupytext
https://github.com/mwouts/jupyterlab-jupytext
jupyter labextension install jupyterlab-jupytext

jupytext --set-formats ipynb,python//py:percent --sync *.ipynb

jupytext --set-formats ipynb,R//Rmd --sync R_test.ipynb
jupytext --set-formats ipynb,R//md --sync R_test.ipynb
jupytext --set-formats ipynb,R//R --sync R_test.ipynb


# EXPORT

jupyter nbconvert --to html R_test.ipynb

jupyter nbconvert --to html R_test.ipynb

#Execute/paramter

pip install papermill


papermill R_test.ipynb R_test_run.ipynb
jupyter nbconvert --to markdown R_test_run.ipynb
jupyter nbconvert --to Rmd R_test_run.ipynb

# Jupyter Noteboos Developement Manifesto

## NOVA extension: Execute notebook on GCP AI Platform

# Github extions (bowse only)

jupyter labextension install @jupyterlab/github

# Tensorboard
https://github.com/chaoleili/jupyterlab_tensorboard

jupyter labextension install jupyterlab_tensorboard

# Overview

Community-developed extensions on GitHub are tagged with the jupyterlab-extension topic, and currently include file viewers (GeoJSON, FASTA, etc.), Google Drive integration, GitHub browsing, and ipywidgets support.

https://github.com/topics/jupyterlab-extension