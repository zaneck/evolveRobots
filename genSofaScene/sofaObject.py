# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################
import sys
sys.path.insert(0,"..")

from geometry import *

class SofaObject(object):
    """ Base class for representing Sofa Object.
    Used to create Sofa pyscn
    """
    
    unique = True 
    def __init__(self, context):
        self.key = "SofaObject"
        pass
    
    def __str__(self):
        """ return a pyscn instruction.
        """
        return ""

    """ return a geometry.shape, who must be in the minimum topology
    """
    def minTopoAdd(self):
        return None


class Head(SofaObject):
    """ Standard head of a sofa pyscn   
    """
    
    def __str__(self):
        return """
import Sofa

import topo
from tools import *
        

def createScene(rootNode):
        ########
        # HEAD #
        ########
        rootNode.createObject('RequiredPlugin', pluginName='SoftRobots')
        rootNode.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
        rootNode.findData("gravity").value = "0 -9810 0"
        rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765')
        rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")"""

class Tail(SofaObject):
    """ Standard ending of a pyscn
    """
    
    def __str__(self):
        return """
        ##########################################
        # Subtopology for Force Field            
        ##########################################
        mask = matrixImageToMask(topo.topology, x-1, y-1)
        hexaStr = tabToString(hexa, mask)
        
        subTopo = object.createChild('subTopo')
        subTopo.createObject('HexahedronSetTopologyContainer', position='@../grid.position', hexahedra=hexaStr)
        subTopo.createObject('HexahedronFEMForceField', template='Vec3d', name='FEM', method='large', poissonRatio='0.3',  youngModulus='500')

        
        ##########################################
        # Controller                             
        ##########################################
        object.createObject('PythonScriptController', filename="controller.py", classname="controller")
        
        return rootNode
"""

class FEM(SofaObject):

    def __str__(self):
        return """
        #######
        # FEM #
        #######
        object = rootNode.createChild('object')
        object.createObject('EulerImplicit', name='odesolver', firstOrder='0')
        object.createObject('CGLinearSolver')
        grid = object.createObject('RegularGridTopology', name= 'grid', n="{0} {1} {2}".format(x, y, z), max="{0} {1} {2}".format(sizeX, sizeY, sizeZ), min="0 0 0")
        hexa = grid.findData('hexahedra').value
        
        object.createObject('MechanicalObject', name='tetras', template='Vec3d', showIndices='false', showIndicesScale='4e-5', rx='0', dz='0')
        object.createObject('UniformMass', totalmass='0.02')
        """

class BoxROI(SofaObject):
    unique = False
    idBox = 0
    def __init__(self, context):
        #value between [-1,1]
        self.tx = context['tx']
        self.ty = context['ty']
        self.tz = context['tz']
        self.bx = context['bx']
        self.by = context['by']
        self.bz = context['bz']

        self.idBox = BoxROI.idBox
        BoxROI.idBox += 1
        
    
    def __str__(self):
        #value between [0, gridSize]
        a = """
        bx = unitX*{3}
        by = unitY*{4}
        bz = unitZ*{5}
        tx = unitX*{0}
        ty = unitY*{1}
        tz = unitZ*{2}""".format(self.tx, self.ty, self.tz, self.bx, self.by, self.bz, self.idBox)

        return a +"""
        object.createObject('BoxROI', name='ROI{0}'""".format(self.idBox)+""", box='{0} {1} {2} {3} {4} {5}'.format(bx ,by, bz, tx, ty ,tz), drawBoxes='true')"""

    def minTopoAdd(self):
        centX = self.tx - (self.tx - self.bx) / 2.0
        centY = self.ty - (self.ty - self.by) / 2.0
        halfW = self.tx - centX
        halfH = self.ty - centY
        
        return Rectangle(centX,centY,halfW,halfH)
