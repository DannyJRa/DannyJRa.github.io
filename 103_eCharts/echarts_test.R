#remotes::install_github("JohnCoene/echarts4r")

# prepare data
df <- state.x77 %>% 
  as.data.frame() %>% 
  tibble::rownames_to_column("State")
library(echarts4r) # load echarts4r

pp=df %>% 
  e_charts(x = State) %>% # initialise and set x
  e_line(serie = Population) # add a line

# save the widget
library(htmlwidgets)
saveWidget(pp, file=paste0( getwd(), "/ggplotlyBubblechart.html"))