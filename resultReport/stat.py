#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os, sys

a=(np.loadtxt(sys.argv[1]))
nbOp=0
ma=0

print("{0} {2} & {1} & {3} & {4} & {5}".format(sys.argv[1], np.mean(a), np.std(a), np.median(a), np.min(a), np.max(a)))
