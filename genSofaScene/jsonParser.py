# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################
import json
from bagOfObject import *
import sofaObjectUsable 
import controllerObjectUsable

class JsonParser(object):

    def __init__(self, filename):
        f = open(filename)
        self.json = json.load(f)
        f.close()

    """ check if the json contain at least:
        - a field SofaObject which contain at least:
             - a CanvasDef field
    """
    def checkValidJson(self):
        if "SofaObject" not in self.json:
            print("You must have a SofaObject field")
            print("CHECK FAIL")
            raise KeyError
        if "CanvasDef" not in self.json["SofaObject"]:
            print("You must have a CanvasDef field in your SofaObject section")
            print("CHECK FAIL")
            raise KeyError

        if "Controller" not in self.json:
            print("You must have a Controller")
            print("CHECK FAIL")
            raise KeyError

        if len(self.json["Controller"]) < 2:
            print("Your controller must have at least a result field and a distance field, look the documentation for more details")
        
        print("CHECK DONE")

    
    def genBagOfObject(self):
        bag = BagOfObject()

        #SofaObject part
        for obj in self.json["SofaObject"].keys():
            cls = getattr(sofaObjectUsable, obj)

            if cls.unique == False:
                for context in self.json["SofaObject"][obj]:
                    a = cls(context)
                    bag.addToStockSofa(a)
            else:
                a=cls(self.json["SofaObject"][obj])
                bag.addToStockSofa(a)
        
        #Controller part
        for obj in self.json["Controller"].keys():
            cls = getattr(controllerObjectUsable, obj)

            if cls.unique == False:
                for context in self.json["Controller"][obj]:
                    a = cls(context)
                    bag.addToStockController(a)
            else:
                a=cls(self.json["Controller"][obj])
                bag.addToStockController(a)
        
        return bag
    
