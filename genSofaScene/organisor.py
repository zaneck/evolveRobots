# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################

class Organisor(object):
    stock = {}

    def addToStock(self, o):
        try:
            Organisor.stock[type(o)].append(o)
        except KeyError:
            Organisor.stock[type(o)] = [o]
            
    def getStock(self):
        return Organisor.stock
