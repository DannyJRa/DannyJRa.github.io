---
title: "<center><div class='mytitle'>R Markdown output with parallax</div></center>"
author: "<center><div class='mysubtitle'>See the original code on [github](https://github.com/holtzy/R-Markdown-Parallax).[^1] This tip is part of my [RMarkdown collection](https://github.com/DannyJRa/DannyJRa.github.io/tree/master/11_R_RMarkdown).</div></center>"
output:
  html_document:
      keep_md: yes
      css: www/style.css
      toc: FALSE
      includes: 
        before_body: www/header.html
---

<br><br>

<div class="mycontent">


# How it works
***

- The `footer.html` file calls both the background image and the logo. 
- The `style.css` file makes the header full width, but keep a restricted area for your document content.


A little plot from the [R graph gallery](https:www.r-graph-gallery.com)? (We need content in this page to be able to scroll..)

```r
# Library
library(tidyverse)
 
# Create data
value1=abs(rnorm(26))*2
data=data.frame(x=LETTERS[1:26], value1=value1, value2=value1+1+rnorm(26, sd=1) )
 
# Reorder data using average?
data = data %>% rowwise() %>% mutate( mymean = mean(c(value1,value2) )) %>% arrange(mymean) %>% mutate(x=factor(x, x))
 
# With a bit more style
ggplot(data) +
  geom_segment( aes(x=x, xend=x, y=value1, yend=value2), color="grey") +
  geom_point( aes(x=x, y=value1), color=rgb(0.2,0.7,0.1,0.5), size=3 ) +
  geom_point( aes(x=x, y=value2), color=rgb(0.7,0.2,0.1,0.5), size=3 ) +
  coord_flip()+
  theme_light() +
  theme(
    legend.position = "none",
    panel.border = element_blank(),
  ) +
  xlab("") +
  ylab("Value of Y") +
  ggtitle("A random plot showing random data")
```

<img src="index_files/figure-html/unnamed-chunk-1-1.png" style="display: block; margin: auto;" />





[^1]: Addopted from https://github.com/holtzy/R-Markdown-Parallax
