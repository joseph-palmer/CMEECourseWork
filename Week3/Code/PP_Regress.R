#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: ggplot practicle for data visualisation

# clear environment
rm(list=ls())

# Load required packages #
require(ggplot2)
require(dplyr)
require(plyr)

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)

# solve mass unit problem - convert those in mg to g.
MyDF <- MyDF %>% rowwise() %>% mutate(Prey.mass = ifelse(Prey.mass.unit == "mg", Prey.mass / 1000, Prey.mass))

# make the plot
p <- qplot(Prey.mass,
      Predator.mass,
      facets = Type.of.feeding.interaction ~.,
      data = MyDF,
      log = "xy",
      xlab = "Prey Mass in grams",
      ylab = "Predator mass in grams",
      shape= I(3),
      colour = Predator.lifestage)
q = p + stat_smooth(method = "lm", fullrange = TRUE) +
  geom_point(shape = I(3)) + theme_bw() +
  theme(legend.position="bottom", legend.title = element_text(face = "bold")) +
  guides(colour = guide_legend(nrow = 1))

print(q)

# Save the plot as pdf
pdf("../Results/PP_Regress_Plot.pdf")
q
dev.off()

# use dlpyl to group by feeding type and predator lifestage to get lm.
grouped_lm <- dlply(MyDF,.(Type.of.feeding.interaction, Predator.lifestage), function(x) lm(Predator.mass~Prey.mass, data = x))

# extract stats from grouped_ml
out <- ldply(grouped_lm, function(x){
  intercept <- summary(x)$coefficients[1]
  slope <- summary(x)$coefficients[2]
  p.val <- summary(x)$coefficients[8]
  r2 <- summary(x)$r.squared
  data.frame(slope, intercept, r2, p.val)
  })

# extract f-statistic
Fstat <- ldply(grouped_lm, function(x) summary(x)$fstatistic[1])
out <- merge(out, Fstat, by = c("Type.of.feeding.interaction","Predator.lifestage"), all = T)

# rename columns
names(out)[7] <- "F.Statistic"
names(out)[6] <- "P.Value"

# write the results to a file (exclude the row names they are not needed)
results_path = "../Results/PP_Regress_Results.csv"
write.csv(out, results_path, row.names = F, quote = F)

# end - everything bellow is trial to run by someone as to why  it is wrong.



# # create a dataframe of unique feeding interaction predator lifestage combinations.
# combinations = expand.grid(unique(MyDF$Type.of.feeding.interaction), unique(MyDF$Predator.lifestage))
# 
# # Standard looping approach #
# 
# # make an empty dataframe to fill with correlation values
# d = data.frame(FeedingType = rep(NA, nrow(combinations)),
#                PreditorLifeStage = rep(NA, nrow(combinations)),
#                Slope = rep(NA, nrow(combinations)),
#                Intercept = rep(NA, nrow(combinations)),
#                R_Squared = rep(NA, nrow(combinations)),
#                F_Value = rep(NA, nrow(combinations)),
#                P_Value = rep(NA, nrow(combinations)))
# 
# # loop through the combinations using the names to run the subseted linear models
# for (i in 1:nrow(combinations)){
#   tfi = combinations[[i,"Var1"]]
#   pls = combinations[[i,"Var2"]]
#   model = subset(MyDF, Type.of.feeding.interaction == tfi & Predator.lifestage == pls)
#   
#   # ignore combinations with no data
#   if (nrow(model) < 1){
#     next
#   }
#   
#   # run linear model and extrat values into the initialized dataframe d
#   mod1 = lm(log(model$Prey.mass) ~ log(model$Predator.mass))
#   sum = summary(mod1)
#   intercept = sum$coefficients[1]
#   slope = sum$coefficients[2]
#   r2 = sum$r.squared
#   fstat = sum$fstatistic[[1]]
#   pval = sum$coefficients[2,4]
#   print(pval)
#   d[i, ] = c(paste(tfi), paste(pls), slope, intercept, r2, fstat, pval)
# }
# 
# # vectorized approach ##
# 
# # make a function that does what the loop did, but pass it the dataframe and the names to subset on.
# MyLM <- function(MyDF, tfi, pls){
#   # subset the data on the combinations passed
#   model = subset(MyDF, Type.of.feeding.interaction == tfi & Predator.lifestage == pls)
#   
#   # return nothing when no combinations exist
#   if (nrow(model) < 1){
#     return(c(paste(tfi), paste(pls), NA, NA, NA, NA, NA))
#   }
#   # run linear model and extrat values into a list
#   mod1 = lm(log(model$Prey.mass) ~ log(model$Predator.mass))
#   sum = summary(mod1)
#   intercept = sum$coefficients[1]
#   slope = sum$coefficients[2]
#   r2 = sum$r.squared
#   fstat = sum$fstatistic[[1]]
#   pval = sum$coefficients[2,4] # ? not sure about this as pvalue looks odd
#   return(c(paste(tfi), paste(pls), slope, intercept, r2, fstat, pval))
# }
# 
# 
# # the looped way of applying the function - extract the tfi and pls to a dataframe
# # (not a vector I know but a way of showing whats going on in the lapply function)
# for (i in 1:nrow(combinations)){
#   tfi = combinations[[i,"Var1"]]
#   pls = combinations[[i,"Var2"]]
#   d[i, ] = MyLM(MyDF, tfi, pls)
# }
# 
# # vectorised alternative to the above mini-loop. this returns a list of the values.
# model_results = lapply(1:nrow(combinations), function(i) MyLM(MyDF, combinations[[i,"Var1"]], combinations[[i,"Var2"]]))
# 
# # the list returned 30 columns and 7 rows. need to transpose it to fix
# transposed_model_results = transpose(model_results)
# 
# # convert the transformed list to a dataframe
# result_df <- as.data.frame(transposed_model_results)
# 
# # add appropriate column headings to the dataframe
# colnames(result_df) <- c("FeedingType",
#                         "PreditorLifeStage",
#                         "Slope",
#                         "Intercept",
#                         "R_Squared",
#                         "F_Value",
#                         "P_Value")
# 
# # write the results to a file (exclude the row names they are not needed)
# results_path = "../Results/PP_Regress_Results.csv"
# write.csv(result_df, results_path, row.names=FALSE)
# 
# 
