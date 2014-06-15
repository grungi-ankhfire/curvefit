import time
import numpy

def getDataFromFile(filename):
    """
    Return an array with data from a CSV file
    """

    data_array = numpy.loadtxt(open(filename,"rb"),delimiter=",",skiprows=1)
    
    output = numpy.ndarray(shape=(numpy.amax(data_array[:,0])+1,
                            numpy.amax(data_array[:,1])+1,
                            numpy.amax(data_array[:,2])+1,
                            numpy.amax(data_array[:,3])+1))

    for l in range(data_array.shape[0]):
        output[data_array[l, 0],data_array[l, 1],data_array[l, 2],data_array[l, 3]]=  data_array[l, 4]

    return output

def parseList(input_string):
    blocks = input_string.split(",")
    output = []
    for block in blocks:
        block = block.split("..")
        if len(block) > 1:
            output.extend(range(int(block[0]), int(block[1])+1))
            continue
        block = block[0].split("+")
        if len(block) > 1:
            output.append([int(x) for x in block])
            continue
        output.extend([int(block[0])])
    return output

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
