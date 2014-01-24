import time
import numpy

def getDataFromFile(filename):
    """
    Return an array with N rows and M columns.

    N is the number of datasets
    M is the number of data point in each set
    """

    data = open(filename)
    data_array = []
    for line in data:
        # Data points need to be separated by a comma
        d = str.split(line,",")

        # We transform the strings into floats
        for index,number in enumerate(d):
            d[index] = float(number)

        # We add the processed dataset in the Python array
        data_array.append(d)

    data.close()
        
    # Finally we transform the data in a numpy array
    data_array = numpy.array(data_array)

    return data_array

def exportResults(filename, options, func_names, fitting_functions,
                  fitting_scores, popts):
    """
    Export the curve fitting results into the file filename.

    Currently the norm of the error as well as the function parameters are
    exported.
    A summary of some options and a reference for the functions (built from the 
    functions docstrings are also written to file)
    """

    f = open(filename, 'w')
    f.write("Curve fitting results - " + time.strftime("%c") + "\n")
    f.write("\n")
    f.write("Options :\n")
    for key,value in options.iteritems():
        f.write(key + " : " + str(value) + "\n")
    f.write("\n")
    f.write("Function reference\n")
    for i,func in enumerate(fitting_functions):
        f.write(func_names[i] + "\n")
        f.write(func.__doc__)
        f.write("\n\n")
    for i,scores in enumerate(fitting_scores):
        f.write("Dataset #" + str(i) + "\n")
        for j in range(len(func_names)):
            f.write("Function " + str(func_names[j]) + "\n")
            f.write("    Parameters : " + str(popts[i][j]) + "\n")
            f.write("    Error : " + str(scores[j]) + "\n")
        f.write("\n")

    f.close()
