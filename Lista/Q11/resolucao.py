# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#regras de simpson e do trapezio 
def simp13(h, f0, f1, f2):
    return h*(f0 + 4*f1 + f2)/3

def simp38(h, f0, f1, f2, f3):
    return 3*h*(f0+3*(f1+f2)+f3)/8

#regra do trapezio para dados desigualmente espacados
def trapezio(x, y, n):
    sum_ = []
    for i in range(1, n):
        sum_.append((x[i] - x[i-1])*(y[i-1] + y[i])/2)
    return sum_


def main():
    #dados do problema 24.31
    tempo = [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.12, 0.18, 0.28, 0.4]
    tensao = [0,   18,   29,   44,   49,   46,   35,   26,   15,  7]

    #aqui podemos achar as areas nos segmentos da curva
    areas = trapezio(tempo, tensao, 10)

    integralV = sum(areas)
    #print(integralV)

    #entao a indutancia será integralV/I , sendo I = 2A
    L = integralV/2
    print(L)

    
if __name__ == "__main__":
    main()