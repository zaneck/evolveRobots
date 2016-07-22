# coding: utf8 
#############################################################################
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################
# an arbitrary value for the canvas.  
g_maxresolution = 4096
from indi import Indi
from geometry import Shape 

class Canvas(object):
    """A Canvas is used to discreetize a candidate into a grid
       The Canvas is always centered at 0,0. 
       The dim parameter is used to specify the canvas dimmension in the global
       coordinate system.
       The res parameter is used to specify the canvas resolution. 
       Example:
                c = Canvas( dim(1.0,1.0), res(16,16)) 
    """
    def __init__(self, dim, res):
        if dim[0] > dim[1]:
                raise ValueError("dimmensions should be dim[0] < dim[1].")

        if res[0] < 0 or res[1] < 0:
                raise ValueError("resolution should be greater than zero.")

        if res[0] > g_maxresolution or res[1] > g_maxresolution:
                raise ValueError("resolution should be greater than zero.")

    
        self.dim = dim 
        self.res = res  

    @property
    def resolution(self):
        return self.res

    def toMatrice(self, candidate, binfct):
        """Converts a candidate into a matrix using a given binning function.
           The binning function is use to convert from the -inf, +inf interval a 
           candidate can return to a finite number of "bins".  
           The function is evaluated in the middle of the grid voxels.
        """ 
        res =[[0 for _ in range(self.res[1])] for _ in range(self.res[0])]

        if not isinstance(candidate, (Shape, Indi)):
                raise TypeError("The 'candidate' parameter must be of class 'Shape or Indi'")

        if not callable(binfct):
                raise TypeError("The 'binfct' must be a callable object")
                
        # For each line and column of the resulting matrix. 
        for i in range(self.res[0]):
                for j in range(self.res[1]):
                    # Calculate the position of the center of the pixel/voxel using the 
                    # grid position, resolution and dimmension.  
                    px = ( self.dim[0] * i / self.res[0] ) - 0.5 * self.dim[0] + 0.5 * self.dim[0] / self.res[0] 
                    py = ( self.dim[1] * j / self.res[1] ) - 0.5 * self.dim[1] + 0.5 * self.dim[1] / self.res[1]
                    
                    # Query the candidate to get its content at the calculated location px,py 
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
