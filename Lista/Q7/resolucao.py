# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from gaussElimin import gaussElimin

#least square
def LSA(x, y):
    
    sum_x2 = sum(x*x)
    sum_y2 = sum(y*y)
    sum_xy = sum(x*y)
    sum_x2y = sum(x*(y*x))
    sum_y2x = sum((y*y)*x)
    
    matrizA = np.array([[sum_x2, -sum_xy],[sum_xy, -sum_y2]])
    matrizB = np.array([[sum_x2y], [sum_y2x]])

    return gaussElimin(matrizA, matrizB)


def main():
    conc = np.array([0.197, 0.139, 0.068, 0.0427, 0.027, 0.015, 0.009, 0.008])
    velocidade = np.array([21.5, 21, 19, 16.5, 14.5, 11, 8.5, 7])

    coef = LSA(conc,velocidade)

    a = coef[0]
    b = coef[1]

    def F(a,b,x):
        return a*x/(b+x)

    v_calc = F(a,b,conc)

    print("Aqui esta o valor da velocidade experimental:\n")
    print(velocidade)
    print("Aqui esta o valor da velocidade calculada:\n")
    print(v_calc)


    ax1 = plt.plot(conc, v_calc, 'o-')

    ax2 = plt.plot(conc, velocidade, '--')

    plt.legend(["calculado","experimental"])
    plt.title("Valores de velocidade na equação de Michaelis-Menten")
    plt.xlabel("concentration")
    plt.ylabel("velocity")

    plt.show()


if __name__ == "__main__":
    main()

