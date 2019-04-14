---
title: Blog JSON
author: DannyJRa
date: '2019-01-11'
slug: github_rest_api3
categories:
  - R
tags:
  - GitHub
hidden: false
image: "img/cover.jpg"
share: false
output:
  html_document:
    keep_md: yes
    theme: cerulean
    highlight: tango
    code_folding: show
    toc: yes
    toc_float: yes
  pdf_document:
    number_sections: yes
geometry: margin = 1.2in
fontsize: 10pt
always_allow_html: yes

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
a=1
print(a)
```

```
## 1
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














# Working with JSON


```r
library(tidyverse)
```

```
## ── Attaching packages ─────────────────────────────────────────────────────────────────────── tidyverse 1.2.1 ──
```

```
## ✔ ggplot2 3.1.0       ✔ purrr   0.3.2  
## ✔ tibble  2.1.1       ✔ dplyr   0.8.0.1
## ✔ tidyr   0.8.3       ✔ stringr 1.4.0  
## ✔ readr   1.3.1       ✔ forcats 0.4.0
```

```
## ── Conflicts ────────────────────────────────────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
```



```r
library(jsonlite)
```

```
## 
## Attaching package: 'jsonlite'
```

```
## The following object is masked from 'package:purrr':
## 
##     flatten
```

```
## The following objects are masked from 'package:rjson':
## 
##     fromJSON, toJSON
```

```r
yelp <- fromJSON("data/yelp_academic_dataset_business.json")
```

```
## Error in parse_con(txt, bigint_as_char): parse error: trailing garbage
##            true}, "type": "business"}  {"business_id": "UsFtqoBl7naz8A
##                      (right here) ------^
```

However, when we run the above command we would actully get an error like below.

This is because this JSON file turned out to be something called ‘NDJSON (Newline delimited JSON)’, which means there are multiple JSON values inside this file and each of the JSON values is considered as an independent object. In this particular case, each business information makes up one single JSON value therefore there are many JSON values inside of this JSON file. This could be used often in data streaming situations where each JSON data can be separated from other parts of the file so that each JSON data can be processed without waiting for the whole document to load.


![caption](blog/blog_title.png)


```r
yelp <- stream_in(file("data/yelp_academic_dataset_business.json"))
```

```
##  Found 500 records... Found 1000 records... Found 1500 records... Found 2000 records... Found 2500 records... Found 3000 records... Found 3500 records... Found 4000 records... Found 4500 records... Found 5000 records... Found 5500 records... Found 6000 records... Found 6500 records... Found 7000 records... Found 7500 records... Found 8000 records... Found 8500 records... Found 9000 records... Found 9500 records... Found 10000 records... Found 10500 records... Found 11000 records... Found 11500 records... Found 12000 records... Found 12500 records... Found 13000 records... Found 13500 records... Found 14000 records... Found 14500 records... Found 15000 records... Found 15500 records... Found 16000 records... Found 16500 records... Found 17000 records... Found 17500 records... Found 18000 records... Found 18500 records... Found 19000 records... Found 19500 records... Found 20000 records... Found 20500 records... Found 21000 records... Found 21500 records... Found 22000 records... Found 22500 records... Found 23000 records... Found 23500 records... Found 24000 records... Found 24500 records... Found 25000 records... Found 25500 records... Found 26000 records... Found 26500 records... Found 27000 records... Found 27500 records... Found 28000 records... Found 28500 records... Found 29000 records... Found 29500 records... Found 30000 records... Found 30500 records... Found 31000 records... Found 31500 records... Found 32000 records... Found 32500 records... Found 33000 records... Found 33500 records... Found 34000 records... Found 34500 records... Found 35000 records... Found 35500 records... Found 36000 records... Found 36500 records... Found 37000 records... Found 37500 records... Found 38000 records... Found 38500 records... Found 39000 records... Found 39500 records... Found 40000 records... Found 40500 records... Found 41000 records... Found 41500 records... Found 42000 records... Found 42500 records... Found 43000 records... Found 43500 records... Found 44000 records... Found 44500 records... Found 45000 records... Found 45500 records... Found 46000 records... Found 46500 records... Found 47000 records... Found 47500 records... Found 48000 records... Found 48500 records... Found 49000 records... Found 49500 records... Found 50000 records... Found 50500 records... Found 51000 records... Found 51500 records... Found 52000 records... Found 52500 records... Found 53000 records... Found 53500 records... Found 54000 records... Found 54500 records... Found 55000 records... Found 55500 records... Found 56000 records... Found 56500 records... Found 57000 records... Found 57500 records... Found 58000 records... Found 58500 records... Found 59000 records... Found 59500 records... Found 60000 records... Found 60500 records... Found 61000 records... Found 61184 records... Imported 61184 records. Simplifying...
```

