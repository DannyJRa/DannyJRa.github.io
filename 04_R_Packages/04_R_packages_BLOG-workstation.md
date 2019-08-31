---
title: R packages
author: DannyJRa
date: '2018-06-15'
slug: github_rest_api3
categories:
  - R
tags:
  - Set-up
hidden: false
image: "img/04_R_packages_BLOG.jpg"
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





Original post here: /home/danny/OneDrive/DataScience/41_DannyJRa.github.io/04_R_Packages/01_blog_caret_Tut.html

Add summary desdcription of blog
 
<!--more-->




# Favorite packages

Here are my go-to R packages -- in a handy searchable table.
One of the great things about R is the thousands of packages users have written to solve specific problems in various disciplines -- analyzing everything from weather or financial data to the human genome -- not to mention analyzing computer security-breach data.


Some tasks are common to almost all users, though, regardless of subject area: data import, data wrangling and data visualization. The table below show my favorite go-to packages for one of these three tasks (plus a few miscellaneous ones tossed in). The package names in the table are clickable if you want more information. 




```r
library(openxlsx)
favorites <- read.xlsx(xlsxFile = "Packages_favorite.xlsx", sheet = 1, skipEmptyRows = FALSE)
```



```r
library(DT)
datatable(favorites)
```

<!--html_preserve--><div id="htmlwidget-e39f4f6d901093a460a9" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-e39f4f6d901093a460a9">{"x":{"filter":"none","data":[["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78"],["dplyr","purrr","readxl","googlesheets","readr","rio","Hmisc","datapasta","sqldf","jsonlite","XML","httr","quantmod","tidyquant","rvest","reshape2","tidyr","splitstackshape","magrittr","validate","testthat","data.table","stringr","lubridate","zoo","editR","knitr","officeR","listviewer","DT","ggplot2","patchwork","ggiraph","dygraphs","googleVis","metricsgraphics","taucharts","RColorBrewer","sf","leaflet","ggmap","tmap &amp; tmaptools","mapsapi","tidycensus","glue","rga","RSiteCatalyst","roxygen2","shiny","flexdashboard","openxlsx","gmodels","janitor","car","rcdimple","foreach","scales","plotly","highcharter","profvis","tidytext","diffobj","Prophet","feather","fst","googleAuthR","devtools","remotes","installr","reinstallr","usethis","here","pacman","plumber","echarts4r","cloudyR project","geofacet","beepr"],["data wrangling, data analysis","data wrangling","data import","data import, data export","data import","data import, data export","data analysis","data import","data wrangling, data analysis","data import, data wrangling","data import, data wrangling","data import, data wrangling","data import, data visualization, data analysis","data import, data visualization, data analysis","data import, web scraping","data wrangling","data wrangling","data wrangling","data wrangling","data wrangling","programming","data wrangling, data analysis","data wrangling","data wrangling","data wrangling, data analysis","data display","data display","data display","data display, data wrangling","data display","data visualization","data visualization","data visualization","data visualization","data visualization","data visualization","data visualization","data visualization","mapping, data wrangling","mapping","mapping","mapping","mapping, data wrangling","mapping, data wrangling","data wrangling","Web analytics","Web analytics","package development","data visualization","data visualization","misc","data wrangling, data analysis","data wrangling, data analysis","data wrangling","data visualization","data wrangling","data wrangling","data visualization","data visualization","programming","text mining","data analysis","forecasting","data import, data export","data import, data export","data import","package development, package installation","package installation","misc","misc","package development, programming","misc","misc","data export, programming","data visualization","data import, data export","data visualization, mapping","misc"],["The essential data-munging R package when working with data frames. Especially useful for operating on data by categories. CRAN.","purrr makes it easy to apply a function to each item in a list and return results in the format of your choice. It's more complex to learn than the older plyr package, but also more robust. And, its functions are more standardized than base R's apply family -- plus it's got functions for tasks like error-checking. CRAN.","Fast way to read Excel files in R, without dependencies such as Java. CRAN.","Easily read data into R from Google Sheets. CRAN.","Base R handles most of these functions; but if you have huge files, this is a speedy and standardized way to read tabular files such as CSVs into R data frames, as well as plain text files into character strings with read_file. CRAN.","rio has a good idea: Pull a lot of separate data-reading packages into one, so you just need to remember 2 functions: import and export. CRAN.","There are a number of useful functions in here. Two of my favorites: describe, a more robust summary function, and Cs, which creates a vector of quoted character strings from unquoted comma-separated text. Cs(so, it, goes) creates c(\"so\", \"it\", \"goes\"). CRAN.","Data copy and paste: Meet reproducible research. If you've copied data from the Web, a spreadsheet, or other source into your clipboard, datapasta lets you paste it into R as an R object, with the code to reproduce it. It includes RStudio add-ins as well as command-line functions for transposing data, turning it into markdown format, and more. CRAN.","Do you know a great SQL query you'd use if your R data frame were in a SQL database? Run SQL queries on your data frame with sqldf. CRAN.","Parse json within R or turn R data frames into json. CRAN.","Many functions for elegantly dealing with XML and HTML, such as readHTMLTable. CRAN.","An R interface to http protocols; useful for pulling data from APIs. See the httr quickstart guide. CRAN.","Even if you're not interested in analyzing and graphing financial investment data, quantmod has easy-to-use functions for importing economic as well as financial data from sources like the Federal Reserve. CRAN.","Another financial package that's useful for importing, analyzing and visualizing data, integrating aspects of other popular finance packages as well as tidyverse tools. With thorough documentation. CRAN.","Web scraping: Extract data from HTML pages. Inspired by Python's Beautiful Soup. Works well with Selectorgadget. CRAN.","Change data row and column formats from \"wide\" to \"long\"; turn variables into column names or column names into variables and more. The tidyr package is a newer, more focused option, but I still use reshape2. CRAN.","While I still prefer reshape2 for general re-arranging, tidy won me over with specialized functions like fill (fill in missing columns from data above) and replace_na. CRAN.","It's rare that I'd recommend a package that hasn't been updated in years, but the cSplit() function solves a rather complex shaping problem in an astonishingly easy way. If you have a data frame column with one or more comma-separated values (think a survey question with \"select all that apply\"), this is worth an install if you want to separate each item into its own new data frame row.. CRAN.","This package gave us the %&gt;% symbol for chaining R operations, but it's got other useful operators such as %&lt;&gt;% for mutating a data frame in place and and . as a placeholder for the original object being operated upon. CRAN.","Intuitive data validation based on rules you can define, save and re-use. CRAN.","Package that makes it easy to write unit tests for your R code. CRAN.","Popular package for heavy-duty data wrangling. While I typically prefer dplyr, data.table has many fans for its speed with large data sets. CRAN.","Numerous functions for text manipulation. Some are similar to existing base R functions but in a more standard format, including working with regular expressions. Some of my favorites: str_pad and str_trim. CRAN.","Everything you ever wanted to do with date arithmetic, although understanding &amp; using available functionality can be somewhat complex. CRAN.","Robust package with a slew of functions for dealing with time series data; I like the handy rollmean function with its align=right and fill=NA options for calculating moving averages. CRAN.","Interactive editor for R Markdowndocuments. Note that R Markdown Notebooks are another useful way to generate Markdown interactively. editR is on GitHub.","Add R to a markdown document and easily generate reports in HTML, Word and other formats. A must-have if you're interested in reproducible research and automating the journey from data analysis to report creation. CRAN.","Import and edit Microsoft Word and PowerPoint documents, making it easy to add R-generated analysis and visualizations to existing as well as new reports and presentations. CRAN.","While RStudio has since added a list-viewing option, this HTML widget still offers an elegant way to view complex nested lists within R. GitHub timelyportfolio/listviewer.","Create a sortable, searchable table in one line of code with this R interface to the jQuery DataTables plug-in. GitHub rstudio/DT.","Powerful, flexible and well-thought-out dataviz package following 'grammar of graphics' syntax to create static graphics, but be prepared for a steep learning curve. CRAN.","Easily combine ggplot2 plots and keep the new, merged plot a ggplot2 object. plot_layout() adds ability to set columns, rows, and relative sizes of each component graphic. GitHub.","Make ggplot2 plots interactive with this extension's new geom functions such geom_bar_interactive and arguments for tooltips and JavaScript onclicks. CRAN.","Create HTML/JavaScript graphs of time series - one-line command if your data is an xts object. CRAN.","Tap into the Google Charts API using R. CRAN.","R interface to the metricsgraphics JavaScript library for bare-bones line, scatterplot and bar charts. GitHub hrbrmstr/metricsgraphics.","This html widget library is especially useful for scatterplots where you want to view multiple regression options. However, it does much more than that, including line and bar charts with legends and tooltips. GitHub hrbrmstr/taucharts.","Not a designer? RColorBrewer helps you select color palettes for your visualizations. CRAN. ","This package makes it much easier to do GIS work in R. Simple features protocols make geospatial data look a lot like regular data frames, while various functions allow for analysis such as determining whether points are in a polygons. A GIS game-changer for R. CRAN.","Map data using the Leaflet JavaScript library within R. GitHub rstudio/leaflet.","Although I don't use this package often for its main purpose of pulling down background map tiles, it's my go-to for geocoding up to 2,500 addresses with the Google Maps API with its geocode and mutate_geocode functions. CRAN.","These package offer an easy way to read in shape files and join data files with geographic info, as well as do some exploratory mapping. Recent functionality adds support for simple features, interactive maps and creating leaflet objects. Plus, tmaptools::palette_explorer() is a great tool for picking ColorBrewer palettes. CRAN.","This interface to the Google Maps Direction and Distance Matrix APIs let you analyze and map distances and driving routes. CRAN.","Want to analyze and map U.S. Census Bureau data from 5-year American Community Surveys or 10-year censuses? This makes it easy to download numerical and geospatial info in R-ready format. CRAN.","Main function, also glue, evaluates variables and R expressions within a quoted string, as long as they're enclosed by {} braces. This makes for an elegant paste() replacement. CRAN.","Use Google Analytics with R. GitHub skardhamar/rga.","Use Adobe Analytics with R. GitHub randyzwitch/RSiteCatalyst.","Useful tools for documenting functions within R packages. CRAN.","Turn R data into interactive Web applications. I've seen some nice (if sometimes sluggish) apps and it's got many enthusiasts. CRAN.","If Shiny is too complex and involved for your needs, this package offers a simpler (if somewhat less robust) solution based on R Markdown. CRAN.","If you need to write to an Excel file as well as read, this package is easy to use. CRAN.","There are several functions for modeling data here, but the one I use, CrossTable, simply creates cross-tabs with loads of options -- totals, proprotions and several statistical tests. CRAN.","Basic data cleaning made easy, such as finding duplicates by multiple columns, making R-friendly column names and removing empty columns. It also has some nice tabulating tools, like adding a total row, as well as generating tables with percentages and easy crosstabs. CRAN.","car's recode function makes it easy to bin continuous numerical data into categories or factors. While base R's cut accomplishes the same task, I find recode's syntax to be more intuitive - just remember to put the entire recoding formula within double quotation marks. dplyr's case_when() function is another option worth considering. CRAN.","R interface to the dimple JavaScript library with numerous customization options. Good choice for JavaScript bar charts, among others. GitHub timelyportfolio/rcdimple.","Efficient - and intuitive if you come from another programming language - for loops in R. CRAN.","While this package has many more sophisticated ways to help you format data for graphing, it's worth a download just for the comma(), percent() and dollar() functions. CRAN.","R interface to the Plotly JavaScript library that was open-sourced in late 2015. Basic graphs have a distinctive look which may not be for everyone, but it's full-featured, relatively easy to learn (especially if you know ggplot2) and includes a ggplotly() function to turn graphs created with ggplot2 interactive. CRAN.","R wrapper for the robust and well documented Highcharts JavaScript library, one of my favorite choices for presentation-quality interactive graphics. The package uses ggplot2-like syntax, including options for handling both long and wide data, and comes with plenty of examples. Note that a paid Highcharts license is needed to use this for commercial or government work (it's free for personal and non-profit projects). CRAN. . CRAN.","Is your R code sluggish? This package gives you a visual representative of your code line by line so you can find the speed bottlenecks. CRAN.","Elegant implementation of text mining functions using Hadley Wickham's \"tidy data\" principles. CRAN.","Base R's identical() function tells you whether or not two objects are the same; but if they're not, it won't tell you why. diffobj gives you a visual representation of how two R objects differ. CRAN.","I don't do much forecasting analysis; but if I did, I'd start with this package. CRAN.","This binary data-file format can be read by both Python and R, making data interchange easier between the two languages. It's also built for I/O speed. CRAN.","Another alternative for binary file storage (R-only), fst was built for fast storage and retrieval, with access speeds above 1 GB/sec. It also offers compression that doesn't slow data access too much, as well as the ability to import a specific range of rows (by row number). CRAN.","If you want to use data from a Google API in an R project and there's not yet a specific package for that API, this is the place to turn for authenticating CRAN.","devtools has a slew of functions aimed at helping you create your own R packages, such as automatically running all example code in your help files to make sure everything works. Requires Rtools on Windows and XCode on a Mac. On CRAN.","If you want to install R packages from GitHub, devtools was long the go-to. However, it has a ton of other functions and some hefty dependences. remotes is a lighter-weight alternative if all you want is to install packages from GitHub as well as Bitbucket and some other sources. CRAN. (ghit is another option, but is GitHub-only.)","Windows only: Update your installed version of R from within R. On CRAN.","Seeks to find packages that had previously been installed on your system and need to be re-installed after upgrading R. CRAN.","Initially aimed at package development, usethis now includes useful functions for any coding project. Among its handy features are an edit family that lets you easily update your .Renvironment and .Rprofile files. On CRAN, but install GitHub version from \"r-lib/usethis\" for latest updates.","This package has one function with a single, useful purpose: find your project's working directory. Surprisingly helpful if you want your code to run on more than one system. CRAN.","This package is another that aims to solve one problem, and solve it well: package installation. The main functions will loadi a package that's already installed or installing it first if it's not available. While this is certainly possible to do with base R's require() and an if statement, p_load() is so much more elegant for CRAN packages, or p_load_gh() for GitHub. Other useful options include p_temp(), which allows for a temporary, this-session-only package installation. CRAN.","Turn any R function into a host-able API with a line or two of code. This well-thought-out package makes it easy to use R for data handling in other, non-R coding projects. CRAN.","R wrapper for the powerful and flexible ECharts JavaScript library. It features dozens of chart and graph types, from bar and line charts to sunbursts, heat maps, and geographical maps. Hundreds of customizations not explicitly mentioned in the package docs are nevertheless available; you just need to peruse the original ECharts documentation. (ECharts is an Apache Software Foundation incubator project.)","This is a collection of packages aimed at making it easier for R to work with cloud platforms such as Amazon Web Services, Google and Travis-CI. Some are already on CRAN, some can be found on GitHub.","To be honest, I rarely need the ability create \"geofacets\" -- maps with same-sized blocks in geospatially appropriate locations. However, this package is so cool that I had to include it. Geofaceting is best understood by looking at an example. The package lets you create your own geofacet visualizations using ggplot2 and built-in grids such as US states, EU countries and San Francisco Bay Area counties. Even more impressive, it comes with design-your-own geofacet grid capabilities. CRAN.","This is pretty much pure fun. Yes, getting an audible notification when code finishes running or encounters an error could be useful; but here, the available sounds include options like a fanfare flourish, a Mario Brothers tune, and even a scream. CRAN."],["See the intro vignette","map_df(mylist, myfunction)","read_excel(\"my-spreadsheet.xls\", sheet = 1)","mysheet &lt;- gs_title(\"Google Spreadsheet Title\")","read_csv(myfile.csv)","import(\"myfile\")","describe(mydf)","df_paste() to create a data frame, vector_paste() to create a vector.","sqldf(\"select * from mydf where mycol &gt; 4\")","myjson &lt;- toJSON(mydf, pretty=TRUE)","mytables &lt;- readHTMLTable(myurl)","r &lt;- GET(\"http://httpbin.org/get\")","getSymbols(\"AITINO\", src=\"FRED\")","aapl_key_ratios &lt;- tq_get(\"AAPL\", get = \"key.ratios\")","See the package vignette","See my tutorial","See examples in this blog post.","cSplit(mydata, \"multi_val_column\", sep = \",\", direction = \"long\").","mydf %&lt;&gt;% mutate(newcol = myfun(colname))","See the introductory vignette.","See the testing chapter of Hadley Wickham's book on R packages.","Useful tutorial","str_pad(myzipcodevector, 5, \"left\", \"0\")","mdy(\"05/06/2015\") + months(1)","rollmean(mydf, 7)","editR(\"path/to/myfile.Rmd\")","See the Minimal Examples page.","my_doc &lt;- read_docx() %&gt;% ","jsonedit(mylist)","datatable(mydf)","qplot(factor(myfactor), data=mydf, geom=\"bar\", fill=factor(myfactor))","plot1 + plot2 + plot_layout(ncol=1)","g &lt;- ggplot(mpg, aes( x = displ, y = cty, color = drv) )\r\nmy_gg &lt;- g + geom_point_interactive(aes(tooltip = model), size = 2)\r\nggiraph(code = print(my_gg), width = .7).","dygraph(myxtsobject)","mychart &lt;- gvisColumnChart(mydata)","See package intro","See the author's post on RPubs","See Jennifer Bryan's tutorial","See the package vignettes, starting with the introduction, Simple Features for R.","See my tutorial","geocode(\"492 Old Connecticut Path, Framingham, MA\")","See the package vignette or my mapping in R tutorial","google_directions( origin = c(my_longitude, my_latitude),","See Basic usage of tidycensus.","glue(\"Today is {Sys.Date()}\")","See package README file and my tutorial","See intro video","See this short, easy-to-read blog post","See the tutorial","More info in Using flexdashboard","write.xlsx(mydf, \"myfile.xlsx\")","CrossTable(myxvector, myyvector, prop.t=FALSE, prop.chisq = FALSE)","tabyl(mydf, sort = TRUE) %&gt;% adorn_totals(\"row\")","recode(x, \"1:3='Low'; 4:7='Mid'; 8:hi='High'\")","dimple(mtcars, mpg ~ cyl, type = \"bar\")","foreach(i=1:3) %do% sqrt(i)","comma(mynumvec)","d &lt;- diamonds[sample(nrow(diamonds), 1000), ] plot_ly(d, x = carat, y = price, text = paste(\"Clarity: \", clarity), mode = \"markers\", color = carat, size = carat)","hchart(mydf, \"charttype\", hcaes(x = xcol, y = ycol, group = groupbycol))","profvis({ your code here })","See tidytextmining.com for numerous examples.","diffObj(x,y)","See the Quick start guide.","write_feather(mydf, \"myfile\")","write.fst(mydf, \"myfile.fst\", 100)","See examples on the package website and this gist for use with Google Calendars. CRAN.","run_examples()","remotes::install_github(\"mangothecat/franc\")","updateR()","reinstallr()","edit_r_environ()","my_project_directory &lt;- here()","p_load(dplyr, here, tidycensus)","See the documentation or my article Create your own Slack bots -- and Web APIs -- with R","mtcars %&gt;% e_charts(wt) %&gt;% e_line(mpg)","See the list of packages.","grid_design()","beep(\"wilhelm\")"],["Hadley Wickham","Hadley Wickham","Hadley Wickham","Jennifer Bryan","Hadley Wickham","Thomas J. Leeper &amp; others","Frank E Harrell Jr &amp; others","Miles McBain","G. Grothendieck","Jeroen Ooms &amp; others","Duncan Temple Lang","Hadley Wickham","Jeffrey A. Ryan","Matt Dancho","Hadley Wickham","Hadley Wickham","Hadley Wickham","Ananda Mahto","Stefan Milton Bache &amp; Hadley Wickham","Mark van der Loo &amp; Edwin de Jonge","Hadley Wickham","Matt Dowle &amp; others","Hadley Wickham","Garrett Grolemund, Hadley Wickham &amp; others","Achim Zeileis &amp; others","Simon Garnier","Yihui Xie &amp; others","David Gohel","Kent Russell","RStudio","Hadley Wickham","Thomas Lin Pedersen","David Gohel","JJ Allaire &amp; RStudio","Markus Gesmann &amp; others","Bob Rudis","Bob Rudis","Erich Neuwirth","Edzer Pebesma &amp; others","RStudio","David Kahle &amp;Hadley Wickham","Martijn Tennekes","Michael Dorman","Kyle E. Walker","Jim Hester","Bror Skardhamar","Randy Zwitch","Hadley Wickham &amp; others","RStudio","JJ Allaire, RStudio &amp; others","Alexander Walker","Gregory R. Warnes","Samuel Firke","John Fox &amp; others","Kent Russell","Revolution Analytics, Steve Weston","Hadley Wickham","Carson Sievert &amp; others","Joshua Kunst &amp; others","Winston Chang &amp; others","Julia Silge &amp; David Robinson","Brodie Gaslam &amp; Michael B. Allen","Sean Taylor &amp; Ben Letham at Facebook","Wes McKinney &amp; Hadley Wickham","Mark Klik","Mark Edmondson","Hadley Wickham &amp; others","Gabor Csardi &amp; others","Tal Galili &amp; others","Calli Gross","Hadley Wickham, Jennifer Bryan &amp; RStudio","Kirill Müller","Tyler Rinker","Jeff Allen, Trestle Technology &amp; others","John Coene","Various","Ryan Hafen","Rasmus Bååth"],[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"See my searchable ggplot2 cheat sheet and",null,null,null,"Numerous examples here",null,null,null,null,null,null,null,null,null,null,null,null,"on writing R packages",null,null,null,null,null,null,null,"Also see The Wonders of foreach",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th> <\/th>\n      <th>PACKAGE<\/th>\n      <th>CATEGORY<\/th>\n      <th>DESCRIPTION<\/th>\n      <th>SAMPLE.USE<\/th>\n      <th>AUTHOR<\/th>\n      <th>X6<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"order":[],"autoWidth":false,"orderClasses":false,"columnDefs":[{"orderable":false,"targets":0}]}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->



