def tabToString(tab, mask):
    res = ""
    for i in range(len(tab)):
        try:
            if mask[i] == 1:
                for j in tab[i]:
                    res +="{0} ".format(j)
        except IndexError:
            return res
    return res

def matrixImageToMask(m, x, y):
    res = []

    for i in range((x-1),-1,-1):
        for j in range(y):
            if m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res

#part = "L" or "R", for left and right
def halfPart(m, x, y, part):
    res = []
    
    for i in range((x-1),-1,-1):
        for j in range(y):
            if part=="L" and j > (y-1)/2 - 1:
                res.append(0)
            elif part=="R" and j < (y-1)/2 + 2:
                res.append(0)
            elif m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res

def selectHexa(tab, mask):
    res = []
    for i in range(len(tab)):
        try:
            if mask[i] == 1:
                tmp=[]
                for j in tab[i]:
                    tmp.append(j)
                res.append(tmp)
        except IndexError:
            return res
    return res

#take a set of position, a set of hexa in str format
# return a reduce point set and an according hexaStr
def reducePositionOverHexa(position, hexa):
    newPosition = {} #<old id><new,(x,y,z)>
    positionStr =""
    cpt = 0

    #select Position and rename into the newPosition dict
    for i in hexa:
        for j in i:
            if j not in newPosition:
                newPosition[j] = (cpt,position[j])
                positionStr += "{} {} {} ".format(newPosition[j][1][0], newPosition[j][1][1], newPosition[j][1][2])
                cpt += 1
    
    #construct the updated hexaStr
    updatedHexaStr = ""
    for i in hexa:
        for j in i:
            updatedHexaStr +="{0} ".format(newPosition[j][0]) 

    return (positionStr, updatedHexaStr)