Flatten Yelp data frame
Let’s find out how the data has been imported by quickly running ‘str()’ function.

```r
str(yelp)
```

```
...
## 'data.frame':	61184 obs. of  15 variables:
##  $ business_id  : chr  "vcNAWiLM4dR7D2nwwJ7nCA" "UsFtqoBl7naz8AVUBZMjQQ" "cE27W9VPgO88Qxe4ol6y_g" "HZdLhv6COCleJMo7nPl-RA" ...
##  $ full_address : chr  "4840 E Indian School Rd\nSte 101\nPhoenix, AZ 85018" "202 McClure St\nDravosburg, PA 15034" "1530 Hamilton Rd\nBethel Park, PA 15234" "301 S Hills Vlg\nPittsburgh, PA 15241" ...
##  $ hours        :'data.frame':	61184 obs. of  7 variables:
##   ..$ Tuesday  :'data.frame':	61184 obs. of  2 variables:
##   .. ..$ close: chr  "17:00" NA NA "21:00" ...
##   .. ..$ open : chr  "08:00" NA NA "10:00" ...
##   ..$ Friday   :'data.frame':	61184 obs. of  2 variables:
##   .. ..$ close: chr  "17:00" NA NA "21:00" ...
##   .. ..$ open : chr  "08:00" NA NA "10:00" ...
##   ..$ Monday   :'data.frame':	61184 obs. of  2 variables:
##   .. ..$ close: chr  "17:00" NA NA "21:00" ...
##   .. ..$ open : chr  "08:00" NA NA "10:00" ...
##   ..$ Wednesday:'data.frame':	61184 obs. of  2 variables:
##   .. ..$ close: chr  "17:00" NA NA "21:00" ...
...
```
As you can see ‘hours’ variable is actually a data frame that contains 7 data frames each of which is for a weekday like ‘Tuesday’. And the weekday variables themselves are data frames and each contains two ‘character’ variables of ‘open’ and ‘close’.

This is reflecting the original JSON data structure, but it is a bit confusing for analyzing data in R. We can use ‘flatten()’ function from ‘jsonlite’ package to make the nested hiearchical data structure into a flatten manner by assigning each of the nested variable as its own column as much as possible.



```r
yelp_flat <- jsonlite::flatten(yelp)
str(yelp_flat)
```

```
## 'data.frame':	61184 obs. of  105 variables:
##  $ business_id                                         : chr  "vcNAWiLM4dR7D2nwwJ7nCA" "UsFtqoBl7naz8AVUBZMjQQ" "cE27W9VPgO88Qxe4ol6y_g" "HZdLhv6COCleJMo7nPl-RA" ...
##  $ full_address                                        : chr  "4840 E Indian School Rd\nSte 101\nPhoenix, AZ 85018" "202 McClure St\nDravosburg, PA 15034" "1530 Hamilton Rd\nBethel Park, PA 15234" "301 S Hills Vlg\nPittsburgh, PA 15241" ...
##  $ open                                                : logi  TRUE TRUE FALSE TRUE TRUE TRUE ...
##  $ categories                                          :List of 61184
##   ..$ : chr  "Doctors" "Health & Medical"
##   ..$ : chr "Nightlife"
##   ..$ : chr  "Active Life" "Mini Golf" "Golf"
##   ..$ : chr  "Shopping" "Home Services" "Internet Service Providers" "Mobile Phones" ...
##   ..$ : chr  "Bars" "American (New)" "Nightlife" "Lounges" ...
...
```


