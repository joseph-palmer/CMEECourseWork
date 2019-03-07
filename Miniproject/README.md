## __Project Details__
### __Course:__ MSc Computational Methods In Ecology and Evolution
### __Assessment:__ MiniProject
### __Title:__ Modelling foraging distances of the Western Honeybee, _Apis mellifera_: A comparison between rural and urban environments
### __Date of submission:__ 08/03/2019
### __Author:__ Joseph Palmer, joseph.palmer@imperial.ac.uk
### __Affiliation:__ Imperial College London
### __Affiliation Adress:__ Department of Life Sciences, Imperial College London, Ascot, Berkshire, SL5 7PY, United Kingdom
---

# Getting started

#### Cloning this repository
The first step in creating the miniproject is to clone this repository. On the previous page (the main one for CMEECourseWork) you should see a green dropdown button which reads 'Clone or download' click on this and copy the github path in the box displayed.  

Next, open a terminal on your computer and navigate to a location you want to store this project, such as in Documents. Once you have done this type in 'gitclone' and paste the link.  
```
gitclone git@github.com:joseph-palmer/CMEECourseWork.git
```

#### Prerequisites

In order to run this miniproject you must have [python 3.6](https://www.python.org/downloads/release/python-360/) and [R version 3.4.4](https://www.r-project.org/) (or higher) installed on your machine and present in the environment path. This is because the commands python3 and Rscript are used to run python and R scripts respectivley. You must also have [pdfTeX](https://ctan.org/pkg/pdftex?lang=en) version 3.14159265-2.6-1.40.18 or higher installed.

The following python packages are required for instilation: [scipy 1.1.0](https://www.scipy.org/), [pandas 0.23.4](https://pandas.pydata.org/), [re 2.2.1](https://docs.python.org/3/library/re.html). To install with pip3 simply paste the following command into the terminal:


```
pip3 install scipy pandas re
```
NOTE: if you do not have pip3 you can install it with ```sudo apt install pip3```

The following R packages are required for instilation: [xtable 1.8-3](https://cran.r-project.org/web/packages/xtable/index.html), [cowplot 0.9.4](https://cran.r-project.org/web/packages/cowplot/vignettes/introduction.html), [ggplot2 3.1.0](https://ggplot2.tidyverse.org/), [reshape2 1.4.3](https://cran.r-project.org/web/packages/reshape2/reshape2.pdf), [pracma 2.2.2](https://cran.r-project.org/web/packages/pracma/pracma.pdf), [minpack.lm 1.2-1](https://cran.r-project.org/web/packages/minpack.lm/minpack.lm.pdf). The simplest way to install these packages is to open r and install using install.packages. First open the r console by typing ```R``` and then paste in the following commands:  

```
install.packages("xtable")
install.packages("cowplot")
install.packages("ggplot2")
install.packages("reshape2")
install.packages("pracma")
install.packages("minpack.lm")
```

Once you have done the above you are ready to run the code.  

#### Running the project

From the command line navigate to the Code directory of Miniproject. Assuming you git cloned the CMEECourseWork repository into documents the command would be:

```
cd ~/Documents/CMEECourseWork/Miniproject/Code
```

Once here all you need to do is run the file 'run_MiniProject.sh' to run the entire project. ```bash run_MiniProject.sh```. This will first create csv files in the Data directory of foraging distances and produce associated csv metadata files. Then the model fitting will begin producing a table in the directory Results and plots in the directors Results/Plots. Finally, once the analysis is complete the script will compile the miniproject tex and bib document (called JPalmer_MiniProject.tex and JPalmer_MiniProject.bib)  to produce a pdf file (JPalmer_MiniProject.pdf) in the Writeup Directory.
