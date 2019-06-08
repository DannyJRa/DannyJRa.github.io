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

# %% [markdown]
#

# %% [markdown]
#

# %%
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

iplot([{"x": [1, 2, 3, 4, 5, 6, 7, 8], "y": [0, 1, 1, 2, 2, 3, 3, 4]}])


# %%
b+2

# %%
g=8

# %%
# enables the %%R magic, not necessary if you've already done this
# %load_ext rpy2.ipython

import pandas as pd
df = pd.DataFrame({
    'cups_of_coffee': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'productivity': [2, 5, 6, 8, 9, 8, 0, 1, 0, -1]
})


# %%
import feather
path = 'my_data.feather'
#feather.write_dataframe(df, path)
df2 = feather.read_dataframe(path)
df2.tail()

# %% {"magic_args": "-i df -w 5 -h 5 --units in -r 200", "language": "R"}
# # import df from global environment
# # make default figure size 5 by 5 inches with 200 dpi resolution
#
# #install.packages("ggplot2", repos='http://cran.us.r-project.org', quiet=TRUE)
# library(ggplot2)
# ggplot(df, aes(x=cups_of_coffee, y=productivity)) + geom_line()
#

# %% {"magic_args": "-i df", "language": "R"}
# # import df from global environment
# # make default figure size 5 by 5 inches with 200 dpi resolution
# rdf=df
# #install.packages("ggplot2", repos='http://cran.us.r-project.org', quiet=TRUE)
# library(ggplot2)
# ggplot(df, aes(x=cups_of_coffee, y=productivity)) + geom_line()

# %%
# #%load_ext rpy2.ipython


# %R -o rdf

pydf2 = pd.DataFrame(rdf)
pydf2

# %%
