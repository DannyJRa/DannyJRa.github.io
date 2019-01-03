####COMMENT#############33
input=c()
input$n_breaks=10
input$bw_adjust=1
#####################3


x= hist(faithful$eruptions, probability = TRUE, breaks = as.numeric(input$n_breaks),
        xlab = "Duration (minutes)", main = "Geyser eruption duration")

dens <- density(faithful$eruptions, adjust = input$bw_adjust)
lines(dens, col = "blue")