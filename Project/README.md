# MSc Computational Methods in Ecology and Evolution Project.
### Joseph Palmer: <joseph.palmer18@imperial.ac.uk>
### Update Date: 09/05/2019

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
* __NEW:__ can do 2 and 3 rate paramater sum of exponentials.
* __Edit:__ sum of exponentials set up with flexible equations. Log-likelihood equation coming too high so function needs a tweak, but on the right lines. Tomorrows plan is to discuss the equation with one of the maths phds to see where I am going wrong, discuss with francis getting the git version control set up properly, and if time putting the sum of exponentials into a seperate class from the other functions and cleaning up the code.

These are implimented and can be extended to any data provided if desired.

#### what the package will soon be able to do
Imediate targets for inclusion are:

* Testing frame work for sampling from any function.

plan is to use the inverse cdf method for this. A comprehensive testing method is not possible. One has to sample from a uniform distribution bound between 0,1 and pass these to the inverse of the cdf of the target distribution. Not possible to code fully but an example script in a jupyter notebook in __Notebooks/__ for exponential shows the method. This will need to be done manually for every other function you want to test from.


