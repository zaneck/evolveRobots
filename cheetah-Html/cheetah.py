import glob
import os
from Cheetah.Template import Template

class TemplateIndex(Template):
    title = 'Experiment'
    entries = os.listdir("html-site/images")
    
    
class TemplateImage(Template):
    title="test"

def imagetoHtml(imagePath, expName):
    subwdList = os.listdir(imagePath)
    absPath = []
    
    for a in subwdList:
        absPath.append("images/"+expName+"/"+a)

    nameSpace['entries']=absPath
    nameSpace['nbImage']=len(subwdList)
    nameSpace['exp']= expName

    print nameSpace['entries']
    
    imageFile = open("html-site/"+expName+"-dir.html", "w")
    imageFile.write(str(t))
    imageFile.close()
    
t = TemplateIndex(file="index.tmpl")
indexFile = open("html-site/index.html", "w")
indexFile.write(str(t))
indexFile.close()

wd="./html-site/images"
wdList = os.listdir(wd)

nameSpace= {'entries':'None', 'nbImage':'0'}#searchList=[nameSpace]
t = TemplateImage(file="image.tmpl", searchList=[nameSpace])

for d in wdList:
    imagetoHtml(wd+"/"+d, d)
