import os
from Cheetah.Template import Template
import sys

class TemplateIndex(Template):
    entries = os.listdir("html-site/images")

class TemplateFirstGen(Template):
    entries = None

class TemplateNetwork(Template):
    pic = None
    fitness =None
    philo =None
    nbChild =None
    child= None
    
t = TemplateIndex(file="index.tmpl")

indexFile = open("html-site/index.html", "w")
indexFile.write(str(t))
indexFile.close()

f = open("html-site/images/"+sys.argv[1]+"/networkSet.txt", "r")

firstChild = []

child ={}
translate = {}

for line in f:
    lineSplit = line.split(" ")

    translate[lineSplit[0]] = lineSplit[1]
    
    #add first child
    if lineSplit[0] == lineSplit[1]:
        firstChild.append(lineSplit[1])
    
    #add child
    #if the last char not a digit
    if not lineSplit[0][-1].isdigit():
        if lineSplit[0][-1] != ")":
            elder = len(lineSplit[0])-1

            try:
                child[lineSplit[0][:elder]].append(lineSplit[0])
            except:
                child[lineSplit[0][:elder]] = [lineSplit[0]]
        else:
            pos = len(lineSplit[0])-2
            cptBracket = 1

            while cptBracket != 0:
                if lineSplit[0][pos] == ")":
                    cptBracket += 1
                elif lineSplit[0][pos] == "(":
                    cptBracket -= 1
                pos -= 1
                
            try:
                child[lineSplit[0][:elder]].append(lineSplit[0])
            except:
                child[lineSplit[0][:elder]] = [lineSplit[0]]
f.close()
            
#FirstChild Page
    
firstChild = list(map(lambda x: "images/"+sys.argv[1]+"/folks/"+x+".png", firstChild))

nameSpace= {}
nameSpace['entries'] = firstChild
nameSpace['nbImage'] = len(firstChild)

t = TemplateFirstGen(file="image.tmpl", searchList=[nameSpace])

circleFile = open("html-site/"+sys.argv[1]+"-dir.html", "w")
circleFile.write(str(t))
circleFile.close()

#create network page, second lecture

f = open("html-site/images/"+sys.argv[1]+"/networkSet.txt", "r")

nameSpace={}


for line in f:
    lineSplit = line.split(" ")

    nameSpace["picPath"] = "images/"+sys.argv[1]+"/folks/"
    nameSpace["pic"] = "images/"+sys.argv[1]+"/folks/"+lineSplit[1]+".png"
    nameSpace["fitness"] = float(lineSplit[2])
    nameSpace["philo"] = lineSplit[0]
    try:
        nameSpace["nbChild"] = len(child[lineSplit[0]])  
        # nameSpace["child"] = child[lineSplit[0]]

        nameSpace["child"] = []
        for c in child[lineSplit[0]]:
            nameSpace["child"].append(translate[c]+"-"+c)
    except:
        nameSpace["nbChild"] = 0
        nameSpace["child"] = None

    
    circleFile = open("html-site/"+lineSplit[1]+"-pic.html", "w")
    t = TemplateNetwork(file="network.tmpl", searchList=[nameSpace])
    circleFile.write(str(t))
    circleFile.close()

        
f.close()
