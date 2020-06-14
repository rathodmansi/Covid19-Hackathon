data = read.csv('~/Downloads/Weather-Pospercent.csv')
data = data[1:46,]
plot(data$Temperature,data$New.Positive.Percentage, main="Temperature vs One Week Ahead New Positive Percentage",ylab="One Week Ahead New Positive Percentage", xlab = 'Temperature',col="red")
cor(data$Temperature,data$New.Positive.Percentage)

data2 = read.csv('~/Downloads/Averges-Weater-NPP.csv')
data2 = data2[1:7,]
plot(data2$Average.Temperature.for.Week,data2$Average.NPP.for.Week, main="Weekly Temperature vs One Week Ahead Weekly New Positive Percentage",ylab="One Week Ahead Average New Positive Percentage", xlab = 'Average Temperature',col="red")
cor(data2$Average.Temperature.for.Week,data2$Average.NPP.for.Week)
