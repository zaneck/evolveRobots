import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, "..")

from fun import *

for f in range(0,6):
    print(setOfFun[f])
    x = np.arange(-1, 1.1, 0.1)
    y = setOfFun[f](x)
    plt.plot(x,y)
    plt.show()
