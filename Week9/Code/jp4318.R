#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: November 2018
# Desc: The HPC practicle

# clear environment
rm(list=ls())
#graphics.off()

##############
# Question 1)
##############
species_richness <- function(community){
  # measures the species richness of a system
  return(length(unique(community)))
}

##############
# Question 2)
##############
initialise_max <- function(size){
  # generate an initial state for the simulation community
  # returns the maximum number of possible species for the community size given
  return(seq(size))
}

##############
# Question 3)
##############
initialise_min <- function(size){
  # Generate an alternative initial state for the simulation of a certain size with minimum number of
  # possible species
  return(array(1, size))
}

##############
# Question 4)
##############
choose_two <- function(x){
  # chooses a random number from uniform distribution between 1 and x
  # choose a second random number as above but not equal to the previous one
  # return the numbers as a vector of length 2 *check again
  y = sample(1:x, 2)
  return(c(y[1], y[2]))
}

##############
# Question 5)
##############
neutral_step <- function(community) {
  # Pick one individual to die, one to reproduce and fill the gap left
  remove_replace = choose_two(length(community))
  print(remove_replace)
  community[remove_replace[1]] = community[remove_replace[2]]
  return(community)
}

##############
# Question 6)
##############
neutral_generation <- function(community){
  # simulate several neutral steps over a generation
  # (returns the state of the community after x number of generations)
  # complete generation = number of individuals in the community divided by 2
  generation_time = ceiling(length(community) / 2)
  for (i in 1:generation_time) {
    community = neutral_step(community)
  }
  return(community)
}

##############
# Question 7)
##############
neutral_time_series <- function(initial, duration) {
  # gets the species richness at each generation in the neutral model
  x = rep.int(0, duration + 1)
  x[1] = species_richness(initial)
  for (i in 2:length(x)) {
    initial = neutral_generation(initial)
    x[i] = species_richness(initial)
  }
  return(x)
}

##############
# Question 8)
##############
question_8 <- function() {
  # runs the neutral time series on a poplation of 100 over 200 generations
  y = neutral_time_series(initialise_max(100), duration = 200)
  x = seq(length(y))
  plot(x, y,
       type = "l",
       xlab = "Generations",
       ylab = "Species richness",
       main = "Variaion in species richness over 200 generations")
  return(cbind(x, y))
}

##############
# Question 9)
##############
neutral_step_speciation <- function(community, v) {
  # performs a neutral step but with a random speciaton event given as v.
  remove_replace =  choose_two(length(community))
  if (v <= runif(1)){
    community[remove_replace[1]] = community[remove_replace[2]]
  } else {
    community[remove_replace[1]] =  max(community) + 1
  }
  return(community)
}

##############
# Question 10)
##############
neutral_generation_speciation <- function(community, v){
  # simulate several neutral steps over a generation with speciation
  # (returns the state of the community after x number of generations)
  # complete generation = number of individuals in the community divided by 2
  generation_time = ceiling(length(community) / 2)
  for (i in 1:generation_time) {
    community = neutral_step_speciation(community, v)
  }
  return(community)
}

##############
# Question 11)
##############
neutral_time_series_speciation <- function(initial, duration, v) {
  # gets the species richness at each generation in the neutral model
  x = rep.int(0, duration + 1)
  x[1] = species_richness(initial)
  for (i in 2:length(x)) {
    initial = neutral_generation_speciation(initial, v)
    x[i] = species_richness(initial)
  }
  return(x)
}

##############
# Question 12)
##############
question_12 <- function() {
  # runs the neutral time series with speciation on a poplation of 100 over 200 generations
  # with speciation probability of 0.1
  max_run = neutral_time_series_speciation(initialise_max(100), duration = 200, v = 0.1)
  min_run = neutral_time_series_speciation(initialise_min(100), duration = 200, v = 0.1)
  time = seq(length(max_run))
  plot(time,
       max_run,
       type = "l",
       col = "blue",
       ylim = c(0, 100),
       xlab = "Generations",
       ylab = "Species richness",
       main = "Variaion in species richness over 200 generations with speciation")
  lines(min_run,
        col = "red")
  legend("topright",
         legend=c("max possible species for community",
                  "min possible species for community"),
         fill = c("blue", "red"))
}

##############
# Question 13)
##############
species_abundance <- function(community) {
  # retuns species abundance for all species in the system
  vals = sort(table(community), decreasing = TRUE)
  return(as.numeric(vals))
}

