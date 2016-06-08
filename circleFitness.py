from imgTools import *
from noveltySearch import *
        
class NoveltyFitnessCircle(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="Novelty Cirlce fitness fun"

        self.x = 32
        self.y = 32
        
        self.img = circle(self.x, self.y, color=1)
        printPict(self.img, 32, 32)
        
        
    def simulate(self, n):
        cptOk = fitnessP(n, self.img, self.x, self.y)
        
        return ([cptOk,0], cptOk)
