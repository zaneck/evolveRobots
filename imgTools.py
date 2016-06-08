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

    
def circle(x,y, color=1):
    img = [[0 for _ in range(x)] for _ in range(y)] 
    
    x0 = int(x / 2)
    y0 = int(y / 2)

    radius = int(1/3 * x) +2

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
    if p[x][y] != color:
        p[x][y] = color
        colorFill(p,x+1,y)
        colorFill(p,x-1,y)
        colorFill(p,x,y+1)
        colorFill(p,x,y-1)


def fitnessP(n, img, x, y):
    cpt=0

    xMiddle = int(x / 2)
    yMiddle = int(y / 2)

    
    for i in range(x):
        for j in range(y):
            res = n.computeNetwork([(xMiddle - i) / x, (yMiddle -j) / y])[0]

            if res >= 0:
                test = 1
            else:
                test = 0
                
            if img[i][j] == 1 and img[i][j] == test:
                cpt += 10
            elif img[i][j] == test:
                cpt += 1
            else:
                cpt -= 30

    return cpt
