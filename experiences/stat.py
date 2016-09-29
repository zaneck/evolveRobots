#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os, sys

a=(np.loadtxt(sys.argv[1]))

print("{0} & {2} & {1} & {3} & {4} & {5}".format(sys.argv[1], round(np.mean(a), 3), round(np.std(a),3), round(np.median(a),3), round(np.min(a),3), round(np.max(a),3)))
