#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sofa
from math import *
from __builtin__ import *

step=0.001

seuil = 0.02
countAlert= 20

class controllergrasper(Sofa.PythonScriptController):

    def initGraph(self, node):
        self.node = node
        self.cable0=self.node.getChild('cable0').getObject('c0')
        self.cable1=self.node.getChild('cable1').getObject('c1')

        self.count = 0
        self.flag = 0
        
    def onEndAnimationStep(self,deltaTime):
        v0 = self.cable0.value
        v1 = self.cable1.value

        if self.flag == 0:
            v0[0][0] = max(0,v0[0][0]-step)
            self.cable0.value = v0
            v1[0][0] = max(0,v1[0][0]-step)
            self.cable1.value = v1

            if v0[0][0] == 0:
                self.flag = 1
                self.count = 0

        elif self.flag == 1:
            self.count += 1
            if self.count == countAlert:
                self.flag = 2
                
        elif self.flag == 2:
            if v0[0][0] < seuil and v1[0][0] < seuil: 
                v0[0][0] = max(0,v0[0][0]+step)
                self.cable0.value = v0
                v1[0][0] = max(0,v1[0][0]+step)
                self.cable1.value = v1
            else:
                self.flag = 3
                self.count = 0

        elif self.flag == 3:
            self.count += 1
            if self.count == countAlert:
                self.flag = 0

                    
    def onKeyPressed(self,c):
        
        # # left key :
        if ord(c)==18:
            v0 = self.cable0.value
            v0[0][0] = max(0,v0[0][0]-step)
            self.cable0.value = v0

            v1 = self.cable1.value
            v1[0][0] += step
            self.cable1.value = v1

        # right key :
        if ord(c)==20:
            v0 = self.cable0.value
            v0[0][0] += step
            self.cable0.value = v0

            v1 = self.cable1.value
            v1[0][0] = max(0,v1[0][0]-step)
            self.cable1.value = v1

        # up key :
        if ord(c)==19:
            v0 = self.cable0.value
            v0[0][0] = max(0,v0[0][0]-step)
            self.cable0.value = v0

            v1 = self.cable1.value
            v1[0][0] = max(0,v1[0][0]-step)
            self.cable1.value = v1


        # down key :
        if ord(c)==21:
            v0 = self.cable0.value
            v0[0][0] += step
            self.cable0.value = v0

            v1 = self.cable1.value
            v1[0][0] += step
            self.cable1.value = v1







