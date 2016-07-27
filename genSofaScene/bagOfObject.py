# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################
from sofaObject import *

from controllerObject import controllerObjectList

class BagOfObject(object):
    stockSofa = {}
    stockController = {}

    def addToStock(self, o):
        if o.key in controllerObjectList:
            try:
                BagOfObject.stockController[o.key].append(o)
            except KeyError:
                BagOfObject.stockController[o.key] = [o]
            return
        else:
            try:
                BagOfObject.stockSofa[o.key].append(o)
            except KeyError:
                BagOfObject.stockSofa[o.key] = [o]
            return
   
    
    def getStockSofa(self):
        return BagOfObject.stockSofa

    def getKeysSofa(self):
        return BagOfObject.stockSofa.keys()
    
    def getDataSofa(self, key):
        return BagOfObject.stockSofa[key]

    
    def getKeysController(self):
        return BagOfObject.stockController.keys()

    def getStockController(self):
        return BagOfObject.stockController

    def getDataController(self, key):
        return BagOfObject.stockController[key]
