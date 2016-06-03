import sys

sys.path.insert(0,"..")

from network import *
from node import *
from edge import *
from fun import *
from population import *

print("Create two Network")
inputNode = [Node(inout="in"), Node(inout="in")]
outputNode = [Node(inout="out")]

net1 = Network(inputNode, outputNode) 
net2 = Network(inputNode, outputNode) 

net1.linkInputOutput()
net2.linkInputOutput()

net1.fitness = 0
net2.fitness = 1

net1.printNetwork()
print("\n")
net2.printNetwork()


print("create population")
p = Population(popMax=1, popAugmentation=2)
print(p.__dict__)

print("add To net")
print(net1)
print(net2)
p.addNetwork(net1)
p.addNetwork(net2)
print(p.__dict__)
print("\n")
p.reducePopulation()
print(p.__dict__)

print(p.numberOfAugmentation())
