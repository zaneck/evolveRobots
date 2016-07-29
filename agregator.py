# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################

def maxAgregator(l):
    return max(l)

def minAgregator(l):
    return min(l)

def averageAgregator(l):
    res = 0.0

    for i in l:
        res += i

    return res / len(l)
