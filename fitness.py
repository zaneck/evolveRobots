import threading
import queue
from indi import *
from config import Config

class Fitness(object):
    def __init__(self,):
        self.name="Abstract fitness fun"
        self.bestOverAll = None
        self.bestNumber = 0

        #MultiThreading
        self.bestOverAllLock = threading.Lock()
        self.queue = queue.Queue()
        self.nbThread = Config.nbThread

        for _ in range(self.nbThread):
            t = threading.Thread(target=Fitness.worker, args=[self])
            t.daemon = True
            t.start()

    def worker(self):
        while True:
            item = self.queue.get()
            fit = self.simulate(item)
            item.fitness = fit

            print("")
            imgTest = item.toMatrice()
            printMatrix(imgTest, self.x, self.y)
            
            #lock the best
            with self.bestOverAllLock:
                if self.bestOverAll == None:
                    self.bestOverAll = item
                    print("NONE record {0}".format(self.bestOverAll.fitness))
                    
                if self.bestOverAll.fitness > item.fitness:
                    print("New record {0}/{1}".format(item.fitness, self.bestOverAll.fitness))
                    self.bestOverAll = item
                    self.bestNumber += 1

            self.queue.task_done()
            
    def computeValues(self, n):
        #load the queue
        for task in n:
            self.queue.put(task)

        #wait until all task done
        self.queue.join()

        return 1
        
    def simulate(self, n, idTask=0):
        raise NotImplementedError


class FitnessImage(Fitness):
    def __init__(self, name, draw, metric, x, y):
        Fitness.__init__(self)
        self.name=name
        
        self.x = x
        self.y = y

        self.metric = metric
        
        self.img = draw
        self.matriceImg = matriceTocouple(self.img, self.x, self.y)
#        printPict(self.img, self.x, self.y)
              
    def simulate(self, n, taskId=0):
        imgTest = n.toMatrice()

        if self.metric == 1:
            cptOk = fitnessHausdorff(imgTest, self.matriceImg, self.x, self.y)
        elif self.metric == 2:
            cptOk = fitnessHausdorffAverage(imgTest, self.matriceImg, self.x, self.y)
        elif self.metric == 3:
            cptOk = fitnessSorensenDice(imgTest, self.img, self.x, self.y)
        else:
            cptOk = fitnessMaxRessemblance(imgTest, self.img, self.x, self.y)
            
        return cptOk


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

def sorensenDice(img, mimg, x, y):
    cpt = 0
    cptA = 0
    cptB = 0
    
    for i in range(x):
        for j in range(y):                
            if img[i][j] == 1:
                cptA += 1
            if mimg[i][j] == 1:
                cptB += 1
            if img[i][j] == mimg[i][j] and img[i][j] == 1:
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