Now the data structure looks a lot easier to grasp and even the data looks easier to see.

Before printing out the data I’m going to use ‘as_data_frame()’ function from the new package called ‘tibble’, which was released just last week from Hadley Wickham and the team to make it easier to see the data frame data in R console UI.

We can use ‘as_data_frame()’ function to convert our data frame to be ‘tbl_df’, which is an extended version of the data frame. Once it’s in ‘tbl_df’ type, it automatically shows only the first 10 variables in the console output by simply typing the data frame name so you don’t need to call ‘head()’ function separately. Also, it shows a data type for each variable in the output.


```r
library(tibble)
yelp_tbl <- as_data_frame(yelp_flat)
```

```
## Warning: `as_data_frame()` is deprecated, use `as_tibble()` (but mind the new semantics).
## This warning is displayed once per session.
```

```r
yelp_tbl
```

```
## # A tibble: 61,184 x 105
##    business_id full_address open  categories city  review_count name 
##    <chr>       <chr>        <lgl> <list>     <chr>        <int> <chr>
##  1 vcNAWiLM4d… "4840 E Ind… TRUE  <chr [2]>  Phoe…            9 Eric…
##  2 UsFtqoBl7n… "202 McClur… TRUE  <chr [1]>  Drav…            4 Clan…
##  3 cE27W9VPgO… "1530 Hamil… FALSE <chr [3]>  Beth…            5 Cool…
##  4 HZdLhv6COC… "301 S Hill… TRUE  <chr [6]>  Pitt…            3 Veri…
##  5 mVHrayjG3u… "414 Hawkin… TRUE  <chr [5]>  Brad…           11 Emil…
##  6 KayYbHCt-R… "141 Hawtho… TRUE  <chr [4]>  Carn…           15 Alex…
##  7 b12U9TFESS… "718 Hope H… TRUE  <chr [2]>  Carn…            5 Flyn…
##  8 Sktj1eHQFu… "920 Forsyt… TRUE  <chr [2]>  Carn…            4 Fors…
##  9 3ZVKmuK2l7… "8 Logan St… TRUE  <chr [2]>  Carn…            3 Quak…
## 10 wJr6kSA5dc… "2100 Washi… TRUE  <chr [4]>  Carn…            8 King…
## # … with 61,174 more rows, and 98 more variables: neighborhoods <list>,
## #   longitude <dbl>, state <chr>, stars <dbl>, latitude <dbl>, type <chr>,
## #   hours.Tuesday.close <chr>, hours.Tuesday.open <chr>,
## #   hours.Friday.close <chr>, hours.Friday.open <chr>,
## #   hours.Monday.close <chr>, hours.Monday.open <chr>,
## #   hours.Wednesday.close <chr>, hours.Wednesday.open <chr>,
## #   hours.Thursday.close <chr>, hours.Thursday.open <chr>,
## #   hours.Sunday.close <chr>, hours.Sunday.open <chr>,
## #   hours.Saturday.close <chr>, hours.Saturday.open <chr>, `attributes.By
## #   Appointment Only` <lgl>, `attributes.Happy Hour` <lgl>,
## #   `attributes.Accepts Credit Cards` <list>, `attributes.Good For
## #   Groups` <lgl>, `attributes.Outdoor Seating` <lgl>, `attributes.Price
## #   Range` <int>, `attributes.Good for Kids` <lgl>,
## #   attributes.Alcohol <chr>, `attributes.Noise Level` <chr>,
## #   `attributes.Has TV` <lgl>, attributes.Attire <chr>, `attributes.Good
## #   For Dancing` <lgl>, attributes.Delivery <lgl>, `attributes.Coat
## #   Check` <lgl>, attributes.Smoking <chr>, `attributes.Take-out` <lgl>,
## #   `attributes.Takes Reservations` <lgl>, `attributes.Waiter
## #   Service` <lgl>, `attributes.Wi-Fi` <chr>, attributes.Caters <lgl>,
## #   `attributes.Drive-Thru` <lgl>, `attributes.Wheelchair
## #   Accessible` <lgl>, attributes.BYOB <lgl>, attributes.Corkage <lgl>,
## #   `attributes.BYOB/Corkage` <chr>, `attributes.Order at Counter` <lgl>,
## #   `attributes.Good For Kids` <lgl>, `attributes.Dogs Allowed` <lgl>,
## #   `attributes.Open 24 Hours` <lgl>, `attributes.Accepts
## #   Insurance` <lgl>, `attributes.Ages Allowed` <chr>,
## #   attributes.Ambience.romantic <lgl>,
## #   attributes.Ambience.intimate <lgl>, attributes.Ambience.classy <lgl>,
## #   attributes.Ambience.hipster <lgl>, attributes.Ambience.divey <lgl>,
## #   attributes.Ambience.touristy <lgl>, attributes.Ambience.trendy <lgl>,
## #   attributes.Ambience.upscale <lgl>, attributes.Ambience.casual <lgl>,
## #   `attributes.Good For.dessert` <lgl>, `attributes.Good
## #   For.latenight` <lgl>, `attributes.Good For.lunch` <lgl>,
## #   `attributes.Good For.dinner` <lgl>, `attributes.Good
## #   For.breakfast` <lgl>, `attributes.Good For.brunch` <lgl>,
## #   attributes.Parking.garage <lgl>, attributes.Parking.street <lgl>,
## #   attributes.Parking.validated <lgl>, attributes.Parking.lot <lgl>,
## #   attributes.Parking.valet <lgl>, attributes.Music.dj <lgl>,
## #   attributes.Music.background_music <lgl>,
## #   attributes.Music.karaoke <lgl>, attributes.Music.live <lgl>,
## #   attributes.Music.video <lgl>, attributes.Music.jukebox <lgl>,
## #   attributes.Music.playlist <lgl>, `attributes.Hair Types Specialized
## #   In.coloring` <lgl>, `attributes.Hair Types Specialized
## #   In.africanamerican` <lgl>, `attributes.Hair Types Specialized
## #   In.curly` <lgl>, `attributes.Hair Types Specialized In.perms` <lgl>,
## #   `attributes.Hair Types Specialized In.kids` <lgl>, `attributes.Hair
## #   Types Specialized In.extensions` <lgl>, `attributes.Hair Types
## #   Specialized In.asian` <lgl>, `attributes.Hair Types Specialized
## #   In.straightperms` <lgl>, `attributes.Payment Types.amex` <lgl>,
## #   `attributes.Payment Types.cash_only` <lgl>, `attributes.Payment
## #   Types.mastercard` <lgl>, `attributes.Payment Types.visa` <lgl>,
## #   `attributes.Payment Types.discover` <lgl>, `attributes.Dietary
## #   Restrictions.dairy-free` <lgl>, `attributes.Dietary
## #   Restrictions.gluten-free` <lgl>, `attributes.Dietary
## #   Restrictions.vegan` <lgl>, `attributes.Dietary
## #   Restrictions.kosher` <lgl>, `attributes.Dietary
## #   Restrictions.halal` <lgl>, `attributes.Dietary
## #   Restrictions.soy-free` <lgl>, `attributes.Dietary
## #   Restrictions.vegetarian` <lgl>
```


```r
yelp_tbl2<-yelp_tbl %>% mutate(categories = as.character(categories)) %>% select(categories)
```


Drop now when you look at the data again, looks there are bunch of variables whose name starts with either ‘hours’ or ‘attributes’.


```r
yelp_tbl %>% 
 select(-starts_with("hours"), -starts_with("attribute"))
