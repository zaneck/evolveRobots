import numpy as np
import random

def gauss(x):
    return np.exp(-np.power(x, 2))

def sigmoid(x):
    try:
        return 1/(1+np.exp(-7 * x))
    except OverflowError:
        if x > 0:
            return 1
        else:
            return 0

def identity(x):
    return x

def abs_root(x):
    return np.sqrt(abs(x))


setOfFun = {
    0: np.sin,
    1: np.cos,
    2: gauss,
    3: sigmoid,
    4: np.square,
    5: abs_root,
    6: identity,
}
    

def randomFun():
    # setOfFun = {
    #     0: np.sin,
    #     1: np.cos,
    #     2: Function.gauss,
    #     3: Function.sigmoid,
    #     4: np.square,
    #     5: Function.abs_root,
    #     6: Function.identity,
    # }
    
    return setOfFun[random.randint(0,6)]

