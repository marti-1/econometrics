library(plotly)
library(zoo)

# fig
gdp <- read.csv("data/GDP.csv")
gdp$DATE <- as.Date(gdp$DATE, format = "%Y-%m-%d")
gdp$year_q <- paste(format(gdp$DATE, '%Y'),quarters(gdp$DATE))

gdp$growth = NA
# compute annualized growth rate
gdp$growth[2:nrow(gdp)] <- ((gdp$GDP[2:nrow(gdp)] / gdp$GDP[1:(nrow(gdp)-1)])**4 - 1)*100
gdp$median_growth = rollapply(gdp$growth, width = 4*5, FUN = median, align = "right", fill = NA)

# read data/DGS20.csv into a data frame called dgs20
dgs20 <- read.csv("data/DGS20.csv")
dgs20$DATE <- as.Date(dgs20$DATE, format = "%Y-%m-%d")
# get year from gdp$DATE
dgs20$year_q <- paste(format(dgs20$DATE, '%Y'), quarters(dgs20$DATE))

dgs20$DGS20 <- as.numeric(dgs20$DGS20)
# drop NA values
dgs20 <- dgs20[!is.na(dgs20$DGS20), ]


gdp_dgs20 <- merge(gdp, dgs20, by = c("year_q"))

# select subset of columns
gdp_dgs20 <- gdp_dgs20[,c("DATE.y", "median_growth", "DGS20")]
# sort gdp_dgs20 by DATE.y
gdp_dgs20 <- gdp_dgs20[order(gdp_dgs20$DATE.y),]

# plot gdp_dgs20 using plotly
p <- plot_ly(gdp_dgs20, x = ~DATE.y, y = ~median_growth, type = "scatter", mode = "lines", name = "GDP Growth") %>%
  add_trace(y = ~DGS20, name = "20 Year Treasury Yield") %>%
  layout(title = "GDP Growth vs. 20 Year Treasury Yield", xaxis = list(title = "Date"), yaxis = list(title = "Percent"))
p
