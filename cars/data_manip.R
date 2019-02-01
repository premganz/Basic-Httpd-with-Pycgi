education <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/robustbase/education.csv", stringsAsFactors = FALSE)
colnames(education) <- c("X","State","Region","Urban.Population","Per.Capita.Income","Minor.Population","Education.Expenditures")
#View(education)
ed_exp2 <- education[c(1:9,22:50),c(1,3:5)]
ed_exp3 <- education[which(education$Region == 2),names(education) %in% c("State","Minor.Population","Education.Expenditures")]
ed_exp4 <- subset(education, Region == 2, select = c("State","Minor.Population","Education.Expenditures"))
library(prob)
#install.packages("dplyr")
library(dplyr)
ed_exp5 <- select(filter(education, Region == 1),c(State,Minor.Population:Education.Expenditures))
space<-probspace(ed_exp5)
print(ed_exp5)
Prob(space,space$State=='ME' & space$Minor.Population>50)

library(reshape2)
df <- dcast(df, ed_exp2$Region ~ ed_exp2$Urban.Population)
df[, 2:ncol(df)] <- df[, 2:ncol(df)] / rowSums(df[, 2:ncol(df)])
df$Sum <- rowSums(df[, 2:ncol(df)])
