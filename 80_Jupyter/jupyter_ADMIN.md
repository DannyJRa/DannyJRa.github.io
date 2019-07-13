# Add Virtual Environment to Jupyter Notebook

Source: https://janakiev.com/til/jupyter-virtual-envs/
Jupyter Notebook makes sure that the IPython kernel is available, but you have to manually add a kernel with a different version of Python or a virtual environment. First, you need to activate your virtual environment. Next, install ipykernel which provides the IPython kernel for Jupyter:

pip install --user ipykernel
Next you can add your virtual environment to Jupyter by typing:

python -m ipykernel install --user --name=myenv
This should print the following:

Installed kernelspec myenv in /home/user/.local/share/jupyter/kernels/myenv