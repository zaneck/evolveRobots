from sofaObject import SofaObject, BoxROI

class Canvas(SofaObject):
    """ Standard head of a sofa pyscn
    """
    def __init__(self, context):
        self.key = "Canvas"
        
        self.x = context['x']
        self.y = context['y']
        self.z = context['z']
        self.divX = context['divX'] + 1
        self.divY = context['divY'] + 1
        self.divZ = context['divZ'] + 1
    
    def __str__(self):
        return """
        ###############
        # CANVAS INFO #
        ###############
        sizeX, sizeY, sizeZ = {0}, {1}, {2}
        x , y , z = {3}, {4}, {5}
        unitX = float(sizeX) / (x-1)
        unitY = float(sizeY) / (y-1)
        unitZ = float(sizeZ) / (z-1)
        """.format(self.x, self.y, self.z, self.divX, self.divY, self.divZ)

class PartialFixedConstraint(SofaObject):
    
    def __init__(self, context):
        self.key = "PartialFixedConstraint"

        self.x = context['x']
        self.y = context['y']
        self.z = context['z']

    def __str__(self):
        return """\t################
        # PartialFixed #
        ################
        object.createObject('PartialFixedConstraint', fixedDirections='{0} {1} {2}', fixAll="true")
""".format(self.x, self.y, self.z)

class FixedConstraint(SofaObject):
    unique = False
    def __init__(self, context):
        self.key = "FixedConstraint"
        self.box = BoxROI(context)
        
    def __str__(self):
        return self.box.__str__() + """
        object.createObject('FixedConstraint', indices='@ROI{0}.indices')""".format(self.box.idBox)
    
    def minTopoAdd(self):
        return self.box.minTopoAdd()


class ConstantForceField(SofaObject):
    unique = False
    def __init__(self, context):
        self.key = "ConstantForceField"
        self.box = BoxROI(context)
        self.dirX = context['dirX']
        self.dirY = context['dirY']
        self.dirZ = context['dirZ']
        
    def __str__(self):
        return self.box.__str__() + """
        object.createObject('ConstantForceField', force='{1} {2} {3} ', points='@ROI{0}.indices')""".format(self.box.idBox, self.dirX, self.dirY, self.dirZ)

    def minTopoAdd(self):
        return self.box.minTopoAdd()