# Save and install packages


## Save packages



```r
##########################################################333

### 64bit Version of Java needed
#library(XLConnect)
########################################################

############3
#shell("zip")
#ZIP needed
#library(openxlsx)
#path="C:/Program Files/7-Zip/7z.exe"
#Sys.setenv("R_ZIPCMD" = path)
#Sys.setenv("R_ZIPCMD"="C:/RBuildTools/3.4/bin/zip.exe")

###########



ip <- as.data.frame(installed.packages()[,c(1,3:4)])
rownames(ip) <- NULL
ip <- ip[is.na(ip$Priority),1:2,drop=FALSE]
#print(ip, row.names=FALSE)

### No need of java
library(openxlsx)

#wb=read.xlsx(xlsxFile="Packages.xlsx")
#wb <- createWorkbook()

#addWorksheet(wb, "Packages")
#writeData(wb, "Packages", ip, startCol = 2, startRow = 3, rowNames = TRUE)

###########

write.xlsx(ip, "Packages_installed.xlsx", asTable = T)
```

```
## Note: zip::zip() is deprecated, please use zip::zipr() instead
```


## Install packages on new machine


```r
### No need of java
library(openxlsx)

ip <- read.xlsx(xlsxFile = "Packages_installed.xlsx", sheet = 1, skipEmptyRows = FALSE)

packages=as.character(ip[,1])
#packages=c("ggplot2")

packages<-packages[1:100]
#install.packages(packages)
```


