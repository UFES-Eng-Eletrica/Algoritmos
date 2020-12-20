# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from gaussElimin import gaussElimin
import math

#alguns ajustes na equacao sao necessários uma vez que será melhor linearizar antes de passar pelo metodo polyfit.
def main():
    T = np.array([273.15, 278.15, 283.15, 293.15, 303.15, 313.15])
    mi = np.array([1.787, 1.519, 1.307, 1.002, 0.7975, 0.6529])

    coef = np.polyfit(1/T,np.log(mi),1)

    a = np.e**(coef[1])
    b = coef[0]

    def F(a,b,x):
        return a*np.e**(b/x)

    mi_calc = F(a,b,T)

    
    ax1 = plt.plot(T, mi_calc, '--')

    ax2 = plt.plot(T, mi, 'o')

    plt.legend(["calculado","experimental"])
    plt.xlabel("Temp(K)")
    plt.ylabel("viscosidade")

    plt.show()


if __name__ == "__main__":
    main()
