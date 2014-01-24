# (c) 2014 Bastien Gorissen
#
# Fitting functions
#
# Library of functions to be fitted to data

import numpy

################################################################################

def stepFunction(x, x0, f0, f1):
    """
    Parameters : [x0, f0, f1]
    x0 : discontinuity point
    f0 : value of the step for x <= x0
    f1 : value of the step for x > x0
    """
    if x > x0:
        return f1
    else:
        return f0

stepFunction_vec = numpy.vectorize(stepFunction)

################################################################################

def hingeFunction(x, x0, f0, m):
    """
    Parameters : [x0, f0, f1]
    x0 : inflexion point
    f0 : value of the constant part for x < x0
    m  : slope of the linear part for x >= x0
    """
    if x >= x0:
        return f0+m*(x-x0)
    else:
        return f0

hingeFunction_vec = numpy.vectorize(hingeFunction)

################################################################################

#
# Add new functions here!
#
