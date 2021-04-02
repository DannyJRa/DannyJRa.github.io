

#https://rstudio.github.io/renv/articles/local-sources.html
#Fortunately, because MRAN snapshotted CRAN on this date, we can retrieve that binary. For example, on macOS with R 3.6:
renv::install("stringi@1.4.5")




#<project>/renv/local/<package>/<package>_<version>.tar.gz
renv::install("<package>@<version>")