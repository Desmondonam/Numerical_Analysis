import math
import numpy as np
def JacobiIteration(n):
    x1 = np.zeros(n)
    x2 = np.zeros(n)
    x3 = np.zeros(n)
    
    for i in range(0,n-1):
        x1[i+1] = -x2[i] - 0.5*x3[i] + 3
        x2[i+1] = 0.5*x1[i] - 0.5*x3[i] + 1.5
        x3[i+1] = -0.5*x1[i] - x2[i] + 3.5
    print ("Our x1 value is",x1[-1],
           "\nOur x2 value is",x2[-1],
           "\nOur x3 value is",x3[-1])
JacobiIteration(60)