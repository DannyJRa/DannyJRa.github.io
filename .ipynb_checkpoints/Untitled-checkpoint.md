---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
  kernelspec:
    display_name: R
    language: R
    name: ir
---

```R slideshow={"slide_type": "slide"}
a=1
```

```R

```

```R

```

```R
library(tidyverse)
library(plotly)

mpg_plotly <- mpg %>%
  plot_ly()
```

```R
mpg_plotly %>%
  add_markers(x = ~cty, y = ~hwy)
```

```R

```
