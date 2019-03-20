#Source. https://www.r-bloggers.com/how-to-create-professional-reports-from-r-scripts-with-custom-styles/

rmarkdown::render(
  "script.R", 
  output_format = rmarkdown::html_document(
    theme = NULL,
    mathjax = NULL,
    highlight = NULL,
    css = "air.css"
  )
)