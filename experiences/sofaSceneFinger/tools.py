# posFixe = [(0,0), (10,19)]

def tabToString(tab, mask):
    res = ""
    for i in range(len(tab)):
        if mask[i] == 1:
            for j in tab[i]:
                res +="{0} ".format(j)
    return res


def matrixImageToMask(m, x, y):
    #m = correction(posFixe, n)
    res = []

    for i in range(x-1,-1,-1):
        for j in range(y):
            if m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res

def createCable(topo, debX, debY, sizeX, sizeY, x, y):
    #topo = correction(posFixe, n)
    positions = ""
    indices = ""

    ratioX = sizeX / (x-1)
    
    cpt = 0

    flagIn = False
    
    for i in range(debX, x-1, 1):
        if topo[debY][i] == 1:
            if flagIn == False:
                positions += "{0} {1} 2.5 ".format(ratioX*i , 28.5)
                indices += "{0} ".format(cpt)
                cpt += 1
                positions += "{0} {1} 2.5 ".format(ratioX*i + 1.5, 28.5)
                indices += "{0} ".format(cpt)
                cpt += 1
            else:
                positions += "{0} {1} 2.5 ".format(ratioX*i + 1.5, 28.5)
                indices += "{0} ".format(cpt)
                cpt += 1
            flagIn = True
            
        elif flagIn == True:
            flagIn = False
            positions += "{0} {1} 2.5 ".format(ratioX*i , 28.5)
            indices += "{0} ".format(cpt)
            cpt += 1
            
            
    # positions += "0.0 0.0 0.0"
    # indices += "0"

    return (positions,indices)

# def look(tab, pos):
#     if pos[0] < len(tab[0]) and pos[0] >=0:
#         if pos[1] < len(tab) and pos[1] >=0:
#             if tab[pos[0]][pos[1]] == 1:
#                 return True
#     return False
    
# def correction(fixe, tab):
#     res = [[ 0 for _ in range(len(tab[0]))] for _ in range(len(tab))]
    
#     toDo = []
#     done = []

#     for i in fixe:
#         toDo.append(i)

#     while not not toDo:
#         pos = toDo.pop()
#         done.append(pos)

#         if look(tab, pos) == True:
#             res[pos[0]][pos[1]] =1         

#             if (pos[0], pos[1]+1) not in done:
#                 toDo.append((pos[0], pos[1]+1))
#             if (pos[0], pos[1]-1) not in done:
#                 toDo.append((pos[0], pos[1]-1))
#             if (pos[0]+1, pos[1]) not in done:
#                 toDo.append((pos[0]+1, pos[1]))
#             if (pos[0]-1, pos[1]) not in done:
#                 toDo.append((pos[0]-1, pos[1]))
                    

#     return res
