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

# Number of points to try and put the "inflexion" point of the fitting function.
num_X0 = 100

# Choose wheter you want to plot the data + fitted functions
plot_results = False

################################################################################
# DATA EXTRACTION
################################################################################

# We get the data from a csv file
data = open(data_file)
x = np.arange(1,21)

d = data.readline() 
d = str.split(d,",")
for index,number in enumerate(d):
    d[index] = float(number)
d = np.array(d)

data.close()

################################################################################
# DATA STRUCTURES
################################################################################

# Will contain the value of the fitted function at the data coordinates
y = np.zeros(x.shape)

# Will contain the norm of the error of each fitted function
fitting_scores = np.zeros(len(fitting_functions))

# Will contain the optimal parameters for each fitted function
popts = []

# Coordinates at which to try to place the "inflexion" point of the fitting
# functions
X0 = np.linspace(1.0,20.0,num_X0)

# Vectorise the fitting functions
# It's technical, it lets you define the function for a single point, and
# numpy transforms it to accept vectors.
for index,f in enumerate(fitting_functions):
    fitting_functions[index] = np.vectorize(f)

################################################################################
# FUNCTION FITTING
################################################################################

# Start the final plot
if (plot_results and can_plot):
    plt.plot(x,d,'o')

for index,f in enumerate(fitting_functions):
    fitting_scores[index] = 1e12
    popts.append([])

    for x0 in X0:
        # Optimise the fitting of the curve
        (popt, pcov) = so.curve_fit(f, x, d, [x0,-1.0,1.0])
        y = f(x, *popt)
        
        # Compute the norm of the error, if better than previous best, keep it.
        norm = np.linalg.norm(y-d, 2)
        if norm < fitting_scores[index]:
            fitting_scores[index] = norm
            popts[index] = popt

    # Compute the function for the final solution for display
    if (plot_results and can_plot):
        y = f(X0,*(popts[index]))
        plt.plot(X0,y)

# Finally show the whole plot
if (plot_results and can_plot):
    plt.show()