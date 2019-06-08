# ---
# jupyter:
#   jupytext:
#     formats: ipynb,R//R
#     text_representation:
#       extension: .R
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: R
#     language: R
#     name: ir
# ---

# +
library(plotly)

p <- plot_ly(
  x = c("giraffes", "orangutans", "monkeys"),
  y = c(20, 14, 23),
  name = "SF Zoo",
  type = "bar"
)

# Create a shareable link to your chart
# Set up API credentials: https://plot.ly/r/getting-started
p
# -

plot(1,1)





# +
library(feather)

df=cars
path <- "my_data.feather"
write_feather(df, path)
df <- read_feather(path)
# -

df


