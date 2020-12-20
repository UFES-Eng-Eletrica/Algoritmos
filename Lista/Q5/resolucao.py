# -*- coding: utf-8 -*-
import numpy as np
from scipy import linalg
from gaussPivot import gaussPivot


def main():
    A = np.array([[-0.6210, 0.0956, -0.0445, 0.8747],[0.4328, -0.0624, 8.8101, -1.0393],[-0.0004, -0.0621, 5.3852, -0.3897],[3.6066, 0.6536, 0.8460, -0.2000]])


    b = np.array([[5.3814],[-1.0393],[-0.3897],[-0.0005]])


    print("Solução exata usando scipy:\n")
    print(linalg.solve(A,b))   
    print('\n')

    print("Solução A-1 * b:\n")
    print(np.linalg.inv(A).dot(b))
    print('\n')

    print("Com a solução do pivoteamento - algoritmo kiusalaas: \n")
    print(gaussPivot(A,b))
    print('\n')


if __name__ == "__main__":
    main()