# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import threading
import queue
from indi import *
from config import Config

# Tasklet/TasksManager/TaskDispatcher/DIstributeComputation
class Fitness(object):
    def __init__(self):
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
            
            #lock the best
            with self.bestOverAllLock:
                if self.bestOverAll == None:
                    self.bestOverAll = item
#                    print("NONE record {0}".format(self.bestOverAll.fitness))
                    
                if self.bestOverAll.fitness > item.fitness:
#                    print("New record {0}/{1}".format(item.fitness, self.bestOverAll.fitness))
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
