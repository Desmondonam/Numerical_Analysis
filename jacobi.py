import math
import numpy as np
def JacobiIteration(n):
    u1 = np.zeros(n)
    u2 = np.zeros(n)
    u3 = np.zeros(n)
    u4 = np.zeros(n)
    u5 = np.zeros(n)
    u6 = np.zeros(n)

    for i in range(0,n-1):
        u1[i+1] = (u2[i] - 0.5*u6[i] + 2.5)/3
        u2[i+1] = ( u1[i] + u3[i] - 0.5*u5[i] + 1.5)/3
        u3[i+1] = (u2[i] + u4[i] + 1)/3
        u4[i+1] = (u3[i] + 0.5*u5[i] + 1)/3
        u5[i+1] = (u4[i] - 0.5*u2[i] +u6[i] + 1.5)/3
        u6[i+1] = (u5[i] - 0.5*u1[i] + 2.5)/3
    print ("Our u1 value is",u1[-1],
           "\nOur u2 value is",u2[-1],
           "\nOur u3 value is",u3[-1],
           "\nOur u4 value is",u4[-1],
           "\nOur u5 value is",u5[-1],
           "\nOur u6 value is",u6[-1])
JacobiIteration(100)