#!/bin/bash

rm profile_data.pyprof out.dot profile_data.pyprof.log

python3 -m cProfile  -o profile_data.pyprof $1
pyprof2calltree -i profile_data.pyprof

gprof2dot --format=callgrind --output=out.dot profile_data.pyprof.log
dot -Tsvg out.dot -o graph.svg
