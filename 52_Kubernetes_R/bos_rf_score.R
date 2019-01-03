bos_rf <- readRDS("bos_rf.rds")
library(randomForest)

#* @param df data frame of variables
#* @post /score
function(req, df)
{
    df <- as.data.frame(df)
    predict(bos_rf, df)
}