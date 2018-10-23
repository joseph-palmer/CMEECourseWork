### script that makes plots with ggplot2.

# clear environment
rm(list=ls())

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)

# load ggplot2
require(ggplot2)

## using quick plot
# plot of preditor and prey mass
qplot(Prey.mass, Predator.mass, data = MyDF)

# make a log plot
qplot(log(Prey.mass), log(Predator.mass), data = MyDF)

# colour according to feeding interaction
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, colour = Type.of.feeding.interaction)

# as above but change the shape
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, shape = Type.of.feeding.interaction)

# asthetic mappings (chose red but ggplot picked the shade of red)
qplot(log(Prey.mass), log(Predator.mass), 
      data = MyDF, colour = "red")

# to choose the actual red use I()
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, colour = I("red"))

# similar for point size...
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, size = 3) # with ggplot size mapping
qplot(log(Prey.mass), log(Predator.mass),  data = MyDF, size = I(3)) #no mapping

# Because there are so many points, we can make them semi-transparent using alpha so that the overlaps can be seen:
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, colour = Type.of.feeding.interaction, alpha = I(.5))
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, colour = Type.of.feeding.interaction, alpha = .5)

# add a smoother to the plot
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, geom = c("point", "smooth"))

# If we want to have a linear regression, we need to specify the method as being lm:
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, geom = c("point", "smooth")) + geom_smooth(method = "lm")

# can also use smoother for each type of interaction (although looks silly)
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, geom = c("point", "smooth"), 
      colour = Type.of.feeding.interaction) + geom_smooth(method = "lm")
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, geom = c("point", "smooth"),
      colour = Type.of.feeding.interaction) + geom_smooth(method = "lm",fullrange = TRUE) # extend the lines to full range

# see how the ratio between preditor and prey mass changes according to the type of interaction
qplot(Type.of.feeding.interaction, log(Prey.mass/Predator.mass), data = MyDF)
qplot(Type.of.feeding.interaction, log(Prey.mass/Predator.mass), data = MyDF, geom = "jitter") # jitter to get a better idea of the spread

# or make a box plot
qplot(Type.of.feeding.interaction, log(Prey.mass/Predator.mass), data = MyDF, geom = "boxplot")

# histogram of preditor-prey mass ratios
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "histogram")
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "histogram", 
      fill = Type.of.feeding.interaction) # colour acording to feeding interaction
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "histogram", 
      fill = Type.of.feeding.interaction, binwidth = 1) # define bin width

# easiery to read is a smooth density
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "density", 
      fill = Type.of.feeding.interaction)
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "density", 
      fill = Type.of.feeding.interaction, 
      alpha = I(0.5)) # make transparent for visable overlaps
qplot(log(Prey.mass/Predator.mass), data = MyDF, geom =  "density", 
      colour = Type.of.feeding.interaction) # or just get the lines

# multifaciting plots is nicer in ggplot than lattice() Note, changing the side that ~. appears on alters rows or column look.
qplot(log(Prey.mass/Predator.mass), facets = Type.of.feeding.interaction ~., data = MyDF, geom =  "density")
qplot(log(Prey.mass/Predator.mass), facets =  .~ Type.of.feeding.interaction, data = MyDF, geom =  "density")

# you can also have combinations whch can get quite large
qplot(log(Prey.mass/Predator.mass), facets = .~ Type.of.feeding.interaction + Location, 
      data = MyDF, geom =  "density")

qplot(log(Prey.mass/Predator.mass), facets = .~ Location + Type.of.feeding.interaction, 
      data = MyDF, geom =  "density")

# you can set axis to be log scaled which is nicer for logs
qplot(Prey.mass, Predator.mass, data = MyDF, log="xy")

# adding plot annotations
qplot(Prey.mass, Predator.mass, data = MyDF, log="xy",
      main = "Relation between predator and prey mass", 
      xlab = "log(Prey mass) (g)", 
      ylab = "log(Predator mass) (g)")
# you can also add themes
qplot(Prey.mass, Predator.mass, data = MyDF, log="xy",
      main = "Relation between predator and prey mass", 
      xlab = "Prey mass (g)", 
      ylab = "Predator mass (g)") + theme_bw()

# saving the plot is like before, using plot keeps the whole command together to be used in a script
pdf("../Results/MyFirst-ggplot2-Figure.pdf")
print(qplot(Prey.mass, Predator.mass, data = MyDF,log="xy",
            main = "Relation between predator and prey mass", 
            xlab = "log(Prey mass) (g)", 
            ylab = "log(Predator mass) (g)") + theme_bw())
dev.off()

# geom Specifies the geometric objects that define the graph type
# barplot
qplot(Predator.lifestage, data = MyDF, geom = "bar")

# boxplot
qplot(Predator.lifestage, log(Prey.mass), data = MyDF, geom = "boxplot")

# density
qplot(log(Predator.mass), data = MyDF, geom = "density")

# histogram
qplot(log(Predator.mass), data = MyDF, geom = "histogram")

# scatterplot
qplot(log(Predator.mass), log(Prey.mass), data = MyDF, geom = "point")

# smooth
qplot(log(Predator.mass), log(Prey.mass), data = MyDF, geom = "smooth")

# can also add methods for a line, such as linear model
qplot(log(Predator.mass), log(Prey.mass), data = MyDF, geom = "smooth", method = "lm")

## Full plotting with ggplot - qplot only allows one dataset to be used. need ggplot to create layers

# to start must specify the data and asthetics
p <- ggplot(MyDF, aes(x = log(Predator.mass),
                      y = log(Prey.mass),
                      colour = Type.of.feeding.interaction))

