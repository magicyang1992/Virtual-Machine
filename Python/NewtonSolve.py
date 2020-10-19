import math
import numpy as np
from numpy import *
from scipy.special import gamma
import matplotlib.pyplot as plt

def Fun(x,num):
    T = 100                                 # lattice temperature
    miu = 1                                 # chem poten
    e = 1                                   # unit
    kB = 1                                  # Boltzmann const
    DA = 1                                  # strain potential
    hbar = 1                                # hbar
    vF = 100000                             # Fermi velocity
    E = 100                                 # field
    i = num
    f = np.zeros((i),dtype=float)
    f[0] = - e * E * ((kB * x[0]) ** 3) / (2 * (pi ** 2)*(hbar ** 3)*(vF ** 3)) * gamma(3) * exp(miu/(kB * x[0])) \
           - 5 * (DA ** 2)* kB * T *((kB * x[0])** 4) * x[1] / (6 * (pi ** 3)*(hbar ** 7)*(vF ** 8)) * gamma(5) * exp(miu/(kB * x[0]))
    f[1] = - 2 * e * E * x[1] * ((kB * x[0]) ** 2) / (3 * (pi ** 2) * (hbar ** 2) * vF) * gamma(2) * exp(miu/(kB * x[0])) \
            - 6 * (DA ** 2) * kB * T *((kB * x[0])** 6) / ((pi ** 3)*(hbar ** 9)*(vF ** 8))*(1 - T / x[0]) * gamma(6) * exp(miu/(kB * x[0]))
    return f

def dfun(x,num):                        
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001                           
    x1 = np.copy(x)
    for i in range(0,num):              
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx           
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx
    df_1 = np.linalg.inv(df)                              
    return df_1

def Newton(x,num):
    x1 = np.copy(x)
    i = 0
    delta = np.copy(x)

    while(np.sum(abs(delta)) > 1.e-8 and i < 20):  
        x1 = x-dot(dfun(x,num),Fun(x,num)) 
        delta = x1-x                     
        x = x1
        i = i+1
        print(x)
    return x

num = 2             
x = np.ones((num),dtype=float)
a = Newton(x,num)
print(a)