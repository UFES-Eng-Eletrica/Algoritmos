# -*- coding: utf-8 -*-
from scipy import linalg
import numpy as np
from gaussElimin import gaussElimin

#usei o modelo de eliminacao gaussiana
def HilbertMatrix(n):
    hilbert = linalg.hilbert(n)
    x = np.ones([n,1])
    b = hilbert.dot(x)

    x = gaussElimin(hilbert, b)

    return x

#exemplo
def main():
    x = HilbertMatrix(18)
    print(x)

if __name__ == "__main__":
    main()

