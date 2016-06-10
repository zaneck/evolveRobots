#!/bin/bash

rm cheetah-Html/html-site -r
mkdir -p cheetah-Html/html-site/images/Reference

python genImageReference.py

cd cheetah-Html
python2 cheetah.py