##############
# Question 14)
##############
octaves <- function(abundance) {
  # places the abundances of species into bis where bin = log 2 to power abundance.
  return(tabulate(floor(logb(abundance, base = 2) + 1)))
}

##############
# Question 15)
##############
sum_vect <- function(x, y) {
  # sums 2 vectors, makes them the same length by adding zeros to the smallest vector first
  len = max(c(length(x), length(y)))
  x = c(x, rep(0, len - length(x)))
  y = c(y, rep(0, len - length(y)))
  return(x + y)
}

##############
# Question 16)
##############
question_16 <- function() {
  # runs neutral model for a burn in period of 200 generations before actual 2000 generation run
  community = neutral_generation_speciation(initialise_max(100), v = 0.1)
  burnin_time = 200
  gens = 2000
  for (i in 2: burnin_time) {
    community = neutral_generation_speciation(community, v = 0.1)
  }
  c = 0
  total = c()
  octave_size = c()
  for (i in 1:gens) {
    c = c + 1
    if (c == 20) {
      c = 0
      community = neutral_generation_speciation(community, v = 0.1)
      oct = octaves(species_abundance(community))
      total = sum_vect(total, oct)
      octave_size = append(octave_size, length(oct))
    } else {
      community = neutral_generation_speciation(community, v = 0.1)
    }
  }
  bins = total / (gens / 20)
  bin_names = unlist(lapply(seq(1, max(octave_size)), function(n) paste(2^(n-1), " - ", 2^n - 1)))
  bin_names[1] = "1"
  barplot(bins,
          names.arg = bin_names,
          ylab = "Average Species abundance",
          xlab = "Octaves",
          main = "Neutral model simulations of species abundance over 2000 generations\n N = 100, v = 0.1, simulations = 2000")
}

#######################
# Challenge Question A
#######################
challenge_A_helper <- function(run_type, v) {
  # Gets the mean species richness as a function of time across a large number of repeated simulations
  # set parameters
  # run type 0 gets min, 1 gets max
  simulations = 100
  time_series_length = 200
  
  # initialise the vectors to store the species richness and squared species richness at each time point
  tot_data = rep(0, time_series_length + 1)
  x2_var = rep(0, time_series_length + 1)
  
  # get initialised max and min use
  if (run_type == 0) {
    community = initialise_min(100)
  } else if (run_type == 1) {
    community = initialise_max(100)
  } else {
    print("run_type must be 1 or 0")
    break
  }
  
  # loop through the simulations and get species richness at each time point, populate the vectors tot_data
  # and x2_var with the total values at that time point
  for (i in 1:simulations) {
    example_time_series = neutral_time_series_speciation(community, time_series_length, v)
    tot_data = tot_data + example_time_series
    x2_var = x2_var + example_time_series^2 
  }
  
  # calulcate average from the running total / simulation number
  avg_data = tot_data / simulations
  avg_x2 = x2_var / simulations
  
  # calculate variance, sd and confidence interval
  varience = avg_x2 - avg_data^2
  std = sqrt(varience)
  error = qnorm(0.986) * std / sqrt(simulations)
  
  return(cbind(avg_data, error))
}

challenge_A <- function() {
  # get data to plot for challenge A using challenge_A_helper function.
  data_max = challenge_A_helper(0, 0.2)
  data_min = challenge_A_helper(1, 0.2)
  
  # create the plot
  time = seq(0, length(data_max[,1]) - 1)
  plot(time,
       data_max[,1],
       type = "l",
       col = "blue",
       ylim = c(0, 100),
       xlab = "Generations",
       ylab = "Species richness",
       main = "Mean species richness over 100 generations as a function of time\n")
  lines(time, data_min[,1], col = "red")
  lines(time, data_max[,1] - data_max[,2])
  lines(time, data_max[,1] + data_max[,2])
  lines(time, data_min[,1] - data_min[,2])
  lines(time, data_min[,1] + data_min[,2])
  legend("topright",
         legend=c("Min possible species for community",
                  "Max possible species for community",
                  "97.2% CI"),
         fill = c("blue", "red", "black"))
}


