import glob
import os
from Cheetah.Template import Template

class TemplateIndex(Template):
    title = 'Experiment'
    entries = os.listdir("./test")

class TemplateImage(Template):
    title="test"
    
        
t = TemplateIndex(file="index.tmpl")
indexFile = open("html-site/index.html", "w")
indexFile.write(str(t))
indexFile.close()

wd="./test"

wdList = os.listdir(wd)
nameSpace= {'entries':'None', 'nbImage':'0'}#searchList=[nameSpace]
t = TemplateImage(file="image.tmpl", searchList=[nameSpace])

for d in wdList:
    subwdList = os.listdir(wd+"/"+d)
    nameSpace['entries']=subwdList
    nameSpace['nbImage']=len(subwdList)
    nameSpace['exp']= d
    
    indexFile = open("html-site/"+d+"-dir.html", "w")
    indexFile.write(str(t))
    indexFile.close()
