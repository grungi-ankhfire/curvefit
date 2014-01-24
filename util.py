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