#######################
# Challenge Question B)
#######################
challenge_B_helper <- function(community, v) {
  # set simulations and tme step
  simulations = 100
  time_series_length = 200
  
  # initialise the vectors to store the species richness and squared species richness at each time point
  tot_data = rep(0, time_series_length + 1)
  x2_var = rep(0, time_series_length + 1)
  for (i in 1:simulations) {
    example_time_series = neutral_time_series_speciation(community, time_series_length, v)
    tot_data = tot_data + example_time_series
    x2_var = x2_var + example_time_series^2 
  }
  
  # calulcate average from the running total / simulation number
  avg_data = tot_data / simulations
  avg_x2 = x2_var / simulations
  
  # calculate variance, sd and confidence interval
  varience = avg_x2 - avg_data^2
  std = sqrt(varience)
  error = qnorm(0.986) * std / sqrt(simulations)
  
  return(cbind(avg_data, error))
}

challenge_B <- function() {
  for (v in 1:100) {
    if (100 %% v == 0){
      print(v)
      run = 100/ v
      output = challenge_B_helper(rep(seq(1, v), run), 0.2)
      time = seq(1, length(output[,1]))
      if(v < 2) {
        plot(time, output[,1], type = "l", xlim = c(0, 100), ylim = c(0, 100), xlab = "Generations", ylab = "Species Richness")
      } else {
        lines(output[,1], col = v)
      }
    }
  }
}

##############
# Question 17)
##############
cluster_run <- function(speciation_rate, size, wall_time, interval_rich, interval_oct, burn_in_generations, output_file_name) {
  # function to run simulations for a set amount of time, returning species richness at burn in and abundace throughout.
  # ste the community with minimal diversity
  # change wall time from miinutes to seconds
  wall_time = wall_time * 60
  community = initialise_min(size)
  # run neautral generations over a specified period of time (counter records how many simulations we have done)
  total_elapsed_time = 0
  counter = 0
  species_richness_burnin = c()
  species_abundance_octaves = c()
  start = as.numeric(proc.time()[3])
  while (total_elapsed_time < wall_time) {
    # start recording the time taken to run the simulations
    counter = counter + 1
    # run the simulation
    community = neutral_generation_speciation(community, speciation_rate)
    # record species abundance at set intervals
    if (counter %% interval_oct == 0) {
      ans = octaves(species_abundance(community))
      species_abundance_octaves = append(species_abundance_octaves, list(octaves(species_abundance(community))))
    }
    # record species richness up to burn in generations at set intervals
    if ((counter <= burn_in_generations) && (counter %% interval_rich == 0)) {
      species_richness_burnin = append(species_richness_burnin, species_richness(community), length(species_richness_burnin))
    }
    # add the time taken so far to the elapsed time the while loop evaluates
    end = as.numeric(proc.time()[3])
    total_elapsed_time = end - start
  }
  # save the simulation output to r data file
  save(species_richness_burnin,
       species_abundance_octaves,
       # time ran on simulation
       total_elapsed_time,
       # state f community at end of simulation
       community,
       # input parameters
       speciation_rate,
       size,
       wall_time,
       interval_rich,
       interval_oct,
       burn_in_generations,
       file = output_file_name)
  return(0)
}

###################################
# Question 18 & 19 ) See zip file.
###################################

