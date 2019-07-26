#!/usr/bin/env python3
"""Data analysis for MMEE 2019 Conference poster."""
__appname__  = "analysis.py"
__author__   = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__  = "0.0.2"
__date__     = "07-2019"

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import gamma
from scipy.special import gammainc
from scipy.special import erf
from scipy.optimize import minimize

## functions ##
def aic_eq(ll, params):
    """Calculates AIC of given likelihood and pweights. 0 pweights also means
    the rate value has an effective value of 0.
    
    Arguments:
        ll {float} -- negative log-likelihood value.
        pweights {array[float]} -- the pweight paramter values.
    
    Returns:
        [float] -- AIC value.
    """
    k = len(params)
    return -2 * ll + 2 * k

def inverse_cdf(data):
    """Produce the inverse CDF of 1-d data provided.
    
    Arguments:
        data {1D numpy array} -- The data.
    
    Returns:
        pandas Dataframe -- The cdf of the data.
    """
    sorted_data = -np.sort(-data)
    prob = np.arange(0, len(data), 1) / len(data)
    return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

# minimizing functions
def exp_model(lamb, x):
    eq = lamb * np.exp(-lamb * x)
    ll = (-1) * np.sum(np.log(eq))
    return ll

def exp_eq(lamb, x):
    eq = 1-np.exp(-lamb * x)
    return 1-eq

def exp_gamma(params, x):
    shape, scale = params
    eq = (1/(gamma(shape) * scale**shape)) * x**(shape-1) * np.exp(-(x/scale))
    ll = (-1) * np.sum(np.log(eq))
    return ll

def gamma_eq(params, x):
    alpha, beta = params
    eq = gammainc(alpha, x / beta)
    return 1 - eq

def exp_halfnorm(sigma, x):
    eq = (np.sqrt(2)/(sigma * np.sqrt(np.pi))) * np.exp(-((x**2)/ (2 * sigma**2)))
    ll = (-1) * np.sum(np.log(eq))
    return ll

def halfnorm_eq(sigma, x):
    eq = erf(x/(sigma * np.sqrt(2)))
    return 1 - eq

def exp_lognorm(params, x):
    mu, sigma = params
    #eq = (1/(x * sigma * np.sqrt(2 * np.pi))) * np.exp(-((np.log(x - mu)**2) / (2 * sigma**2)))

    eq = (1/(x * sigma * np.sqrt(2 * np.pi))) * np.exp(-((np.log(x) - mu)**2/(2 * sigma**2)))
    ll = (-1) * np.sum(np.log(eq))
    return ll

def lognorm_eq(params, x):
    mu, sigma = params
    eq = ((1 / 2) + (1 / 2) * erf((np.log(x) - mu) / 
              np.sqrt(2 * sigma)))
    return 1 - eq

# plotting functions
def density_plots():
    # create density plots of pdf
    fig, axes = plt.subplots(1, 2)
    plot_dict = {"Rural" : rural_dist,
                "Urban" : urban_dist}
    dict_size = len(list(plot_dict.keys()))
    for i in range(dict_size):
        sns.distplot(list(plot_dict.values())[i],
                    hist=False,
                    kde=True,
                    ax=axes[i],
                    rug=True,
                    axlabel="Foraging distance (km)")
        axes[i].title.set_text(list(plot_dict.keys())[i])

    # save plot
    plt.savefig("../Results/Density_plot_pdf.svg", transparent=True)

    # create density plot of cdf
    rural_cdf = inverse_cdf(rural_dist)
    urban_cdf = inverse_cdf(urban_dist)
    fig, axis = plt.subplots(1, 2, clear=True, sharey=True)
    plot_dict = {"Rural" : rural_cdf,
                "Urban" : urban_cdf}
    dict_size = len(list(plot_dict.keys()))
    for i in range(dict_size):
        data = list(plot_dict.values())[i]
        axis[i].plot(data["SortedData"], data["Probability"])
        axis[i].set_xlabel("Foraging distance (km)")
        if i < 1:
            axis[i].set_ylabel("Probability")
        axis[i].title.set_text(list(plot_dict.keys())[i])

    # save plot
    plt.savefig("../Results/Density_plot_cdf.svg", transparent=True)

    return 0

