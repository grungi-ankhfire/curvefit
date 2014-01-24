# (c) 2014 Bastien Gorissen
#
# Fitting functions
#
# Library of functions to be fitted to data

import numpy

################################################################################

def stepFunction(x, x0, f0, f1):
    """
    Return the value of a step function at the coordinate x.

    @type  x: number
    @param x: The coordinate at which to evaluate the step function.
    @type  x0: number
    @param x0: The coordinate of the discontinuity point of the step function.
    @type  f0: number
    @param f0: Value of the step function at coordinates below or equal to x0
    @type  f1: number
    @param f1: Value of the step function at coordinates above x0
    @rtype:   number
    @return:  The value of the function at x.
    """
    if x > x0:
        return f1
    else:
        return f0

stepFunction_vec = numpy.vectorize(stepFunction)

################################################################################

def hingeFunction(x, x0, f0, m):
    """
    Return the value of a hinge function at the coordinate x.

    @type  x: number
    @param x: The coordinate at which to evaluate the hinge function.
    @type  x0: number
    @param x0: The coordinate of the transition point of the step function.
    @type  f0: number
    @param f0: Value of the constant part of the function 
               (at coordinates below or equal to x0).
    @type  m: number
    @param m: Slope of the linear part of the function (at coordinates above x0)
    @rtype:   number
    @return:  The value of the function at x.
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
