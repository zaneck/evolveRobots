def tabToString(tab, mask):
    res = ""
    for i in range(len(tab)):
        if mask[i] == 1:
            for j in tab[i]:
                res +="{0} ".format(j)
    return res

def matrixImageToMask(m, x, y):
    res = []

    for i in range(x-1,-1,-1):
        for j in range(y):
            if m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res

def circle(x,y, color=1, Cradius=None, imgChange=None):
    if imgChange == None:
        img = [[0 for _ in range(x)] for _ in range(y)]
    else:
        img = imgChange


#    img = [[0 for _ in range(x)] for _ in range(y)] 
    
    x0 = int(x / 2)
    y0 = int(y / 2)

    if Cradius == None:
        radius = int(1/3 * x) +2
    else:
        radius = Cradius
        
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    img[x0][ y0 + radius] = color
    img[x0][ y0 - radius] = color
    img[x0 + radius][ y0] = color
    img[x0 - radius][ y0] = color
 
    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        img[x0 + x][ y0 + y] = color
        img[x0 - x][ y0 + y] = color
        img[x0 + x][ y0 - y] = color
        img[x0 - x][ y0 - y] = color
        img[x0 + y][ y0 + x] = color
        img[x0 - y][ y0 + x] = color
        img[x0 + y][ y0 - x] = color
        img[x0 - y][ y0 - x] = color

    colorFill(img, x0, y0)
    return img

def colorFill(p, x, y, color=1):
    toDo=[(x,y)]
    for t in toDo:
        if p[t[0]][t[1]] != color:
            p[t[0]][t[1]] = color
            toDo.append((t[0]+1,t[1]))
            toDo.append((t[0]-1,t[1]))
            toDo.append((t[0],t[1]+1))
            toDo.append((t[0],t[1]-1))

def circleShape(tab):
    img = circle(10,10)
    mask = matrixImageToMask(img, 10,10) 
    return tabToString(tab, mask)