```

```
## # A tibble: 61,184 x 13
##    business_id full_address open  categories city  review_count name 
##    <chr>       <chr>        <lgl> <list>     <chr>        <int> <chr>
##  1 vcNAWiLM4d… "4840 E Ind… TRUE  <chr [2]>  Phoe…            9 Eric…
##  2 UsFtqoBl7n… "202 McClur… TRUE  <chr [1]>  Drav…            4 Clan…
##  3 cE27W9VPgO… "1530 Hamil… FALSE <chr [3]>  Beth…            5 Cool…
##  4 HZdLhv6COC… "301 S Hill… TRUE  <chr [6]>  Pitt…            3 Veri…
##  5 mVHrayjG3u… "414 Hawkin… TRUE  <chr [5]>  Brad…           11 Emil…
##  6 KayYbHCt-R… "141 Hawtho… TRUE  <chr [4]>  Carn…           15 Alex…
##  7 b12U9TFESS… "718 Hope H… TRUE  <chr [2]>  Carn…            5 Flyn…
##  8 Sktj1eHQFu… "920 Forsyt… TRUE  <chr [2]>  Carn…            4 Fors…
##  9 3ZVKmuK2l7… "8 Logan St… TRUE  <chr [2]>  Carn…            3 Quak…
## 10 wJr6kSA5dc… "2100 Washi… TRUE  <chr [4]>  Carn…            8 King…
## # … with 61,174 more rows, and 6 more variables: neighborhoods <list>,
## #   longitude <dbl>, state <chr>, stars <dbl>, latitude <dbl>, type <chr>
```

# Count how restaurants
Now, let’s find out how many ‘Restaurant’ business in the data. We can use ‘str_detect()’ function from ‘stringr’ package to find the businesses whose ‘categories’ variable values contain ‘Restaurant’ text. If you want to know more detail about this function check out this post.


```r
library(stringr)
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant"))
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 21,892 x 13
##    business_id full_address open  categories city  review_count name 
##    <chr>       <chr>        <lgl> <list>     <chr>        <int> <chr>
##  1 mVHrayjG3u… "414 Hawkin… TRUE  <chr [5]>  Brad…           11 Emil…
##  2 KayYbHCt-R… "141 Hawtho… TRUE  <chr [4]>  Carn…           15 Alex…
##  3 wJr6kSA5dc… "2100 Washi… TRUE  <chr [4]>  Carn…            8 King…
##  4 fNGIbpazjT… "1201 Washi… TRUE  <chr [5]>  Carn…            5 Rock…
##  5 b9WZJp5L1R… "1073 Washi… TRUE  <chr [2]>  Carn…           38 Gab …
##  6 zaXDakTd3R… "202 3rd Av… TRUE  <chr [2]>  Carn…            5 Barb…
##  7 WETE_Lykpc… "215 E Main… FALSE <chr [5]>  Carn…            6 Padd…
##  8 rv7CY8G_Xi… "Raceway Pl… TRUE  <chr [1]>  Carn…            3 Long…
##  9 SQ0j7bgSTa… "214 E Main… TRUE  <chr [2]>  Carn…            8 Don …
## 10 wqu7ILomIO… "2180 Green… TRUE  <chr [3]>  Pitt…            7 Denn…
## # … with 21,882 more rows, and 6 more variables: neighborhoods <list>,
## #   longitude <dbl>, state <chr>, stars <dbl>, latitude <dbl>, type <chr>
```
The cool thing about this function is that even when we have a ‘list’ data type variable it can go inside the list values and do the text matching. Pretty awesome.

Now, number of the rows is 21,892, as opposed to the original of 61,184 rows. That means there are 21,892 ‘Restaurant’ related businesses in this data out of 61,184 businesses. To confirm if this is really the case, let’s look at the categories column with ‘as.character()’ function again.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 mutate(categories = as.character(categories)) %>% select(categories)
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 21,892 x 1
##    categories                                                              
##    <chr>                                                                   
##  1 "c(\"Bars\", \"American (New)\", \"Nightlife\", \"Lounges\", \"Restaura…
##  2 "c(\"Bars\", \"American (Traditional)\", \"Nightlife\", \"Restaurants\"…
##  3 "c(\"Burgers\", \"Breakfast & Brunch\", \"American (Traditional)\", \"R…
##  4 "c(\"Bars\", \"American (Traditional)\", \"Nightlife\", \"Lounges\", \"…
##  5 "c(\"Breakfast & Brunch\", \"Restaurants\")"                            
##  6 "c(\"Cafes\", \"Restaurants\")"                                         
##  7 "c(\"Pubs\", \"Irish\", \"Nightlife\", \"Bars\", \"Restaurants\")"      
##  8 Restaurants                                                             
##  9 "c(\"Chinese\", \"Restaurants\")"                                       
## 10 "c(\"Breakfast & Brunch\", \"American (Traditional)\", \"Restaurants\")"
## # … with 21,882 more rows
```
Looks all the rows (well, all the first 10 rows anyway) look like they have “Restaurants’ as one of the categories.

