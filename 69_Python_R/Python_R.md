---
title: R-Python Bridge
author: DannyJRa
date: '2018-04-14'
slug: r-python-bridge
categories:
  - R
tags:
  - Docker
hidden: false
image: "img/cover.jpg"
share: false
output:
  blogdown::html_page:
   # number_sections: true
    toc: TRUE

---

Linear models
The R code is:
<!--more-->

```r
ctl <- c(4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14)
trt <- c(4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69)
group <- gl(2, 10, 20, labels = c("Ctl","Trt"))
weight <- c(ctl, trt)

anova(lm.D9 <- lm(weight ~ group))
```

```
## Analysis of Variance Table
## 
## Response: weight
##           Df Sum Sq Mean Sq F value Pr(>F)
## group      1 0.6882 0.68820  1.4191  0.249
## Residuals 18 8.7292 0.48496
```

```r
summary(lm.D90 <- lm(weight ~ group - 1))# omitting intercept
```

```
## 
## Call:
## lm(formula = weight ~ group - 1)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -1.0710 -0.4938  0.0685  0.2462  1.3690 
## 
## Coefficients:
##          Estimate Std. Error t value Pr(>|t|)    
## groupCtl   5.0320     0.2202   22.85 9.55e-15 ***
## groupTrt   4.6610     0.2202   21.16 3.62e-14 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.6964 on 18 degrees of freedom
## Multiple R-squared:  0.9818,	Adjusted R-squared:  0.9798 
## F-statistic: 485.1 on 2 and 18 DF,  p-value: < 2.2e-16
```


One way to achieve the same with rpy2.robjects is


```r
#library(reticulate)
#use_python("/home/danny/anaconda3/bin/python",required=T)
#use_condaenv(condaenv = "r-nlp", conda = "/opt/anaconda3/bin/conda")
#use_condaenv(condaenv = "r-nlp", conda = "/home/danny/anaconda3")
library(reticulate)
use_python(python = "/home/danny/anaconda3/bin/python", required = TRUE)
py_config()
```

```
## python:         /home/danny/anaconda3/bin/python
## libpython:      /home/danny/anaconda3/lib/libpython3.7m.so
## pythonhome:     /home/danny/anaconda3:/home/danny/anaconda3
## version:        3.7.1 (default, Dec 14 2018, 19:28:38)  [GCC 7.3.0]
## numpy:          /home/danny/anaconda3/lib/python3.7/site-packages/numpy
## numpy_version:  1.15.4
## 
## NOTE: Python version was forced by use_python function
```


```r
py_discover_config()
```

```
## python:         /home/danny/anaconda3/bin/python
## libpython:      /home/danny/anaconda3/lib/libpython3.7m.so
## pythonhome:     /home/danny/anaconda3:/home/danny/anaconda3
## version:        3.7.1 (default, Dec 14 2018, 19:28:38)  [GCC 7.3.0]
## numpy:          /home/danny/anaconda3/lib/python3.7/site-packages/numpy
## numpy_version:  1.15.4
## 
## NOTE: Python version was forced by use_python function
```


```r
py_config()
```

```
## python:         /home/danny/anaconda3/bin/python
## libpython:      /home/danny/anaconda3/lib/libpython3.7m.so
## pythonhome:     /home/danny/anaconda3:/home/danny/anaconda3
## version:        3.7.1 (default, Dec 14 2018, 19:28:38)  [GCC 7.3.0]
## numpy:          /home/danny/anaconda3/lib/python3.7/site-packages/numpy
## numpy_version:  1.15.4
## 
## NOTE: Python version was forced by use_python function
```



```python
import platform
print(platform.python_version())
```

```
## 3.7.1
```

```python
import rpy2
```


```python
from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
stats = importr('stats')
base = importr('base')

ctl = FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
trt = FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])
group = base.gl(2, 10, 20, labels = ["Ctl","Trt"])
weight = ctl + trt

robjects.globalenv["weight"] = weight
robjects.globalenv["group"] = group
lm_D9 = stats.lm("weight ~ group")
print(stats.anova(lm_D9))

# omitting the intercept
lm_D90 = stats.lm("weight ~ group - 1")
print(base.summary(lm_D90))
```



```r
dat <- read.table(text='    V1         V2
  google 0.99702575
   gmail 0.02492131
    maps 0.02040844
motorola 0.02006636
    view 0.01679274',header=TRUE)
ll <- as.list(setNames(dat$V2,dat$V1))
library(rjson)
exportJSON=toJSON(ll)

write(exportJSON, "test.json")
```