def predict(data, prest, fun):
    ivdata = inverse_cdf(data)
    lengths = np.linspace(max(data),
                          min(data),
                          num = len(data))
    prediction = fun(prest, lengths)
    #prediction = inverse_cdf(prediction)
    df = pd.DataFrame({"SortedData"  : ivdata["SortedData"],
                       "Probability" : ivdata["Probability"],
                       "Lengths"     : lengths,
                       "Prediction"  : prediction})
    return df

def predict_fig(data, prest, fun, method, ll, aic):
    df = predict(data, prest, fun)
    plt.figure()
    plt.figure(figsize=cm2inch(15, 20))
    l1 = plt.plot(df["SortedData"],
                  df["Probability"],
                  label = "Distance",
                  linewidth=4)
    l2 = plt.plot(df["Lengths"],
                  df["Prediction"],
                  label = method,
                  linewidth=4)
    plt.legend(handles = [l1[0], l2[0]], prop={"size" : 18, "weight":"bold"})
    plt.xlabel("", fontsize='large', fontweight='bold')
    plt.ylabel("", fontsize='medium', fontweight='bold')
    plt.annotate("MLE = {}\nAIC = {}".format(ll, aic), (2, 0.75), weight="bold", size=18)
    return plt

# miniimize function
def model_minimize(data, startest, fun):
    kwargs = {"method" : "l-bfgs-b"}
    args = (fun, startest, data)
    model = minimize(*args, **kwargs)
    return model

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

import matplotlib
# set plotting style
plt.style.use('seaborn-poster')
plt.rcParams.update({'font.size': 42})

# load data into pandas
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# storage dictionary for results and models
all_models = {}

# Exponential
startest = [1.1]
model = model_minimize(rural_dist, startest, exp_model)
ll = -model.fun
ll = int(np.around(ll, decimals=0))
aic = aic_eq(ll, model.x)
aic = int(np.around(aic, decimals=0))
all_models["Exponential"] = model
plot = predict_fig(rural_dist, model.x, exp_eq, "Exponential", ll, aic)

plt.savefig("../Results/Exponential_rural.svg", transparent=True)

# Gamma
startest = [1.1, 1.1]
model = model_minimize(rural_dist, startest, exp_gamma)
ll = -model.fun
ll = int(np.around(ll, decimals=0))
aic = aic_eq(ll, model.x)
aic = int(np.around(aic, decimals=0))
all_models["Gamma"] = model
plot = predict_fig(rural_dist, model.x, gamma_eq, "Gamma", ll, aic)

plt.savefig("../Results/Gamma_rural.svg", transparent=True)

# Lognormal
startest = [1.1, 1.1]
model = model_minimize(rural_dist, startest, exp_lognorm)
ll = -model.fun
ll = int(np.around(ll, decimals=0))
aic = aic_eq(ll, model.x)
aic = int(np.around(aic, decimals=0))
all_models["Lognormal"] = model
plot = predict_fig(rural_dist, model.x, lognorm_eq, "Lognormal", ll, aic)

plt.savefig("../Results/Lognormal_rural.svg", transparent=True)

# Half-normal
startest = [1.1]
model = model_minimize(rural_dist, startest, exp_halfnorm)
ll = -model.fun
ll = int(np.around(ll, decimals=0))
aic = aic_eq(ll, model.x)
aic = int(np.around(aic, decimals=0))
all_models["Half-normal"] = model
plot = predict_fig(rural_dist, model.x, halfnorm_eq, "Half-normal", ll, aic)

plt.savefig("../Results/Halfnormal_rural.svg", transparent=True)

# show table of mle

model_names = list(all_models.keys())
df = pd.DataFrame({"Model" : model_names,
                   "MLE"   : [0] * len(model_names),
                   "AIC"   : [0] * len(model_names)})

for key in range(len(model_names)):
    mle = -all_models[model_names[key]].fun
    params = all_models[model_names[key]].x
    aic = aic_eq(mle, params)
    df.iloc[key, 1] = mle
    df.iloc[key, 2] = aic
    

sorted_df = df.sort_values("AIC")
latex_df = sorted_df.to_latex(index = False)
print(latex_df)

#plt.show()