# Speeding up package installation


A simple one line tweak can significantly speed up package installation and updates.
## The wonder of CRAN
One of the best features of R is CRAN. When a package is submitted to CRAN, not only is it checked under three versions of R
	• R-past, R-release and R-devel
but also three different operating systems
	• Windows, Linux and Mac (with multiple flavours of each)
CRAN also checks that the updated package doesn’t break existing packages. This last part is particularly tricky when you consider all the dependencies a package like ggplot2 or Rcpp have. Furthermore, it performs all these checks within 24 hours, ready for the next set packages.
What many people don’t realise is that for CRAN to perform this miracle of package checking, it builds and checks these packages in parallel; so rather than installing a single package at a time, it checks multiple packages at once. Obviously some care has to be taken when checking/installing packages due to the connectivity between packages, but R takes care of these details.

## Parallel package installation: Ncpus

If you examine the help package of ?install.packages, there’s a sneaky argument called Ncpus. From the help page:
Ncpus: The number of parallel processes to use for a parallel install of more than one source package.
The default value of this argument is
Ncpus = getOption(‘Ncpus’, 1L)
The getOption() part determines if the value has been set in options(). If no value is found, the default number of processes to use is 1. If you haven’t heard of Ncpus, it’s almost certainly 1, but you can check using


```r
getOption("Ncpus", 1L)
```

```
## [1] 1
```



How many cores can be utilized:


```r
cores = parallel::detectCores()
```
My machine has eight cores 2. So it doesn’t make sense to set Ncpus above 2. 

Set cores and install selected packages


```r
options(Ncpus = cores)
system.time(install.packages(packages))
```


So setting Ncpus to 2 allows us to half the installation time from 409 seconds to around 224 (seconds). Increasing Ncpus to 4 gives a further speed boost. Due to the dependencies between packages, we’ll never achieve a perfect speed-up, e.g. if package X depends on Y, then we have to install X first. However, for a simple change we get an easy speed boost.
Furthermore, setting Ncpus gives a speed boost when updating packages via update.packages().


A permanent change: .Rprofile
Clearly writing options(Ncpus = 6) before you install a package is a pain. However, you can just add it to your .Rprofile file. 

Maybe it is also helpful not to utilize all available cores. This allows packages to be installed in parallel, while giving me a little bit of wiggle room to check email and listen to music.























