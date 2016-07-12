# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################

class Canvas(object):
    """A Canvas is used to discreetize a candidate into a grid
       The Canvas is always centered at 0,0 and of size -1,-1 to 1,1
       Example:
                c = Canvas( dim(1.0,1.0), res(16,16)) 
    """
    def __init__(self, dim, res):
        self.dim = dim 
        self.res = res  

    def toMatrice(self, candidate, binfct):
        """Converts a candidate into a matrix using a given binning function.
           The function is evaluated in the middle of the grid voxels.
        """ 
        res =[[0 for _ in range(self.res[1])] for _ in range(self.res[0])]

        for i in range(self.res[0]):
                for j in range(self.res[1]):
                    px = ( self.dim[0] * i / self.res[0] ) - 0.5 * self.dim[0] + 0.5 * self.dim[0] / self.res[0] 
                    py = ( self.dim[1] * j / self.res[1] ) - 0.5 * self.dim[1] + 0.5 * self.dim[1] / self.res[1]
                    
                    res[i][j] = binfct( candidate.getValueAt( (px,py) ))
        return res
        
def printMatrix(m):
        """ Prints a m = {
               0_0, 1_0, 2_0, 3_0,
               0_1, 1_1, 2_1, 3_1,
               ...
            }
            
         """
        for j in range(len(m[0])):
            for i in range(len(m)):
                if m[i][j] == 1:
                        print("X", end="")
                else:
                        print("-", end="")
            print("")
