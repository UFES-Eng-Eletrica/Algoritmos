# -*- coding: utf-8 -*-
import numpy as np
import math
from scipy import linalg

def Newton_R(f, x, tol=1.0e-9):
    pass
    #funcao para achar o jacobiano calculando as derivadas parciais
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
        #retorno de uma matriz 3x3 nesse caso

    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol: return x
        dx = linalg.inv(jac).dot(-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0):
            return x
    


def main():
    def f(x):
        f = np.zeros(len(x))
        f[0] = 4*x[0]**2 + 2*x[1] - 4
        f[1] = x[0] + 2*x[1]**2 + 2*x[2] - 4
        f[2] = x[1] + 2*x[2]**2 - 4
        return f

    x = np.array([1.0, 1.0, 1.0])

    raizes = Newton_R(f, x)
    print(raizes)

if __name__ == "__main__":
    main()




    

