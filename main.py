import scipy.optimize as so
import numpy as np
import matplotlib.pyplot as plt


def stepFunction(x, x0, f0, f1):
    if x > x0:
        return f1
    else:
        return f0

stepFunction_vec = np.vectorize(stepFunction)

def stepFunction_vec_self(x, x0, f0, f1):
    y = np.zeros(x.shape)
    for i in range(len(y)):
        y[i] = stepFunction(x[i], x0, f0, f1)
    return y


def hingeFunction(x, x0, f0, m):
    if x > x0:
        return f0+m*(x-x0)
    else:
        return f0

hingeFunction_vec = np.vectorize(hingeFunction)

def hingeFunction_vec_self(x, x0, f0, m):
    y = np.zeros(x.shape)
    for i in range(len(y)):
        y[i] = hingeFunction(x[i], x0, f0, m)
    return y




data = open("data.csv")
x = np.arange(1,21)

d = data.readline() 
d = str.split(d,",")
for index,number in enumerate(d):
    d[index] = float(number)
d = np.array(d)

y = np.zeros(x.shape)
y2 = np.zeros(x.shape)

min_x0 = 0.0
min_norm = 1e12

min_x02 = 0.0
min_norm2 = 1e12

num_x0 = 21

for X0 in range(0,num_x0):
    x0 = X0*20.0/num_x0
    (popt, pcov) = so.curve_fit(stepFunction_vec_self, x, d, [x0,-1.0,1.0])
    (popt2, pcov2) = so.curve_fit(hingeFunction_vec_self, x, d, [x0,-1.0,0.0])
    y = stepFunction_vec_self(x, *popt)
    y2 = hingeFunction_vec_self(x, *popt2)

    norm = np.linalg.norm(y-d, 2)
    if norm < min_norm:
        min_x0 = x0
        min_norm = norm
        #print min_norm
    norm2 = np.linalg.norm(y2-d, 2)
    if norm2 < min_norm2:
        min_x02 = x0
        min_norm2 = norm2
        print min_norm2

(popt, pcov) = so.curve_fit(stepFunction_vec_self, x, d, [min_x0,-1.0,1.0])
y = stepFunction_vec_self(x, *popt)

(popt2, pcov2) = so.curve_fit(hingeFunction_vec_self, x, d, [min_x02,-1.0,1.0])
y2 = hingeFunction_vec_self(x, *popt2)

print popt2

plt.plot(x,d,'o')
plt.plot(x,y)
plt.plot(x,d,'or')
plt.plot(x,y2, 'r')
plt.show()