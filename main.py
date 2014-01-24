import scipy.optimize as so
import numpy as np
import matplotlib.pyplot as plt

#Try to see if we can
try:
    import matplotlib.pyplot as plt
    can_plot = True
except(Exception):
    can_plot = False
    print("Cannot import matplotlib")

from functions import *
from util import getDataFromFile, exportResults

################################################################################
# OPTIONS AND PARAMETERS
################################################################################

# Add your function in functions.py, then put the names here of all the ones
# you want to fit to your data. You can have as many as you want.
fitting_functions = [
    stepFunction,
    hingeFunction
    ]

# Put the name of your data file here
data_file = "data.csv"

# Name of the file for the export
results_file = "results.txt"

# Number of points to try and put the "inflexion" point of the fitting function.
num_X0 = 100

# Choose wheter you want to plot the data + fitted functions
plot_results = True

################################################################################
# DATA EXTRACTION
################################################################################

# We get the data from a csv file
# The code is in util.py
d = getDataFromFile(data_file)

################################################################################
# DATA STRUCTURES
################################################################################

# The array with the x coordinates for the data point (1,2,...,20)
x = np.arange(1,21)

# Will contain the value of the fitted function at the data coordinates
y = np.zeros(x.shape)

# Will contain the norm of the error of each fitted function
fitting_scores = np.zeros([d.shape[0],len(fitting_functions)])

# Will contain the optimal parameters for each fitted function, for each
# data set. First indice is for dataset, second for function.
popts_total = []

# Coordinates at which to try to place the "inflexion" point of the fitting
# functions
X0 = np.linspace(1.0,20.0,num_X0)

# Vectorise the fitting functions
# It's technical, it lets you define the function for a single point, and
# numpy transforms it to accept vectors.
fitting_functions_names = []
for index,f in enumerate(fitting_functions):
    fitting_functions_names.append(f.__name__)
    fitting_functions[index] = np.vectorize(f)

################################################################################
# FUNCTION FITTING
################################################################################

# We loop on all the datasets
for dataset in range(d.shape[0]):

    popts = []

    # Start the final plot
    if (plot_results and can_plot):
        plt.plot(x,d[dataset][:],'o')

    for index,f in enumerate(fitting_functions):
        fitting_scores[dataset][index] = 1e12
        popts.append([])

        for x0 in X0:
            # Optimise the fitting of the curve
            (popt, pcov) = so.curve_fit(f, x, d[dataset][:], [x0,-1.0,1.0])
            y = f(x, *popt)
            
            # Compute the norm of the error, if better than previous best, keep it.
            norm = np.linalg.norm(y-d[dataset][:], 2)
            if norm < fitting_scores[dataset][index]:
                fitting_scores[dataset][index] = norm
                popts[index] = popt
       
        # Compute the function for the final solution for display
        if (plot_results and can_plot):
            y = f(X0,*(popts[index]))
            plt.plot(X0,y)

    popts_total.append(popts)

    # Finally show the whole plot
    if (plot_results and can_plot):
        plt.show(block=False)

################################################################################
# RESULTS EXPORT
################################################################################

options = {"Data file" : data_file, 
           "Number of tests" : num_X0
          }

exportResults(results_file, options, fitting_functions_names, fitting_functions,
              fitting_scores, popts_total)

