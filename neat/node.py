import random

from fun import *

class Node():
    idNodeCpt = 0

    def __init__(self, inout=None):
        self.idNode = Node.idNodeCpt
        Node.idNodeCpt += 1

        if inout == None:
            self.fun = randomFun()
            self.nodeType = "hidden"
        elif inout == "in":
            self.fun = identity
            self.nodeType = "in"
        else:
            self.fun = identity
            self.nodeType = "out"

        Nodes.addNode(self)

    def nodeOutVal(self, inputVal):
        return self.fun(inputVal)

    def printNode(self):
        print("id {0} fun {1}".format(self.idNode, self.fun))

class Nodes():
    nodes = []
    numberOfNodes = 0

    def addNode(n):
        Nodes.nodes.append(n)
        Nodes.numberOfNodes +=1

    def getNode(idNode):
        return Nodes.nodes[idNode]
