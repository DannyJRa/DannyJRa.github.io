#https://appsilon.com/create-outstanding-dashboards-with-the-new-semantic-dashboard-package/

library(shiny)
library(semantic.dashboard)

ui <- dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody()
)

server <- shinyServer(function(input, output, session) {
  
})

shinyApp(ui, server)