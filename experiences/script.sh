#!/bin/bash

set -e

export PATH=/home/zaneck/defrost/sofa/build/bin/:$PATH
export PATH=/home/zaneck/Project/evolveRobots/:$PATH

# # rm -r arch arch.txt
# # mkdir arch

# echo "arch 1/5"
# for ((i=5 ; 10 - $i ; i+=1))do
#     mainSofa.py --config arch.json --scene sofaSceneArch/scene.json >> arch.txt
#     mv BESTtopo.py arch/topo-$i.py
# done

# # rm -r archSparse archSparse.txt
# # mkdir archSparse

# echo "arch sparse 2/5"
# for ((i=5 ; 10 - $i ; i+=1))do
#     mainSofa.py --config archSparse.json --scene sofaSceneArch/scene.json >> archSparse.txt
#     mv BESTtopo.py archSparse/topo-$i.py
# done

# # rm -r highBridge highBridge.txt
# # mkdir highBridge

# echo "high bridge 3/5"
# for ((i=5 ; 10 - $i ; i+=1))do
#     mainSofa.py --config highBridge.json --scene sofaSceneArch/scene.json >> highBridge.txt
#     mv BESTtopo.py highBridge/topo-$i.py
# done

# # rm -r lowBridge lowBridge.txt
# # mkdir lowBridge

# echo "low bridge 4/5"
# for ((i=5 ; 10 - $i ; i+=1))do
#     mainSofa.py --config lowBridge.json --scene sofaSceneArch/scene.json >> lowBridge.txt
#     mv BESTtopo.py lowBridge/topo-$i.py
# done

rm -r pincer pincer.txt
mkdir pincer
    

for ((i=0 ; 10 - $i ; i+=1))do
    echo $i
    mainSofa.py --config pincer.json --scene sofaSceneArch/scene.json >> pincer.txt
    mv BESTtopo.py pincer/topo-$i.py
done
