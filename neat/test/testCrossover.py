import sys

sys.path.insert(0,"..")

from network import *
from node import *
from edge import *
from fun import *



from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plotMe(n, m, o):

    fig = plt.figure()
    
    ax = fig.add_subplot(221, projection='3d')
    x = y = np.arange(-1.0, 1.0, 0.01)
    X, Y = np.meshgrid(x, y)
    zs = np.array([n.computeNetwork([x,y])[0] for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('input X')
    ax.set_ylabel('input Y')
    ax.set_zlabel('output Z')

    ax = fig.add_subplot(222, projection='3d')
    x = y = np.arange(-1.0, 1.0, 0.01)
    X, Y = np.meshgrid(x, y)
    zs = np.array([m.computeNetwork([x,y])[0] for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('input X')
    ax.set_ylabel('input Y')
    ax.set_zlabel('output Z')

    ax = fig.add_subplot(223, projection='3d')
    x = y = np.arange(-1.0, 1.0, 0.01)
    X, Y = np.meshgrid(x, y)
    zs = np.array([o.computeNetwork([x,y])[0] for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('input X')
    ax.set_ylabel('input Y')
    ax.set_zlabel('output Z')

    plt.show()
    plt.savefig('testCrossover.png')
    
print("Create two Network")
inputNode = [Node(inout="in"), Node(inout="in")]
outputNode = [Node(inout="out")]

net1 = Network(inputNode, outputNode) 
net2 = Network(inputNode, outputNode) 

net1.linkInputOutput()
net2.linkInputOutput()

net1.fitness = 0
net2.fitness = 1

net1.addNode(0,2)
net2.addNode(1,2)

net1.printNetwork()
print("\n")
net2.printNetwork()

net3 = net1.crossover(net2)

print("\n")
net3.printNetwork()

plotMe(net1, net2, net3)
