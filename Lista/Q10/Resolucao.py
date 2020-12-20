# -*- coding: utf-8 -*-
'''
Questão 20.56 do Chapre: 

As temperaturas são medidas em diversos pontos de uma
placa aquecida (Tabela P20.56). Faça uma estimativa da temperatura 
em (a) x = 4, y = 3,2 e (b) x = 4,3, y = 2,7.


Utilizando regressão linear multipla:

nesse caso-> T(temperatura) = a0 + a1*x + a2*y, onde x e y são posições na placa
e a0 a1 a2 são coeficientes 

'''
import numpy as np
import matplotlib.pyplot as plt
from gaussElimin import gaussElimin

def multi_regress(x, y, T):
    
    sum_y = sum(y)
    sum_x = sum(x)
    sum_T = sum(T)
    sum_x_2 = sum(x**2)
    sum_y_2 = sum(y**2)
    sum_xy = sum(x*y)
    sum_xT = sum(x*T)
    sum_yT = sum(y*T)

    return sum_y, sum_x, sum_T, sum_x_2, sum_y_2, sum_xy, sum_xT, sum_yT

def pontos_placa(c1, c2, c3, x, y):
    return c1 + x*c2 + y*c3


def main():
    #vetores das features
    x = np.array([0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8])
    y = np.array([0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8])

    #label
    T = np.array([100, 85, 70, 55, 40, 90, 64.49, 48.90, 38.78, 35, 80, 53.50, 38.43, 30.39, 30, 70, 48.15, 35.03, 27.07, 25, 60, 50, 40, 30, 20])
    
    sum_y, sum_x, sum_T, sum_x_2, sum_y_2, sum_xy, sum_xT, sum_yT = multi_regress(x,y,T)

    #preparando as matrizes para a eliminacao de gauss
    A = np.array([[25, sum_x, sum_y],
                 [sum_x, sum_x_2, sum_xy],
                 [sum_y, sum_xy, sum_y_2]])
    B = np.array([[sum_T],
                  [sum_xT],
                  [sum_yT]])
    #matriz coef recebe o retorno da eliminicao de gauss
    coef = gaussElimin(A, B)

    #vendo a temperatura nos pontos especificados
    Temp_a = pontos_placa(float(coef[0]), float(coef[1]), float(coef[2]), 4, 3.2)
    Temp_b = pontos_placa(float(coef[0]), float(coef[1]), float(coef[2]), 4.3, 2.7)
    #print(x*x)
    


if __name__ == "__main__":
    main()