And this is interesting because people on Yelp are tagging different genres for each “Restaurant” business. For example, some restaurants could be considered as “Bars”, “American (New)”, “Pub”, etc. So one of the interesting question would be, “what type of the restaurants are more common in this data set?”

The easiest way to answer this question is to break out this ‘categories’ list data type variable and assign each value inside the list into each row. So essentially we’ll have a variable called ‘categories’ and this will have just one category value for each row. This means, some businesses might be repeated across rows many times, but that’s ok because our concern for now is to count each restaurant category type.


# Unnest a list variable
To break out ‘categories’ variable and create one row for each value, we can use ‘unnest()’ function from tidyr package, which is another great package from ‘Hadleyverse’ to help making raw data into a ‘tidy’ format.

hadley/tidyr

tidyr - Easily tidy data with spread and gather functions.
github.com	
I will talk about more on ‘tidy’ format with ‘tidyr’ package in a separate post, but for now I am going to simply use ‘unnest()’ function to “unnest” the ‘categories’ variable like below.


```r
library(tidyr)
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 select(name, categories)
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 63,909 x 2
##    name                    categories            
##    <chr>                   <chr>                 
##  1 Emil's Lounge           Bars                  
##  2 Emil's Lounge           American (New)        
##  3 Emil's Lounge           Nightlife             
##  4 Emil's Lounge           Lounges               
##  5 Emil's Lounge           Restaurants           
##  6 Alexion's Bar & Grill   Bars                  
##  7 Alexion's Bar & Grill   American (Traditional)
##  8 Alexion's Bar & Grill   Nightlife             
##  9 Alexion's Bar & Grill   Restaurants           
## 10 Kings Family Restaurant Burgers               
## # … with 63,899 more rows
```



