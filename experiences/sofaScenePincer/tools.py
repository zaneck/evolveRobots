posFixe = [(0,0), (0,19), (19,10)]

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

def matrixImageToMask(n, x, y):
    m = correction(posFixe, n)
    res = []

    for i in range((x-1),-1,-1):
        for j in range(y):
            if m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res

#part = "L" or "R", for left and right
def halfPart(n, x, y, part):
    m = correction(posFixe, n)
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


def look(tab, pos):
    if pos[0] < len(tab[0]) and pos[0] >=0:
        if pos[1] < len(tab) and pos[1] >=0:
            if tab[pos[0]][pos[1]] == 1:
                return True
    return False
    
def correction(fixe, tab):
    res = [[ 0 for _ in range(len(tab[0]))] for _ in range(len(tab))]
    
    toDo = []
    done = []

    for i in fixe:
        toDo.append(i)

    while not not toDo:
        pos = toDo.pop()
        done.append(pos)

        if look(tab, pos) == True:
            res[pos[0]][pos[1]] =1         

            if (pos[0], pos[1]+1) not in done:
                toDo.append((pos[0], pos[1]+1))
            if (pos[0], pos[1]-1) not in done:
                toDo.append((pos[0], pos[1]-1))
            if (pos[0]+1, pos[1]) not in done:
                toDo.append((pos[0]+1, pos[1]))
            if (pos[0]-1, pos[1]) not in done:
                toDo.append((pos[0]-1, pos[1]))
                    

    return res
