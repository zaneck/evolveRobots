import os
from imgTools import matriceToImage
from datetime import datetime

def activated():
        return True

theBasePath = None
theIndexFileName = None        
theIndexFile = None        
generationCount = 0 
        
def addGeneration(theGeneration):
        global generationCount
        
        generationPath = theBasePath+"/generation{0}".format(generationCount)                
        if not os.path.exists(generationPath): 
                os.mkdir(generationPath)
        
        theGenerationIndexFileName = generationPath+"/index.html"
        theGenerationIndexFile = open(theGenerationIndexFileName, "w+t")
        theGenerationIndexFile.write(
        """
        <html>
        <header>
        </header>
        <body>
        <center><h1>Generation: {0}</h1></center>
        <hr>
        Number of candidates: {1} <br> 
        """.format(generationCount, len(theGeneration)))
        num=0
        for candidate in theGeneration:
                #fixme {toMatrix instead of toMatrice}
                imageName = "candidate{0}.png".format(num)
                imagePath = generationPath+"/"+imageName
                matriceToImage(candidate.toMatrice(), candidate.x, candidate.y, imagePath)        
                theGenerationIndexFile.write("""
                        <img src='{0}' width='64' height='64'></img>
                """.format(imageName))
                num+=1
                
        theGenerationIndexFile.write("""</body></html>""")
       
        theIndexFile.write("""<a href='../{0}'>Generation {1}</a><br> """.format(theGenerationIndexFileName, generationCount))
       
        generationCount+=1
        
def newExperiment(theDestPath, theFitnessFunction, theInitialPopulation):
        global theIndexFileName, theIndexFile, theBasePath
        if not os.path.exists(theDestPath): 
                os.mkdir(theDestPath)
        
        theBasePath = theDestPath 
        theIndexFileName=theDestPath+"/index.html"
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
        Fitness function: {0}
        <hr>
        """.format(theFitnessFunction.name, str(datetime.now())))
                
def endExperiment():
        global theIndexFile 
        theIndexFile.write("""
        </body>
        </html>
        """)