#################################################
# Interporate output of HPC script (Question 20)
#################################################
question_20 <- function() {
  # load the data (all files with extention .rda)
  datafiles = list.files(path = "../jp4318_hpc_files/Results/", pattern = "*.rda")
  # work out what datafiles correspond to what size from each file
  size_500 = c()
  size_1000 = c()
  size_2500 = c()
  size_5000 = c()
  for(i in datafiles) {
    filestring = paste0("../jp4318_hpc_files/Results/", i)
    load(filestring)
    switch(as.character(size),
           "500" = {size_500 = append(size_500, filestring)},
           "1000" = {size_1000 = append(size_1000, filestring)},
           "2500" = {size_2500 = append(size_2500, filestring)},
           "5000" = {size_5000 = append(size_5000, filestring)})
  }
  # set partition for the bar plots produced
  par(mfrow=c(2,2), oma=c(0,0,2,0))
  # set storage vector for octaves to be returned
  return_octaves = c()
  # loop through each size, then loop through each file of that size
  # get the octaves average for each file, then sum these averages and take an average
  # for each size, then plot these in a bar plot 
  for (files in list(size_500, size_1000, size_2500, size_5000)){
    # set average vector for each size
    simulation_octaves = c()
    for (i in files) {
      # load the file into mem and set an empty vector for the octave totals
      load(i)
      octaves_sum = c()
      # calculate what part of the species abundance octaves correspond to the burn in period
      burnin_endpoint = burn_in_generations / interval_oct
      # loop through the octave vectors for the main run and add to the running total
      for (data in species_abundance_octaves[burnin_endpoint:length(species_abundance_octaves)]) {
        octaves_sum = sum_vect(octaves_sum, data)
      }
      # average the octaves for the number of octaves recorded
      avg_octaves = unlist(lapply(octaves_sum, function(n) n/(length(species_abundance_octaves) - burnin_endpoint)))
      # add the averages to the size running total
      simulation_octaves = sum_vect(simulation_octaves, avg_octaves)
    }
    # average the size sum of the averages for each file
    avg_simulation_octaves = unlist(lapply(simulation_octaves, function(n) n/length(files)))
    # produce the final barplot with labels and title
    
    # create labels fot the plot.
    len_bins = c(0:(length(avg_simulation_octaves) - 1))
    bins = c()
    for (i in len_bins) {
      if (i > 0) {
        max_bin = 2^i
        min_bin = 2^(i + 1) - 1
        bins = append(bins, paste0(max_bin, " -\n", min_bin))
      } else {
        max_bin = 2^i
        bins = append(bins, max_bin)
      }
    }
    
    barplot(avg_simulation_octaves,
            main = paste("Size =", size),
        #    names.arg = bins[1:length(avg_simulation_octaves)],
            xlab = "Octaves",
            ylab = "Average Species Abundance")
    title(paste("Species Richness", speciation_rate), outer = T)
    
    # return the octaves to main to be returned
    return_octaves = append(return_octaves, list(avg_simulation_octaves)) 
  }
  return(return_octaves)
}

#############
# Challenge C
#############
Challenge_C_helper <- function(size) {
  # mean species richness against generation to better identify accurate burn in time
  simulations = 10
  time_series_length = 100
  speciation_rate = 0.2
  community = initialise_min(size)
  tot_data = 0
  
  for (i in 1:simulations) {
    example_time_series = neutral_time_series_speciation(community, time_series_length, speciation_rate)
    tot_data = tot_data + example_time_series
  }
  
  # calulcate average from the running total / simulation number
  avg_data = tot_data / simulations
  return(avg_data)
}

Challenge_C <- function() {
  s_500 = Challenge_C_helper(500)
  s_1000 = Challenge_C_helper(1000)
  s_2500 = Challenge_C_helper(2500)
  s_5000 = Challenge_C_helper(5000)
  sizes = list(s_1000, s_2500, s_5000)
  time = seq(0, length(s_500) - 1)
  plot(time, s_500, type = "l", xlim = c(0, 100), ylim = c(0, 2500), xlab = "Generations", ylab = "Average Species Richness")
  c = 1
  for (i in sizes) {
    c = c + 1
    lines(i, col = c)
  }
}


#############
# Challenge D
#############
Challenge_D <- function(J, v) {
  # coalesence code
  lineages = rep(1, J)
  abundances = c()
  N = J
  theta = v * (J-1/1-v)
  while (N > 1) {
    j = sample(length(lineages), 1)
    randnum = runif(1)
    if (randnum < (theta / (theta + N - 1))) {
      abundances = append(abundances, lineages[j])
    } else {
      i = sample(length(lineages), 1)
      while (i == j) {
        i = sample(length(lineages), 1)
      }
      lineages[i] = lineages[i] + lineages[j]
    }
    lineages = lineages[-j]
    N = N - 1
  }
  abundances = append(abundances, lineages)
  return(abundances)
}

RunChallengeD <- function(simulation_number, speciation_rate) {
  #### code to run coalescence with a given speciation rate and number of simulations
  sample_sizes = c(500)#, 1000, 2500, 5000)
  for (i in 1:length(sample_sizes)) {
    print(paste("Community size =", sample_sizes[i]))
    total_oct = c()
    for (ii in 1:simulation_number) {
      x = Challenge_D(sample_sizes[i], speciation_rate)
      #  spa = species_abundance(x)
      oct = octaves(x)
      total_oct = sum_vect(total_oct, oct)
    }
    average_oct = total_oct / simulation_number
    return(average_oct)
  }
}

Create_Graph_ChallengeD <- function() {
  forwards_octaves = question_20()
  coalescence = RunChallengeD(30000, 0.002125)
  forwards = forwards_octaves[[1]]
  bartable = cbind(forwards, coalescence)
  # clear the previous graphics
  dev.off()
  barplot(bartable,
          beside = T,
          #    names.arg = bins[1:length(avg_simulation_octaves)],
          xlab = "Octaves",
          ylab = "Average Species Abundance")
}

