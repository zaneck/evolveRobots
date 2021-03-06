import hashlib
import random

class Edge():
    idEdgeCpt = 0

    def __init__(self, begin, end, idEdge=None, weight=None, disable=None):
        self.begin = begin
        self.end = end

        if weight == None:
            self.weight = Edge.randomWeight()
        else:
            self.weight = weight

        if disable == None:
            self.disable = False
        else:
            self.disable = disable
            

        if idEdge == None:
            self.idEdge = Edge.idEdgeCpt
            Edge.idEdgeCpt += 1
            Edges.addEdge(self)
        else:
            self.idEdge = idEdge

    def randomWeight():
        return random.uniform(-2,2)

    def printEdge(self):
        print("id {0} begin {1} end {2} weight {3} disable {4}".format(self.idEdge, self.begin, self.end, self.weight, self.disable))

    
class Edges():
    edges = {} # key = hash(begin,end)
    numberOfEdges = 0

    def hashFun(begin, end):
        key = "{0},{1}".format(begin, end)
        
        md = hashlib.md5()
        md.update(key.encode())
        return md.digest()
    
    def addEdge(g):
        #gen key
        key = Edges.hashFun(g.begin, g.end)
        Edges.edges[key]=g
        Edges.numberOfEdges += 1

        
    def get(begin, end):
        key = Edges.hashFun(begin, end)
        try:
            return Edges.edges[key]
        except KeyError:
            return None
