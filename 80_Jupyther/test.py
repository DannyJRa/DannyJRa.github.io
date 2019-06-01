# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md,Rmd
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
a=5
a

# %%
b=7

# %%
b+a

# %%
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

iplot([{"x": [1, 2, 3, 4, 5, 6, 7, 8], "y": [0, 1, 1, 2, 2, 3, 3, 4]}])


# %%
b+2

# %%
g=8

# %%
