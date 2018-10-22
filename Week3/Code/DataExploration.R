

# clear environment
rm(list=ls())

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)

# plot preditor mass vs prey mass
plot(MyDF$Predator.mass,MyDF$Prey.mass)

# That doesn't look very meaningful! Let's try taking logarithms. 
# Why? - Because body sizes across species tend to be log-normally distributed, 
# with a lot of small species and a few large ones. Taking a log allows you to inspect the body 
# size range in a meaningful (logarithmic) scale and reveals the true relationship. 
# This also illustrates a important point. Just like statistical analyses, 
# the effectiveness of data visualization too depends on the type of distribution of the data.
plot(log(MyDF$Predator.mass),log(MyDF$Prey.mass))

# change the points
plot(log(MyDF$Predator.mass),log(MyDF$Prey.mass),pch=20)

# lets make it look nice by adding labels
plot(log(MyDF$Predator.mass),log(MyDF$Prey.mass),pch=20, xlab = "Predator Mass (kg)", ylab = "Prey Mass (kg)")

# histograms

# predator body mass histogram
hist(MyDF$Predator.mass)

# The data is heavily right skewed. Take a log to get a better understanding of the distribution
hist(log(MyDF$Predator.mass), xlab = "Predator Mass (kg)", ylab = "Count")

# change the colours
hist(log(MyDF$Predator.mass), xlab = "Predator Mass (kg)", ylab = "Count", col = "lightblue", border = "pink")


# you can place subplots together for easy comparison
par(mfcol=c(2,1)) #initialize multi-paneled plot
par(mfg = c(1,1)) # specify which sub-plot to use first 
hist(log(MyDF$Predator.mass),
     xlab = "Predator Mass (kg)", ylab = "Count", 
     col = "lightblue", border = "pink", 
     main = 'Predator') # Add title
par(mfg = c(2,1)) # Second sub-plot
hist(log(MyDF$Prey.mass),
     xlab="Prey Mass (kg)",ylab="Count", 
     col = "lightgreen", border = "pink", 
     main = 'prey')

# or we could overlap them
hist(log(MyDF$Predator.mass), # Predator histogram
     xlab="Body Mass (kg)", ylab="Count", 
     col = rgb(1, 0, 0, 0.5), # Note 'rgb', fourth value is transparency
     main = "Predator-prey size Overlap") 
hist(log(MyDF$Prey.mass), col = rgb(0, 0, 1, 0.5), add = T) # Plot prey
legend('topleft',c('Predators','Prey'),   # Add legendfrom
       fill=c(rgb(1, 0, 0, 0.5), rgb(0, 0, 1, 0.5))) # Define legend colors


# boxlots can be used to dee the distribution and view the center of mass is (the mean). the line is the median.
# there is no difference between the mean and the median in a normal distribuition.
boxplot(log(MyDF$Predator.mass), xlab = "Location", ylab = "Predator Mass", main = "Predator mass")

# we can now view the locations the data are 
boxplot(log(MyDF$Predator.mass) ~ MyDF$Location, # Why the tilde?
        xlab = "Location", ylab = "Predator Mass",
        main = "Predator mass by location")
# Note the tilde (~). This is to tell R to subdivide or categorize your analysis and plot by the "Factor" location

# we can also combine types
par(fig=c(0,0.8,0,0.8)) # specify figure size as proportion
plot(log(MyDF$Predator.mass),log(MyDF$Prey.mass), xlab = "Predator Mass (kg)", ylab = "Prey Mass (kg)") # Add labels
par(fig=c(0,0.8,0.4,1), new=TRUE)
boxplot(log(MyDF$Predator.mass), horizontal=TRUE, axes=FALSE)
par(fig=c(0.55,1,0,0.8),new=TRUE)
boxplot(log(MyDF$Prey.mass), axes=FALSE)
mtext("Fancy Predator-prey scatterplot", side=3, outer=TRUE, line=-3)

# Saving plots is important - use pdf!
pdf("../Results/Pred_Prey_Overlay.pdf", # Open blank pdf page using a relative path
    11.7, 8.3) # These numbers are page dimensions in inches
hist(log(MyDF$Predator.mass), # Plot predator histogram (note 'rgb')
     xlab="Body Mass (kg)", ylab="Count", col = rgb(1, 0, 0, 0.5), main = "Predator-Prey Size Overlap") 
hist(log(MyDF$Prey.mass), # Plot prey weights 
     col = rgb(0, 0, 1, 0.5), 
     add = T)  # Add to same plot = TRUE
legend('topleft',c('Predators','Prey'), # Add legend
       fill=c(rgb(1, 0, 0, 0.5), rgb(0, 0, 1, 0.5))) 
graphics.off(); #you can also use dev.off()

# using ggplot -  better graphics package
require(ggplot2)

# make a scatter plot of preditor and prey mass
qplot(Prey.mass, Predator.mass, data = MyDF)
qplot(log(Prey.mass), log(Predator.mass), data = MyDF)

# can also colour according to feeding interaction
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, colour = Type.of.feeding.interaction)

# can also do the shape too
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, shape = Type.of.feeding.interaction)

# adding labels
qplot(Prey.mass, Predator.mass, data = MyDF, log="xy",
      main = "Relation between predator and prey mass", 
      xlab = "log(Prey mass) (g)", 
      ylab = "log(Predator mass) (g)")

# can also ad themes
qplot(Prey.mass, Predator.mass, data = MyDF, log="xy",
      main = "Relation between predator and prey mass", 
      xlab = "Prey mass (g)", 
      ylab = "Predator mass (g)") + theme_bw()

# save ggplot plot
pdf("../Results/MyFirst-ggplot2-Figure.pdf")
print(qplot(Prey.mass, Predator.mass, data = MyDF,log="xy",
            main = "Relation between predator and prey mass", 
            xlab = "log(Prey mass) (g)", 
            ylab = "log(Predator mass) (g)") + theme_bw())
dev.off()