As you can see, ‘Emil’s Lounge’ is now repeated 5 times, for example. This is because it has those 5 different categories assigned to this business. This will allow us to do a quick summarization with ‘count()’ function like below.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 select(name, categories) %>%
 count(categories)
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 284 x 2
##    categories                 n
##    <chr>                  <int>
##  1 Active Life               41
##  2 Adult Entertainment        2
##  3 Afghan                    13
##  4 African                   30
##  5 Airports                   1
##  6 American (New)          1494
##  7 American (Traditional)  2113
##  8 Amusement Parks            2
##  9 Apartments                 1
## 10 Appliances                 1
## # … with 274 more rows
```



And if you want to see the top categories you can simply use ‘arrange()’ function to sort.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 select(name, categories) %>%
 count(categories) %>%
 arrange(desc(n))
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 284 x 2
##    categories                 n
##    <chr>                  <int>
##  1 Restaurants            21892
##  2 Fast Food               2383
##  3 Pizza                   2223
##  4 Mexican                 2208
##  5 American (Traditional)  2113
##  6 Nightlife               2045
##  7 Sandwiches              1981
##  8 Bars                    1934
##  9 Food                    1807
## 10 Italian                 1633
## # … with 274 more rows
```



Let’s get rid of the rows with ‘Restaurants’ category because we know every single rows in this data set has something to do with ‘Restaurant’ now.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 filter(categories != "Restaurants") %>%
 count(categories) %>%
 arrange(desc(n))
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 283 x 2
##    categories                 n
##    <chr>                  <int>
##  1 Fast Food               2383
##  2 Pizza                   2223
##  3 Mexican                 2208
##  4 American (Traditional)  2113
##  5 Nightlife               2045
##  6 Sandwiches              1981
##  7 Bars                    1934
##  8 Food                    1807
##  9 Italian                 1633
## 10 Chinese                 1496
## # … with 273 more rows
```


When you run the above command you will get something like below. You can see ‘Fast Food’ is the number one, and ‘Pizza’ and ‘Mexican’ come after.


What are the most common restaurant types per state / province?
In this data set, there is a variable called ‘state’ that contains state names or province names of US and some European countries. So, what if we want to know what restaurant categories are more frequently showing up for each state ?

We can simply add ‘state’ variable into ‘count()’ function like below.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 filter(categories != "Restaurants") %>%
 count(state, categories) %>%
 arrange(desc(n))
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 1,483 x 3
##    state categories                 n
##    <chr> <chr>                  <int>
##  1 AZ    Mexican                 1197
##  2 AZ    Fast Food               1035
##  3 AZ    Pizza                    944
##  4 AZ    American (Traditional)   924
##  5 AZ    Sandwiches               834
##  6 AZ    Nightlife                725
##  7 NV    Fast Food                695
##  8 AZ    Bars                     686
##  9 AZ    American (New)           668
## 10 AZ    Burgers                  648
## # … with 1,473 more rows
```



