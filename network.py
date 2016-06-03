from edge import *
from node import *

class Network():

    def __init__(self, inputNode, outputNode):
        self.inputNodes = inputNode
        self.outputNodes = outputNode
        self.hiddenNodes = []

        self.edges = []
        self.nbActiveEdge = 0
        self.matrixAdj = None
        
        self.calculPath= None

        self.fitness = None
        self.behavior = None

    def linkInputOutput(self):
        for i in self.inputNodes:
            for o in self.outputNodes:
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
                if t in matrix[x.idNode].keys() and x not in done:
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
        print(tmp)
        result = []
        for n in self.outputNodes:
            result.append(tmp[n.idNode])

        return result

    #need to compute a value before evolving
    def addEdge(self, begin, end):
        matrix = self.toAdj()

        #test on current graph
        if Nodes.getNode(begin).nodeType == "in" and Nodes.getNode(end).nodeType == "in":
            print("end 1")
            return False

        if Nodes.getNode(begin).nodeType == "out" and Nodes.getNode(end).nodeType == "out":
            print("end 2")
            return False

        if end in matrix[begin].keys():
            print("end 3")
            return False

        #retrieve from edges
        test = Edges.get(begin, end)
        if test != None:
            newEdge = Edge(begin, end, test.idEdge)
            self.edges.append(newEdge)
            sort(self.edge, key= lambda x : x.idEdge)
        
        else:
            #do not create cycle
            #by order, the end must be compute after the begin            
            indexBegin = self.calculPath.index(Nodes.getNode(begin))
            indexEnd = self.calculPath.index(Nodes.getNode(end))
            
            if indexEnd< indexBegin:
                print("end 4")
                return False

            newEdge = Edge(begin, end)
            self.edges.append(newEdge)

        #matrix and calculPath outdated        
        self.matrixAdj = None
        self.calculPath = None
        self.nbActiveEdge += 1
        return True

    #add edge on the begin end edge
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
        e1 = Edge(begin, newNode.idNode)
        e1.weight=1
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

            elif netA[cptA].inov < netB[cptB].inov: #dismatch
                d += 1
                cptA += 1

            else:
                d += 1
                cptB += 1

        e= max(0,(netLenA - cptA) + (netLenB - cptB) -1)
        return ((c1*e)/n) + ((c2*d)/n) + (c3*w/m)
        #return [e,d,w,m]
