# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################

class History(object):
        """ An History object stores all the evenement that happened during the evolution 
            of our population
            Example:
                h = History()
        """ 
        def __init__(self):
                self.events = []
            
        def addEvent(self, aCandidate, prev, genId, score):
                if prev[1] != None:
                        prev[1] = prev[1].myId
                if prev[2] != None:
                        prev[2] = prev[2].myId
                   
                self.events.append([aCandidate.myId, prev[0], prev[1], prev[2], genId, score])
            
            
        def saveToCSV(self, filename):
                theFile = open(filename, "w+t")
                theFile.write("id,type,a,b,gen,score\n")
                for event in self.events:
                        theFile.write("{0},{1},{2},{3},{4},{5}\n".format(event[0], event[1], event[2], event[3], event[4], event[5]))
                theFile.close()