Now, let’s take a look at the top restaurant category for each state. We can use ‘group_by()’ function to group the data by state and use ‘top_n()’ function to keep only the top category. Both functions are from ‘dplyr’ package.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 filter(categories != "Restaurants") %>%
 count(state, categories) %>%
 group_by(state) %>%
 top_n(1, n)
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 25 x 3
## # Groups:   state [18]
##    state categories        n
##    <chr> <chr>         <int>
##  1 AZ    Mexican        1197
##  2 BW    Food             82
##  3 EDH   Food            189
##  4 ELN   British           3
##  5 FIF   Bars              1
##  6 FIF   Cocktail Bars     1
##  7 FIF   Delis             1
##  8 FIF   Fast Food         1
##  9 FIF   Nightlife         1
## 10 IL    Pizza            31
## # … with 15 more rows
```



As you can see there are 5 entries for “FIF” province, this is because they are all tie. But the values are just ‘1’ and that’s a really small number compared to the others. So let’s filter out those small numbers from the data before the group_by and top_n steps.


```r
yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute")) %>%
 filter(str_detect(categories, "Restaurant")) %>%
 unnest(categories) %>%
 filter(categories != "Restaurants") %>%
 count(state, categories) %>%
 filter(n > 10) %>%
 group_by(state) %>%
 top_n(1, n)
```

```
## Warning in stri_detect_regex(string, pattern, negate = negate, opts_regex =
## opts(pattern)): argument is not an atomic vector; coercing
```

```
## # A tibble: 12 x 3
## # Groups:   state [12]
##    state categories                 n
##    <chr> <chr>                  <int>
##  1 AZ    Mexican                 1197
##  2 BW    Food                      82
##  3 EDH   Food                     189
##  4 IL    Pizza                     31
##  5 MLN   Cafes                     11
##  6 NC    American (Traditional)   257
##  7 NV    Fast Food                695
##  8 ON    Chinese                   29
##  9 PA    Pizza                    196
## 10 QC    French                   272
## 11 SC    American (Traditional)    13
## 12 WI    Nightlife                130
```



The result is a list of the top restaurant category for each of the 12 state or province.

This is a very simple analysis on Yelp business data. But given where we started with Yelp business data in the raw JSON format, hope this has demonstrated how quickly, incrementally, and iteratively we can get some interesting information out of such un-traditional (not tabular) data format relatively easily and quickly.

Notes: Adopted from https://blog.exploratory.io/working-with-json-data-in-very-simple-way-ad7ebcc0bb89
