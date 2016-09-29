#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import math

for i in range(100):
        v = 1.0*i/100.0 - 0.5
        r = math.fmod(v, 0.1)
        p = v-r
        print("{0:.2f} -> {1:.2f} = {2:0.2f}".format(v,r, p))
