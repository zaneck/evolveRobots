import sys

sys.path.insert(0,"..")

from network import *
from node import *
from edge import *
from fun import *


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plotMe(n):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.arange(-1.0, 1.0, 0.01)
    X, Y = np.meshgrid(x, y)
    zs = np.array([n.computeNetwork([x,y])[0] for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('input X')
    ax.set_ylabel('input Y')
    ax.set_zlabel('output Z')

    plt.show()
    plt.savefig('testNetwork.png')


print("first Test: simple network")
inputNode = [Node(inout="in"), Node(inout="in")]
outputNode = [Node(inout="out")]

net = Network(inputNode, outputNode) 

net.linkInputOutput()

#net.edges[0].weight=0.1
#net.edges[1].weight=0.5

net.printNetwork()


a = net.computeNetwork([0.5,0.5])
b = net.computeNetwork([0.5,0.5])

print([a,b])

if a != b:
    print("KO\n\n")
else:
    print("OK\n\n")

print("Add Edge impossible")
test = net.addEdge(0,1)

if test != False:
    print("KO\n\n")
else:
    print("OK\n\n")


print("Add Node ok")

test = net.addNode(0,2)
#net.edges[3].weight=0.8
if test == False:
    print("KO\n\n")
else:
    print("OK\n\n")

print("compute test")
a = net.computeNetwork([0.5,0.5])
b = net.computeNetwork([0.5,0.5])

print([a,b])
if a != b:
    print("KO\n\n")
else:
    print("OK\n\n")

print("Add Node ok")

test = net.addNode(1,2)

if test == False:
    print("KO\n\n")
else:
    print("OK\n\n")

print("\n")
print(net.calculPath)
print(net.matrixAdj)
print("compute test")
a = net.computeNetwork([0.5,0.5])
b = net.computeNetwork([0.5,0.5])

print([a,b])
if a != b:
    print("KO\n\n")
else:
    print("OK\n\n")

print("Add Edge OK 1-3")
test = net.addEdge(1,3)

if test == True:
    print("OK\n\n")
else:
    print("KO\n\n")

a = net.computeNetwork([0.5,0.5])

print("Add Edge ok 0-4")
test = net.addEdge(0,4)

if test == True:
    print("OK\n\n")
else:
    print("KO\n\n")

print("\n")
net.printNetwork()
print("\n")

#CRITIks

# net.hiddenNodes[1].fun=gauss
# net.hiddenNodes[0].fun=gauss


#end

plotMe(net)
print("\n")
net.printNetwork()
print("\n")




# import numpy as np
# for i in np.arange(-1,1,0.1):
#     for j in np.arange(-1,1,0.1):
#         print("{0} {1} {2}".format(i,j,net.computeNetwork([i,j])[0]))
