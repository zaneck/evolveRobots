from PIL import Image, ImageDraw

def makeImg(n,x,y):
    img = [[0 for _ in range(x)] for _ in range(y)] 
    xMiddle = int(x / 2)
    yMiddle = int(y / 2)
    
    for i in range(x):
        for j in range(y):
            test = n.computeNetwork([(xMiddle - i) / x, (yMiddle -j) / y])[0]
            if test >= 0:
                img[i][j]=1
    return img

def matriceToImage(m, x, y, nameFile):
    img = Image.new("RGB", (x, y))
    draw = ImageDraw.Draw(img)

    color=[]

    for i in range(x):
        for j in range(y):
            if m[i][j] == 1:
                color.append((i,j))
                
    draw.point(color, fill=(255,255,255))
    img.save(nameFile)

def cross(x, y, centX, centY, color=1, Cradius=None, imgChange=None):
    if imgChange == None:
        img = [[0 for _ in range(x)] for _ in range(y)]
    else:
        img = imgChange

    if Cradius == None:
        radius = int(1/4 * x)
    else:
        radius = Cradius

    for i in range(centX-radius, centX+radius):
        for j in range(0,y):
            img[i][j] = color

    for i in range(0,x):
        for j in range(centY-radius, centY+radius):
            img[i][j] = color

    return img

def fourSquare(x, y, color=1, Rradius=None, imgChange=None):
    if imgChange == None:
        img = [[0 for _ in range(x)] for _ in range(y)]
    else:
        img = imgChange
        
    if Rradius == None:
        radius = int(1/4 * x)
    else:
        radius = Rradius

    square(x,y, int(x/2)-(2*radius), int(y/2)-(2*radius), Rradius=15, imgChange=img)
    square(x,y, int(x/2)+(2*radius), int(y/2)-(2*radius), Rradius=15, imgChange=img)
    square(x,y, int(x/2)-(2*radius), int(y/2)+(2*radius), Rradius=15, imgChange=img)
    square(x,y, int(x/2)+(2*radius), int(y/2)+(2*radius), Rradius=15, imgChange=img)

    return img    
    
def square(x, y, centX, centY, color=1, Rradius=None, imgChange=None):
    if imgChange == None:
        img = [[0 for _ in range(x)] for _ in range(y)]
    else:
        img = imgChange
        
    x0 = centX
    y0 = centY

    if Rradius == None:
        radius = int(1/4 * x)
    else:
        radius = Rradius
        
    tlx = x0 - radius
    tly = y0 - radius

    brx = x0 + radius
    bry = y0 + radius
    
    for i in range(tlx,brx):
        for j in range(tly,bry):
            img[i][j] = color

    return img
            
def circle(x,y, color=1, Cradius=None, imgChange=None):
    if imgChange == None:
        img = [[0 for _ in range(x)] for _ in range(y)]
    else:
        img = imgChange


    img = [[0 for _ in range(x)] for _ in range(y)] 
    
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

def printPict(p, x, y):
    for i in range(x):
        print(p[i])

def colorFill(p, x, y, color=1):
    toDo=[(x,y)]
    for t in toDo:
        if p[t[0]][t[1]] != color:
            p[t[0]][t[1]] = color
            toDo.append((t[0]+1,t[1]))
            toDo.append((t[0]-1,t[1]))
            toDo.append((t[0],t[1]+1))
            toDo.append((t[0],t[1]-1))

def fitnessP(imgTest, img, x, y):
    cpt=0

    xMiddle = int(x / 2)
    yMiddle = int(y / 2)

    
    for i in range(x):
        for j in range(y):                
            if img[i][j] == 1 and img[i][j] == imgTest[i][j]:
                cpt += 10
            elif img[i][j] == imgTest[i][j]:
                cpt += 1
            else:
                cpt -= 30

    return cpt

def blockBehavior(imgTest, img, x, y, blockSize=8):
    res =[]

    for beginX in range(0,x,8):
        for beginY in range(0,y,8):
            tmp=0
            for i in range(beginX, beginX + blockSize):
                for j in range(beginY, beginY + blockSize):
                    if img[i][j] == 1 and img[i][j] == imgTest[i][j]:
                        tmp += 10
                    elif img[i][j] == imgTest[i][j]:
                        tmp += 1
                    else:
                        tmp -= 30
            res.append(tmp)
    return res
