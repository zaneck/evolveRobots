#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa
from math import *
from __builtin__ import *

step=0.0005

class controllercube(Sofa.PythonScriptController):

    def initGraph(self, node):
        self.node = node
	self.cube1 = self.node.getChild("cube1")
	self.cube2 = self.node.getChild("cube2")
        self.restShapeSpringsForceField1 = self.cube1.getObject('fixation')
        self.restShapeSpringsForceField2 = self.cube2.getObject('fixation')
	
        
                
   
    def onKeyPressed(self,c):


        # + key :
        if ord(c)==61:
            stiffness = self.restShapeSpringsForceField1.findData('stiffness').value[0][0]*10
	    self.restShapeSpringsForceField1.findData('stiffness').value = str(stiffness)
	    self.restShapeSpringsForceField2.findData('stiffness').value = str(stiffness)
	    print "stiffness = "+str(self.restShapeSpringsForceField1.findData('stiffness').value[0][0])


        # - key :
        if ord(c)==45:
            stiffness = self.restShapeSpringsForceField1.findData('stiffness').value[0][0]/10
	    self.restShapeSpringsForceField1.findData('stiffness').value = str(stiffness)
	    self.restShapeSpringsForceField2.findData('stiffness').value = str(stiffness)
	    print "stiffness = "+str(self.restShapeSpringsForceField1.findData('stiffness').value[0][0])

     




