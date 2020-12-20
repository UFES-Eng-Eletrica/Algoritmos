import numpy as np
def gaussElimin(a,b):
    n = len(b)
    # eliminacao
    for j in range(0,n-1):
        for i in range(j+1,n):
            if a[i,j] != 0.0:
                lambda_ = a[i,j]/a[j,j]
                a[i,j+1:n] = a[i,j+1:n] - lambda_*a[j,j+1:n]
                b[i] = b[i] - lambda_*b[j]

    # Substituicao
    for j in range(n-1,-1,-1):
        b[j] = (b[j] - np.dot(a[j,j+1:n],b[j+1:n]))/a[j,j]
    return b