################################################
#                  Fractals                    #
################################################

##############
# Question 21)
##############
question_21 <- function() {
  # calculates the dimentions for the two objects in the workbook.
  # A) - The 2D image on the left hand side.
  # A subset image appears 8 times within its larger image.
  # The Large image ratio to smaller image, i.e. how much it must reduce or increase by is 3.
  dimension_a = log(8) / log(3)
  
  # B) - The 3D image on the right hand side.
  # The larger ploks are made of smaller 3D blocks. 
  # The top and bottom row has 8 of these blocks. The midle had 4 giving a total of 20
  # The large to small image ratio is 3 just as in the previous one.
  dimension_b = log(20) / log(3)
}

##############
# Question 22)
##############
chaos_game <- function() {
  # initialised the plot
  plot(0:5, 0:5, type = "n", xaxt = "n", yaxt = "n", ann = F, bty = "n")
  # set the plot values to randomly choose from
  A = c(0, 0)
  B = c(3, 4)
  C = c(4, 1)
  # place vector in a list
  vector_list = list(A, B, C)
  # set the starting value for the plot
  plotter = c(0, 0)
  for (i in 1:100000) {
    # randomly select some points to draw towards
    random_selection = sample(3, 1)
    target = unlist(vector_list[random_selection])
    # make a new point half way towards the desired point (diferance - (difference / 2))
    # max - difference between max and min / 2.
    new_x = max(plotter[1], target[1]) - ((max(plotter[1], target[1]) - min(plotter[1], target[1]))/2)
    new_y = max(plotter[2], target[2]) - ((max(plotter[2],  target[2]) - min(plotter[2], target[2]))/2)
    # plot the point 
    points(new_x, new_y, cex = 0.05)
    # re set pointer to the new position
    plotter = c(new_x, new_y)
  }
}

##############
# Question 22) - E) Challenge question -
##############
Challenge_E <- function() {
  # save seed state
  seed_state <- .Random.seed
  # set the seed
  set.seed(9)
  # initialised the plot
  plot(0:5, 0:5, type = "n", xaxt = "n", yaxt = "n", ann = F, bty = "n")
  # set the plot values to randomly choose from
  A = c(0, 0)
  B = c(2, 3)
  C = c(4, 0)
  # place vector in a list
  vector_list = list(A, B, C)
  # set the starting value for the plot
  plotter = c(0, 5)
  for (i in 1:100000) {
    # randomly select some points to draw towards
    random_selection = sample(3, 1)
    target = unlist(vector_list[random_selection])
    # make a new point half way towards the desired point (diferance - (difference / 2))
    # max - difference between max and min / 2.
    new_x = max(plotter[1], target[1]) - ((max(plotter[1], target[1]) - min(plotter[1], target[1]))/2)
    new_y = max(plotter[2], target[2]) - ((max(plotter[2],  target[2]) - min(plotter[2], target[2]))/2)
    # plot the point
    if (i < 20) {
      points(new_x, new_y, cex = 1, pch = 16)
    } else {
      points(new_x, new_y, cex = 0.05, col = random_selection*2)
    }
    # re set pointer to the new position
    plotter = c(new_x, new_y)
  }
  # return the original seed state
  .Random.seed <- seed_state
}


##############
# Question 23)
##############
turtle <- function(start, direction, length) {
  # draw a line of given length from a given point in a given direction
  # calculate end point of the line using the start point as the referrence start point
  end_y = (sin(direction) * length) + start[2]
  end_x = (cos(direction) * length ) + start[1]
  # add a line connecting the start to the calculated end point
  # ectra credit make it funky colours
  colnumber = 1 #sample(10, 1)
  segments(start[1], start[2], end_x, end_y, col = colnumber)
  # return the end point
  return(c(end_x, end_y))
}

##############
# Question 24)
##############
elbow <- function(start, direction, length) {
  # calls turtle to draw a pair of lines
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length = 0.95 * length
  next_direction = direction - pi/4
  # call turtle to draw the next line
  turtle(end, next_direction, next_length)
}

##############
# Question 25)
##############
spiral <- function(start, direction, length) {
  # calls turtle to draw a spiral
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length = 0.95 * length
  next_direction = direction - pi/4
  # call spiral to draw the next part of the spiral
  spiral(end, next_direction, next_length)
}

