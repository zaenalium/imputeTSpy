library(tidyverse)
library(lubridate)
library(zoo)
library(imputeTS)
load("../../imputeTS/data/tsAirgap.rda")
load("../../imputeTS/data/tsAirgapComplete.rda")
load("../../imputeTS/data/tsHeating.rda")
load("../../imputeTS/data/tsNH4.rda")

rownames((tsAirgap))# %>% 

ts_name <- as.yearmon(time(tsAirgap))

df <- data.frame(period = ts_name, data = as.data.frame(tsAirgap))
colnames(df) <- c("period", "number_of_passengers") 

write_csv(df, "../imputeTSpy/imputeTSpy/data/tsAirgap.csv", na = "")

####
z = as.data.frame(tsNH4)

write_lines(z$x,  "data/tsNH4.txt", na = "nan", sep = ",")


####
z = as.data.frame(tsHeating)

write_lines(z$x,  "data/tsHeating.txt", na = "nan", sep = ',')

#conda_install("impyute", envname = "r-reticulate", pip = TRUE)

