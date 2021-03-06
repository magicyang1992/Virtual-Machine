# solve the electron temp, chemical potential and fermi velocity of acoustic phonon
# Author:  Magic Yang
# Version: 0.1
# Date:    2020.09.09  

from scipy.optimize import fsolve,root
import numpy as np
from math import sin,cos,pi,exp
from matplotlib import pyplot as plt
import scipy.special
import copy
from scipy import integrate
from scipy.special import gamma

"""
print(scipy.special.gamma(1))
print(scipy.special.gamma(2))
print(scipy.special.gamma(3))
print(scipy.special.gamma(4))
print(scipy.special.gamma(5))
print(scipy.special.gamma(6))


def f(x):
    d = 140
    l = 156
    a = float(x[0])
    r = float(x[1])
    return [cos(a) - 1 + (d * d) / (2 * r * r), l - r * a]

result = fsolve(f, [1, 1])

print(result)

"""
N_Points = 1000

T_E_Vals = np.zeros((2, N_Points))            # save the values of electron temperature 
E_Vals = np.linspace(-100, 100, num = N_Points)

#print(E_Vals)

'''
test = np.linspace(2, 6, num = 100)
plt.plot(E_Vals, test)
plt.show()
'''

T_E_Vals[[0],:] = E_Vals

#print(T_E_Vals)

T = 100                                 # lattice temperature
miu = 1                                 # chem poten
e = 1                                   # unit
# kB = 1.38 * (10 ** (-23))                                  # Boltzmann const
kB = 1
DA = 1                                  # strain potential
# hbar = 6.626 * (10 ** (-34)) / (2 * pi)                                # hbar
hbar = 1
vF = 100000                             # Fermi velocity
vs = 5000                               # Material acoustic velocity
#upper_limit = 500

'''
Fermi Integration
'''

'''
def f1(x):
    return x / (np.exp(x - (miu / (kB * Tk)))+1)
v1, err1 = integrate.quad(f1, 0, upper_limit)
print(v1)

def f2(x):
    return (x ** 2) / (np.exp(x - (miu / (kB * Tk)))+1)
v2, err2 = integrate.quad(f2, 0, upper_limit)
print(v2)

def f3(x):
    return (x ** 3) / (np.exp(x - (miu / (kB * Tk)))+1)
v3, err3 = integrate.quad(f3, 0, upper_limit)
print(v3)

def f4(x):
    return (x ** 4) / (np.exp(x - (miu / (kB * Tk)))+1)
v4, err4 = integrate.quad(f4, 0, upper_limit)
print(v4)

def f5(x):
    return (x ** 5) / (np.exp(x - (miu / (kB * Tk)))+1)
v5, err5 = integrate.quad(f5, 0, upper_limit)
print(v5)
'''

for i in range(1, N_Points):
#   print(i)
    def f(x):      
        E =  E_Vals[i-1]                   # field
        Tk = float(x[0])                   # electron temperature
        k = float(x[1])                    # momentum
        
        #Fp(miu/kBTk)=Gamma(p+1)exp(miu/kBTk)
        
        # momentum balance equation
        Mon_Bal = - e * E * ((kB * Tk) ** 3) / (2 * (pi ** 2)*(hbar ** 3)*(vF ** 3)) * gamma(3) * exp(miu/(kB * Tk)) \
           - 5 * (DA ** 2)* kB * T *((kB * Tk)** 4) * k / (6 * (pi ** 3)*(hbar ** 6) * (vs ** 2) * (vF ** 6)) * gamma(5) * exp(miu/(kB * Tk))
        
        # energy balance equation
        Ene_Bal = - 2 * e * E * k * ((kB * Tk) ** 2) / (3 * (pi ** 2) * (hbar ** 2) * vF) * gamma(2) * exp(miu/(kB * Tk)) \
            - 6 * (DA ** 2) * kB * T *((kB * Tk)** 6) / ((pi ** 3)*(hbar ** 9)*(vF ** 8))*(1 - T / Tk) * gamma(6) * exp(miu/(kB * Tk))
        
        return [Mon_Bal, Ene_Bal]
    result = fsolve(f, [100, 1], maxfev=5000)
    T_E_Vals[[1], [i - 1]] = result[0] / T
#   print(result)
#print(T_E_Vals[[1],:])

# arrays for plot
px = np.zeros(N_Points)
py = np.zeros(N_Points)

for i in range(1, N_Points):
    px[i-1]=T_E_Vals[[0],[i-1]]
    py[i-1]=T_E_Vals[[1],[i-1]]

plt.clf()
plt.plot(px[0:N_Points-1], py[0:N_Points-1], ls="-", lw=1, label="Tk/T versus E")
plt.xlabel('E')
plt.ylabel('Tk/T')
plt.title('Tk/T versus E')
plt.legend()
plt.savefig('test.png')
plt.show()