##############
# Question 26)
##############
spiral_2 <- function(start, direction, length) {
  # calls turtle to draw a spiral but stops if length is below a certain value
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length = 0.95 * length
  next_direction = direction - pi/4
  # call spiral to draw the next part of the spiral
  if ( length > 0.01) {
    spiral_2(end, next_direction, next_length)
  }
}

##############
# Question 27)
##############
tree <- function(start, direction, length) {
  # calls turtle to draw a spiral but stops if length is below a certain value
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length = 0.65 * length
  next_direction_right = direction - (pi/4)
  next_direction_left = direction + (pi/4) # - ((3 * pi)/4)
  # call spiral to draw the next part of the spiral
  if ( length > 0.1) {
    tree(end, next_direction_right, next_length)
    tree(end, next_direction_left, next_length)
  }
}

##############
# Question 28)
##############
fern <- function(start, direction, length) {
  # calls turtle to draw a spiral but stops if length is below a certain value
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length_right = 0.87 * length
  next_length_left =  0.38 * length
  next_direction_right = direction
  next_direction_left = direction + (pi/4) # - ((3 * pi)/4)
  # call spiral to draw the next part of the spiral
  if ( length > 0.01) {
    fern(end, next_direction_right, next_length_right)
    fern(end, next_direction_left, next_length_left)
  }
}

##############
# Question 29)
##############
fern_2 <- function(start, direction, length, dir, recursive_number = 0) {
  # calls turtle to draw a spiral but stops if length is below a certain value
  # set blank area for plot
  if (recursive_number == 0){
    plot(-50:50, -50:50, type = "n", xaxt = "n", yaxt = "n", ann = F, bty = "n")
    recursive_number = recursive_number + 1
  }
  # store the first turtle line end point for the start of the next turtle call
  end = turtle(start, direction, length)
  # calcuate the length and director for the next line
  next_length_right = 0.87 * length
  next_length_left =  0.38 * length
  next_direction_right = direction
  if (dir == 1) {
    next_direction_left = direction + (pi/4)
  } else if (dir == -1) {
    next_direction_left = direction - (pi/4)
  }
  # alternate the dir from the previous
  dir_pass = dir * -1
  # call spiral to draw the next part of the spiral
  if (length > 0.1) {
    # to make furl, it need to go in same direction as previous one, so change the dir back to the previous call
    fern_2(end, next_direction_left, next_length_left, - dir_pass, recursive_number)
    # this is to go straight up
    fern_2(end, next_direction_right, next_length_right, dir_pass, recursive_number)
  }
}

#############
# Challenge F
#############
Challenge_F <- function(distance, start_x, start_y, colour = 1){
  direction = (pi/3)
  end_x = start_x
  end_y = start_y + distance
  segments(start_x, start_y, end_x, end_y, col = colour)
  new_x = end_x
  new_y = end_y
  end_y = (sin(direction) * (distance/2)) + new_y
  end_x = (cos(direction) * (distance/2)) + new_x
  segments(new_x, new_y, end_x, end_y, col = colour)
  if (distance > 1) {
    newdistance = distance / 2
    if (distance < 10) {
      colour = 4
    } else {
    }
    Challenge_F(newdistance, end_x, end_y, colour)
  }
  direction = 2 * direction
  end_y = (sin(direction) * (distance/2)) + new_y
  end_x = (cos(direction) * (distance/2)) + new_x
  segments(new_x, new_y, end_x, end_y)
  if (distance > 1){
    distance = distance / 2
    if (distance < 10) {
      colour = 4
    } else {
    }
    Challenge_F(distance, end_x, end_y, colour)
  }
}

run_challenge_f <- function() {
  plot(-50:50, -50:50, type = "n", xaxt = "n", yaxt = "n", ann = F, bty = "n")
  Challenge_F(30, 0, -40)
}

#############
# Challenge G
#############

# Challenge_G <- function(s, d, l, f, r = 0) {
#   if(r == 0){
#     bp()
#     r = r + 1
#   }
#   e = turtle(s, d, l)
#   x = 0.87 * l
#   y =  0.38 * l
#   z = d
#   if (f == 1) {
#     A = d + (pi/4)
#   } else {
#     A = d - (pi/4)
#   }
#   Q = f * -1
#  if (l > 0.1) {
#    Challenge_G(e, A, y, - Q, r)
#    Challenge_G(e, z, x, Q, r)
#  }
# }

##################################################################################################################
#                                                         end                                                    #
##################################################################################################################