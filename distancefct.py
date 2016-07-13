#############################################################################
#
# All the cost/distance function between two binary images.  
# 
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
def dist(a,b):
        return math.sqrt(math.pow((a[0]-b[0]) ,2)+pow((a[1]-b[1]) ,2))
        
def hausdorff(A,B):
    try:
        h1 = max(min(dist(a, b) for b in B) for a in A)
        h2 = max(min(dist(a, b) for a in A) for b in B)
    except:
        return sys.maxsize
        
    return max(h1,h2)

def hausdorffAverage(A,B):
    h1, h2 = 0, 0
    try:
        cpt = 0
        for a in A:
            h1 += min(dist(a, b) for b in B)
            cpt += 1
        h1 /= cpt

        cpt = 0
        for b in B:
            h2 += min(dist(a, b) for a in A)
            cpt += 1
        h2 /= cpt
    except:
        return sys.maxsize
        
    return max(h1,h2)

def matriceTocouple(m, x, y):
        res = []
        cpt = 0
        for i in range(x):
                for j in range(y):
                        if m[i][j] == 1:
                                res.append((i,j))
                                cpt += 1
        if cpt ==  x*y:
            return []
        return res

def sorensenDice(img, mimg):
    """Compute the difference between two images using the sorensendDice metric;
       The function returns a value between 0 and 1.  Zero stands for totally similar images while One 
       is for totally different content. 
       Have a look at https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient for more information
       """
    # We check that the two images have the same dimmensions 
    assert(len(img) == len(mimg))
    assert(len(img[0]) == len(mimg[0]))
    
    cpt = 0
    cptA = 0
    cptB = 0
    
    for i in range(len(img)):
        for j in range(len(img[0])):                
            #if img[i][j] == 1:
            cptA += 1
            #if mimg[i][j] == 1:
            cptB += 1
            if img[i][j] == mimg[i][j] :
                cpt += 1

    return 1- ((2*cpt) / (cptA + cptB))


    
def fitnessHausdorff(imgTest, mimg, x, y):
    mtest = matriceTocouple(imgTest, x, y)
    return hausdorff(mtest,mimg)

def fitnessHausdorffAverage(imgTest, mimg, x, y):
    mtest = matriceTocouple(imgTest, x, y)

    return hausdorffAverage(mtest,mimg)

def fitnessSorensenDice(imgTest, img, x, y):
    return sorensenDice(imgTest, img, x, y)


def fitnessMaxRessemblance(imgTest, img, x, y):
    cpt=0

    for i in range(x):
        for j in range(y):                
            if img[i][j] != imgTest[i][j]:
                cpt += 1
    return cpt /(x*y)
