from edge import *
from node import *

class Network():
    idNetwork = 0
    
    def __init__(self, inputNode, outputNode):
        self.idNetwork = Network.idNetwork
        Network.idNetwork += 1
        self.inputNodes = inputNode
        self.outputNodes = outputNode
        self.hiddenNodes = []

        self.edges = []
        self.nbActiveEdge = 0
        self.matrixAdj = None
        
        self.calculPath= None

        self.fitness = None
        self.fitnessAdjust = None
        self.behavior = None
        self.fitnessReal = None

    def copy(self):
        res = Network(self.inputNodes, self.outputNodes)

        #hidden
        for h in self.hiddenNodes:
            res.hiddenNodes.append(h)

        #edges
        for e in self.edges:
            res.edges.append(Edge(e.begin, e.end, idEdge=e.idEdge, weight=e.weight, disable=e.disable))
        res.nbActiveEdge = self.nbActiveEdge

        # res.matrixAdj = self.matrixAdj
        # res.calculPath = self.calculPath
        
        return res
        
    def linkInputOutput(self):
        for i in self.inputNodes:
            for o in self.outputNodes:

                test = Edges.get(i.idNode, o.idNode,)
                if test != None:
                    newEdge = Edge(i.idNode, o.idNode, test.idEdge)
                    self.edges.append(newEdge)
                    self.edges=sorted(self.edges, key= lambda x : x.idEdge)
                else:
                    e = Edge(i.idNode,o.idNode)
                    self.edges.append(e)
                    self.nbActiveEdge += 1


    def toAdj(self):
        if self.matrixAdj == None:
            matrix = {}

            for n in self.inputNodes:
                matrix[n.idNode]={}

            for n in self.outputNodes:
                matrix[n.idNode]={}

            for n in self.hiddenNodes:
                matrix[n.idNode]={}

            for e in self.edges:
                if e.disable == False:
                    matrix[e.begin][e.end] = e.weight
                else:
                    matrix[e.begin][e.end] = None
            self.matrixAdj = matrix

        return self.matrixAdj

    def printNetwork(self):
        print("inputNode")
        for n in self.inputNodes:
            n.printNode()

        print("outputNode")
        for n in self.outputNodes:
            n.printNode()

        print("hiddenNode")
        for n in self.hiddenNodes:
            n.printNode()

        print("Edges")
        for e in self.edges:
            e.printEdge()

        m = self.toAdj()
        for k in m.keys():
            print("{0} -> {1}".format(k, m[k]))


    def computeNetwork(self, inputVal):
        if self.calculPath != None:
            return self.calcul(inputVal)
            
        else:
            return self.calculHard(inputVal)

    def isCycleLess(self):
        matrix = self.toAdj()
        
        toDo = []
        done = []

        nodesToCheck = list(set(self.inputNodes) | set(self.hiddenNodes))

        for n in self.inputNodes:
            toDo.append(n)

        maxTries = 70
        tries = 0
        for t in toDo :
            if tries > maxTries:
                return False
            tries +=1
            flag = True
            for x in nodesToCheck:
                if t.idNode in matrix[x.idNode].keys() and x not in done:
                    flag = False
                    toDo.append(t)
                    break

            if flag == True:
                #sending
                for d in matrix[t.idNode].keys():
                    if matrix[t.idNode][d] != None:
                        if Nodes.getNode(d).nodeType != "out":
                            toDo.append(Nodes.getNode(d))

            done.append(t)
        return True
            
    def calcul(self, inputVal):
        matrix = self.toAdj()
        tmp = {}

        cptNode = 0
        for n in self.inputNodes:
            tmp[n.idNode] = inputVal[cptNode]
            cptNode += 1

        for n in self.outputNodes:
            tmp[n.idNode] = 0

        for n in self.hiddenNodes:
            tmp[n.idNode] = 0

        for t in self.calculPath:
            val = t.nodeOutVal(tmp[t.idNode])
                
            #sending
            for d in matrix[t.idNode].keys():
                if matrix[t.idNode][d] != None:
                    tmp[d] += val * matrix[t.idNode][d]

        result = []
        for n in self.outputNodes:
            result.append(tmp[n.idNode])

        return result

    def calculHard(self, inputVal):
        matrix = self.toAdj()

        tmp = {}
        toDo = []
        done = []

        nodesToCheck = list(set(self.inputNodes) | set(self.hiddenNodes))

        cptNode = 0
        for n in self.inputNodes:
            tmp[n.idNode] = inputVal[cptNode]
            cptNode += 1
            toDo.append(n)

        for o in self.outputNodes:
            tmp[o.idNode] = 0

        for h in self.hiddenNodes:
            tmp[h.idNode] = 0

        for t in toDo:
            flag = True
            for x in nodesToCheck:
                if t.idNode in matrix[x.idNode].keys() and x not in done:
                    flag = False
                    toDo.append(t)
                    break

            if flag == True:
                #compute val
                val = t.nodeOutVal(tmp[t.idNode])
                
                #sending
                for d in matrix[t.idNode].keys():
                    if matrix[t.idNode][d] != None:
                        tmp[d] += val * matrix[t.idNode][d]
                        
                        if Nodes.getNode(d).nodeType != "out":
                            toDo.append(Nodes.getNode(d))
                            
            done.append(t)

        self.calculPath = done
        
        result = []
        for n in self.outputNodes:
            result.append(tmp[n.idNode])

        return result

    #need to compute a value before evolving
    def addEdge(self, begin, end):
        matrix = self.toAdj()
    
        #test on current graph
        if begin == end:
            return False

        if Nodes.getNode(begin).nodeType == "out":
            return False
        
        if Nodes.getNode(end).nodeType == "in":
            return False

        if end in matrix[begin].keys():
            return False

        if begin in matrix[end].keys():
            return False

        #do not create cycle
        matrix[begin][end] = 1

        if self.isCycleLess() == False:
            return False
        
            #retrieve from edges
        test = Edges.get(begin, end)
        if test != None:
            newEdge = Edge(begin, end, test.idEdge)
            self.edges.append(newEdge)
            self.edges=sorted(self.edges, key= lambda x : x.idEdge)
        else:
            newEdge = Edge(begin, end)
            self.edges.append(newEdge)

        #matrix and calculPath outdated        
        self.matrixAdj = None
        self.calculPath = None
        self.nbActiveEdge += 1
        
        return True
    
    def addNode(self, begin, end):
        #look if the edge exist and is active
        matrix = self.toAdj()

        if end not in matrix[begin].keys():
            return False

        #ok create a node and link
        newNode = Node()

        self.hiddenNodes.append(newNode)
        
        #desactive old edge
        for e in self.edges:
            if e.begin == begin and e.end == end:
                e.disable = True
                break

        #create 2 edge
        e1 = Edge(begin, newNode.idNode, weight=1)
        e2 = Edge(newNode.idNode, end)
        
        self.edges.append(e1)
        self.edges.append(e2)
        self.nbActiveEdge += 1 # 2 - 1

        #matrix and calculPath outdated        
        self.matrixAdj = None
        self.calculPath = None

        return True
    
    def distance(self, n, c1=1, c2=1, c3=0.4):
        netA = self.edges
        netB = n.edges
        netLenA = len(netA)
        netLenB = len(netB)
        cptA = 0
        cptB = 0

        n= max(netLenA, netLenB)

        m=0
        w=0
        d=0
        e=0

        while cptA < netLenA and cptB < netLenB :
            if netA[cptA].idEdge == netB[cptB].idEdge: #match
                w += abs(netA[cptA].weight - netB[cptB].weight)
                m += 1
                cptA +=1
                cptB +=1

            elif netA[cptA].idEdge < netB[cptB].idEdge: #dismatch
                d += 1
                cptA += 1

            else:
                d += 1
                cptB += 1

        e= max(0,(netLenA - cptA) + (netLenB - cptB) -1)
        return ((c1*e)/n) + ((c2*d)/n) + (c3*w/m)
        #return [e,d,w,m]

    def crossover(self, n):
        child = Network(self.inputNodes, self.outputNodes)

        #node
        child.hiddenNodes = list(set(self.hiddenNodes) | set(n.hiddenNodes))

        if self.fitness > n.fitness:
            best = self
            complement = n
        else:
            best = n
            complement = self

        cptB = 0
        cptC = 0
        lenB = len(best.edges)
        lenC = len(complement.edges)
        
        while cptB < lenB and cptC < lenC:
            edgeB = best.edges[cptB]
            edgeC = complement.edges[cptC]
            
            if edgeB.idEdge == edgeC.idEdge:
                newEdge = Edge(edgeB.begin, edgeB.end, idEdge= edgeB.idEdge, weight= edgeB.weight, disable= edgeB.disable)

                cptB += 1
                cptC += 1
            
            elif edgeB.idEdge < edgeC.idEdge:
                newEdge = Edge(edgeB.begin, edgeB.end, idEdge= edgeB.idEdge, weight= edgeB.weight, disable= edgeB.disable)
                 
                cptB += 1

            else:
                newEdge = Edge(edgeC.begin, edgeC.end, idEdge= edgeC.idEdge, weight= edgeC.weight, disable= edgeC.disable)
                
                cptC += 1

            child.edges.append(newEdge)
            if newEdge.disable == False:
                child.nbActiveEdge += 1

        #Tail
 #       print("tail")
        while cptB < lenB:
            edgeB = best.edges[cptB]
            
            newEdge = Edge(edgeB.begin, edgeB.end, idEdge= edgeB.idEdge, weight= edgeB.weight, disable=edgeB.disable)
            cptB += 1
            child.edges.append(newEdge)

            if newEdge.disable == False:
                child.nbActiveEdge += 1
#        print("complement")
        while cptC < lenC-1:
            edgeC = complement.edges[cptC]
            
            newEdge = Edge(edgeC.begin, edgeC.end, idEdge= edgeC.idEdge, weight= edgeC.weight, disable=edgeB.disable)
            cptC += 1
            child.edges.append(newEdge)

            if newEdge.disable == False:
                child.nbActiveEdge += 1

        if child.isCycleLess() == True:
            return child
        
        return None
