# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: jupyterlab-environment_new
#     language: python
#     name: jupyterlab-environment_new
# ---

# %%
a=2

# %%

executed in 8ms, finished 11:41:42 2019-10-26
b=3
b=3
executed in 7ms, finished 11:48:18 2019-10-26
b=3

# %%
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length")
fig.show()

# %%


# %%
