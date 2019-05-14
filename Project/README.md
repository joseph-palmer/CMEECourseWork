# MSc Computational Methods in Ecology and Evolution Project.
### Joseph Palmer: <joseph.palmer18@imperial.ac.uk>
### Update Date: 14/05/2019

__Note__: This Project is ongoing and the contents of these folders and this read me is subject to change daily.

---

#### Overview
* The data for the project can be found in: __Data/__
* The code for this project can be found in: __Code/__
* The results of this project are found in: __Results/__
* The writeups can be found in: __WriteUp/__
* The software package (under development) is found in: __Code/mletools/__

The above folders contain everything required to run the project.

The folder __Testing/__ and its subfolders contains testing scripts that are informative to me whilst working things out. These folders are not critical to the project running but store some working outs of methods before I impliment them in the main code under version control.


Part of the objective of this project is to produce software to impliment a sum of exponentials analysis through maximum likelihood. This software is writen in python and will be a python package with an interface for R and a GUI. The ongoing code for this package is in __Code/mletools_V1/__. The script mletester.py in Code runs a test of the package.

#### What the package can do so far

* Fits exponential, lognormal, normal and gamma distributions to data sampled from distributions using numpy.random as well as the actual bee foraging data using MLE.
* Creates plots of these fits with associated confidence intervals.
* Produces comparative stats of AIC and weighted AIC scores.
* Can do 2 and 3 rate paramater sum of exponentials.
* Sum of exponentials set up with flexible equations. 

These are implimented and can be extended to any data provided if desired.

#### Update of the day:

__10/05/2019:__ Spoke to Tin-Yu regarding the likelihood of the function. His advice was to avoid manually deriving the likelihood and log-likelihood since the computer can do it. Demonstration in class was more for analyitical solutions. Under this advice I have the function now as log(product(equation)) which seams to be working, but the results are variable. I canot get a better log-likelihood than a simple exponential on the rural data, which is serving as ideal test data for this. The function has odd behaviour. With fixed rates or 1 and 2 the prob (p) values fix to 1. With everything fixed the optimizer tends to focus more on the other paramaters and prefers to lower the p as much as it can under a 2 p model. With more paramaters it often just fails. Using the SLSQP method of minimize instead of l-bfgs-b yields the same loglikelihood as the simple exponential for 2 p model. But adding in more paramaters causes this to break. All methods are highly variable to changes in p startig values, the starting values of the rates however have little influence. I will discuss this more with vincent. In the mean time I have spoken with Francis who kindly gave me a tutorial on git flow. In addition to mainitaing test script in the CMEE course work directory I have also made a new repository for the program to go in. All backups to box have been carried out, but I need to assemble the external hard-drive at some point.

__14/05/2019:__ Messing around with the bounds I have managed to improve the loglikelihood scores by relaxing bounds on the paramaters but maintaining constraints with in the function (e.g. sum of p must be between 0 and 1). I was able to vary performance on the rural data  by chaning the starting values for the prob values. This heavily impacts where the minimizer converges too. The results are odd as higher likelihood doesn't improve visual fit on the plot once likelihood gets above -240. Up to that it is better than the exponential at -242 and you can see where the code wants to go to, but it is finding problems beyond this value, its like visual fit gets better as it approaches -240/239, but this isnt a clear rule. Plan is to simulate more and see if I can draw any insites from the data paterns with the visual fit, may need to work in some kind of best fit measurement such as $R^2$. Ideally need to talk to vincent to see if there is a mathamatical rational behind my observations which I cannot yet grasp. Data backed up today to github.
