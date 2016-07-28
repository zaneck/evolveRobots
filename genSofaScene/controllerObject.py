# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################
from sofaObject import BoxROI

""" 
   Base class for representing Controller Object.
   Used to create controller py
"""
class ControllerObject(object):
    def __init__(self, context):
        self.key = "ControllerObject"
        self.haveBoxROI = False

    def initObject(self):
        """
        return the init object part for the initGraph fun
        """

        return ""

    def inLoopComputation(self):
        """
        return what it need to be compute during the simulation loop.
        Instruction for the onEndAnimationStep function
        """

        return ""

class DefaultArmor(ControllerObject):
    def __init__(self, context):
        self.key = "defaultArmor"
        self.haveBoxROI = False

    def initObject(self):
        return """import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node
        tetras = node.getObject('tetras').position """

    def inLoopComputation(self):
        return """
def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position"""

    def close(self):
        """ extra fonction"""
        return"""
        print("animation"),
        print("{0},".format(res)),"""
