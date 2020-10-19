# solve the electron temp, chemical potential and fermi velocity of acoustic phonon
# Author:  Magic Yang
# Version: 0.2
# Date:    2020.09.17

from scipy.optimize import fsolve,root
import numpy as np
from math import sin,cos,pi,exp
from matplotlib import pyplot as plt
import scipy.special
import copy
from scipy import integrate
from scipy.special import gamma

T = 100                                 # lattice temperature
miu = 1                                 # chem poten
e = 1                                   # unit
kB = 1                                  # Boltzmann const
DA = 1                                  # strain potential
hbar = 1                                # hbar
vF = 1000                               # Fermi velocity

def f(x):      
        E =  100                           # field
        Tk = float(x[0])                   # electron temperature
        k = float(x[1])                    # momentum
        #Fp(miu/kBTk)=Gamma(p+1)exp(miu/kBTk)
        
        # momentum balance equation
        Mon_Bal = - e * E * ((kB * Tk) ** 3) / (2 * (pi ** 2)*(hbar ** 3)*(vF ** 3)) * gamma(3) * exp(miu/(kB * Tk)) \
           - 5 * (DA ** 2)* kB * T *((kB * Tk)** 4) * k / (6 * (pi ** 3)*(hbar ** 7)*(vF ** 8)) * gamma(5) * exp(miu/(kB * Tk))
        
        # energy balance equation
        Ene_Bal = - 2 * e * E * k * ((kB * Tk) ** 2) / (3 * (pi ** 2) * (hbar ** 2) * vF) * gamma(2) * exp(miu/(kB * Tk)) \
            - 6 * (DA ** 2) * kB * T *((kB * Tk)** 6) / ((pi ** 3)*(hbar ** 9)*(vF ** 8))*(1 - T / Tk) * gamma(6) * exp(miu/(kB * Tk))
        
        return [Mon_Bal, Ene_Bal]


result = fsolve(f, [100, 100], maxfev=5000)

print(result)