# we now have a graphics object (which is empty but has whats specified)
p

# plot is blank because we have not specified a geometry
p + geom_point()

# we can use the + sign to concatonate different commands
p <- ggplot(MyDF, aes(x = log(Predator.mass), y = log(Prey.mass), colour = Type.of.feeding.interaction ))
q <- p + geom_point(size=I(2), shape=I(10)) + theme_bw()
q

# remove the ledgend
q + theme(legend.position = "none")

## plotting a matrix
require(reshape2)
GenerateMatrix <- function(N){
  M <- matrix(runif(N * N), N, N)
  return(M)
}
M <- GenerateMatrix(10)
Melt <- melt(M)
p <- ggplot(Melt, aes(Var1, Var2, fill = value)) + geom_tile()
p
p + geom_tile(colour = "black") # add black lines to divide the cells
p + theme(legend.position = "none") # remove ledgend

# remove all the rest
p + theme(legend.position = "none", 
          panel.background = element_blank(),
          axis.ticks = element_blank(), 
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.text.x = element_blank(),
          axis.title.x = element_blank(),
          axis.text.y = element_blank(),
          axis.title.y = element_blank())
p + scale_fill_continuous(low = "yellow", high = "darkgreen") # change the colours
p + scale_fill_gradient2()
p + scale_fill_gradientn(colours = grey.colors(10))
p + scale_fill_gradientn(colours = rainbow(10))
p + scale_fill_gradientn(colours = c("red", "white", "blue"))

## Plotting two dataframes (Girko's circular Law)
# According to Girko's circular law, the eigenvalues of a matrix M of size N×N are approximately contained in a circle 
# in the complex plane with radius N−−√. Let's draw the results of a simulation displaying this result.

#First, we need to build a function object that will calculate the ellipse (the perdicted bounds of the eigenvalues):
build_ellipse <- function(hradius, vradius){ # function that returns an ellipse
  npoints = 250
  a <- seq(0, 2 * pi, length = npoints + 1)
  x <- hradius * cos(a)
  y <- vradius * sin(a)  
  return(data.frame(x = x, y = y))
}
N <- 250 # Assign size of the matrix

M <- matrix(rnorm(N * N), N, N) # Build the matrix

eigvals <- eigen(M)$values # Find the eigenvalues

eigDF <- data.frame("Real" = Re(eigvals), "Imaginary" = Im(eigvals)) # Build a dataframe

my_radius <- sqrt(N) # The radius of the circle is sqrt(N)

ellDF <- build_ellipse(my_radius, my_radius) # Dataframe to plot the ellipse

names(ellDF) <- c("Real", "Imaginary") # rename the columns

# plot the eigenvalues
p <- ggplot(eigDF, aes(x = Real, y = Imaginary))
p <- p +
  geom_point(shape = I(3)) +
  theme(legend.position = "none")

# now add the vertical and horizontal line
p <- p + geom_hline(aes(yintercept = 0))
p <- p + geom_vline(aes(xintercept = 0))

# finally, add the ellipse
p <- p + geom_polygon(data = ellDF, aes(x = Real, y = Imaginary, alpha = 1/20, fill = "red"))
p

## Annotating plots
a <- read.table("../Data/Results.txt", header = TRUE)
head(a)
a$ymin <- rep(0, dim(a)[1]) # append a column of zeros

# Print the first linerange
p <- ggplot(a)
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y1,
  size = (0.5)
),
colour = "#E69F00",
alpha = 1/2, show.legend = FALSE)

# Print the second linerange
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y2,
  size = (0.5)
),
colour = "#56B4E9",
alpha = 1/2, show.legend = FALSE)

# Print the third linerange:
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y3,
  size = (0.5)
),
colour = "#D55E00",
alpha = 1/2, show.legend = FALSE)

# Annotate the plot with labels:
p <- p + geom_text(data = a, aes(x = x, y = -500, label = Label))

# now set the axis labels, remove the legend, and prepare for bw printing
p <- p + scale_x_continuous("My x axis",
                            breaks = seq(3, 5, by = 0.05)) + 
  scale_y_continuous("My y axis") + 
  theme_bw() + 
  theme(legend.position = "none") 
p

# Mathmatical notation
x <- seq(0, 100, by = 0.1)
y <- -4. + 0.25 * x +
  rnorm(length(x), mean = 0., sd = 2.5)

# and put them in a dataframe
my_data <- data.frame(x = x, y = y)

# perform a linear regression
my_lm <- summary(lm(y ~ x, data = my_data))

# plot the data
p <-  ggplot(my_data, aes(x = x, y = y,
                          colour = abs(my_lm$residual))
) +
  geom_point() +
  scale_colour_gradient(low = "black", high = "red") +
  theme(legend.position = "none") +
  scale_x_continuous(
    expression(alpha^2 * pi / beta * sqrt(Theta)))

# add the regression line
p <- p + geom_abline(
  intercept = my_lm$coefficients[1][1],
  slope = my_lm$coefficients[2][1],
  colour = "red")
# throw some math on the plot
p <- p + geom_text(aes(x = 60, y = 0,
                       label = "sqrt(alpha) * 2* pi"), 
                   parse = TRUE, size = 6, 
                   colour = "blue")

p

## GGthemes

library(ggthemes)

p <- ggplot(MyDF, aes(x = log(Predator.mass), y = log(Prey.mass),
                      colour = Type.of.feeding.interaction )) +
  geom_point(size=I(2), shape=I(10)) + theme_bw()

p + geom_rangeframe() + # now fine tune the geom to Tufte's range frame
  theme_tufte() # and theme to Tufte's minimal ink theme