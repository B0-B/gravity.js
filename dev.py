
import numpy as np

dx=-500
x0=1000
sq=np.sqrt(x0)

def f (x):
    return sq + 1/sq*(.5*(x-x0)-.25*(x-x0)**2/x0)

def d (x):
    return f(x)**2/x-1

def e (x):
    return abs(d(x))

print(f(x0+dx), np.sqrt(x0+dx), e(x0+dx))