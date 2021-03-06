# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. It contains functions to save in 
# a directory details about a genetic algorithm run. You can view 
# the report using your web browser and loading the index.html files.
#
# Contributors:
#	- created by damien.marchal@univ.lille1.fr
#############################################################################
import os
from imgTools import matriceToImage
from datetime import datetime

def activated():
        return False#True

theBasePath = None
theIndexFileName = None        
theIndexFile = None        
generationCount = 0
maxgeneration = 0  
        
def saveCandidateHistory(aCandidate):
        global generationCount
        historyPath = theBasePath+"/history/"  
        if not os.path.exists(historyPath): 
                os.mkdir(historyPath)
                              
        theCandidateFileName = historyPath+"/candidate{0}.html".format(aCandidate.myId)

def saveHistories(theCandidates):
        for candidate in theCandidates:
                saveCandidateHistory(candidate) 
                        
def addGeneration(theGeneration, theFitnessFunction):
        global generationCount
        theHistoryIndexFileName = "../../"+theBasePath+"/history/index.html"  
        theScoringFileName = "../../"+theBasePath+"/history/score.html"  
        generationPath = theBasePath+"/generation{0}".format(generationCount)                
        if not os.path.exists(generationPath): 
                os.mkdir(generationPath)

        if generationCount > 0:
                prevGenerationPath = "../generation{0}/index.html".format(generationCount-1)                
        else:
                prevGenerationPath = "../../"+theIndexFileName 
             
        if generationCount+1 < maxgeneration:       
                nextGenerationPath = "../generation{0}/index.html".format(generationCount+1)                
        else:
                nextGenerationPath = "../../"+theIndexFileName                
        
        theGenerationIndexFileName = generationPath+"/index.html"
        theGenerationIndexFile = open(theGenerationIndexFileName, "w+t")
        theGenerationIndexFile.write(
        """
        <html>
        <header>
        </header>
        <body>
        <center><h1>Generation: {0}</h1> <a href='{2}'>[prev]</a>[<a href='{4}'>history</a>][<a href='{5}'>scoring</a>]<a href='{3}'>[next]</a></center>
        <hr>
        Number of candidates: {1} <br> 
        <hr>
        <table width='100%'><tr= width='100%'>
        """.format(generationCount, len(theGeneration), prevGenerationPath, nextGenerationPath, theHistoryIndexFileName, theScoringFileName))
        num=0
        for candidate in theGeneration:
                if num % 20 == 0 and num != 0:
                        theGenerationIndexFile.write("</tr><tr>")
                #fixme {toMatrix instead of toMatrice}
                imageName = "candidate{0}.png".format(candidate.myId)
                imagePath = generationPath+"/"+imageName
                matriceToImage(theFitnessFunction.toMatrice(candidate), theFitnessFunction.canvas.res[0], 
                                                                        theFitnessFunction.canvas.res[1], imagePath)        
                theGenerationIndexFile.write("""
                        <td width='5%'><center>
                                <img src='{0}' width='100%' ></img><br>
                                {2}<br>
                                Score: {1:.0f}
                                </center>
                        </td>
                """.format(imageName, candidate.fitness, candidate.myId))
                num+=1
                
        theGenerationIndexFile.write("""</tr></table></body></html>""")
       
        theIndexFile.write("""<a href='../{0}'>Generation {1}</a><br> """.format(theGenerationIndexFileName, generationCount))
       
        generationCount+=1
        
        
        
def newExperiment(theDestPath, theFitnessFunction, theInitialPopulation, numGenerations):
        global theIndexFileName, theIndexFile, theBasePath, maxgeneration
        if not os.path.exists(theDestPath): 
                os.mkdir(theDestPath)
        maxgeneration = numGenerations
        theBasePath = theDestPath 
        theIndexFileName=theDestPath+"/index.html"
        historyIndexFileName = "../"+theBasePath+"/history/index.html"  
        theIndexFile=open(theIndexFileName, "w+t")
        theIndexFile.write("""
        <html>
        <header>
        </header>
        <body>
        <center>
        <h1>Experiment {1} </h1>
        <hr>
        </center>
        Fitness function: {0} <br>
        Initial Population: {2} <br>
        Number of generations: {3} <br>
        History: <a href='{4}'>View</a>
        <hr>
        """.format(theFitnessFunction.name, str(datetime.now()), len(theInitialPopulation), numGenerations, historyIndexFileName))
                
def endExperiment():
        global theIndexFile 
        theIndexFile.write("""
        </body>
        </html>
        """)

