#!/bin/bash

echo "arch"
for ((i=0 ; 10 - $i ; i+=1))do
    ../mainSofa.py --config arch.json >> arch.txt
    mv BESTtopo.py arch/topo-$i.py
done

echo "shortBridge"
for ((i=0 ; 10 - $i ; i+=1))do
    ../mainSofa.py --config shortBridge.json >>shortBridge.txt
    mv BESTtopo.py shortBridge/topo-$i.py
done

echo "squareBeam"
for ((i=0 ; 10 - $i ; i+=1))do
    ../mainSofa.py --config squareBeam.json >>squareBeam.txt
    mv BESTtopo.py squareBeam/topo-$i.py
done

echo "wheel"
for ((i=0 ; 10 - $i ; i+=1))do
    ../mainSofa.py --config wheel.json >> wheel.txt
    mv BESTtopo.py wheel/topo-$i.py
done
