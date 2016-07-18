# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################
from PIL import Image, ImageDraw

import math
import sys

def matriceToImage(m, w, h, destinationPath):
    """ Save a matrix into an RGB image of size w,h with a given name 
        w is width and h height. 
        destinationPath is the name of the destination file. No directory is created in case a path is given 
        Example of use:
                matriceToImage(aMatrix, 16, 16, "myFile.png")
    """
    img = Image.new("RGB", (w+2, h+2))
    draw = ImageDraw.Draw(img)

    color=[]

    # Draw a gray border line around the real image data to improve clarity. 
    for i in range(1,w+1):
        draw.point((i,0), fill=(127,127,127)) 
        draw.point((i,h+1), fill=(127,127,127)) 

    for j in range(1,h+1):
        draw.point((0,j), fill=(127,127,127)) 
        draw.point((w+1,j), fill=(127,127,127)) 

    #This generate a kind of optical illusion :) 
    #draw.point((0,0), fill=(255,255,255))
    #draw.point((0,h+1), fill=(255,255,255))
    #draw.point((w+1,h+1), fill=(255,255,255))
    #draw.point((w+1,0), fill=(255,255,255))
   
    # Draw the candidate data into the image
    for i in range(1,w+1):
        for j in range(1,h+1):
            if m[i-1][j-1] == 1:
                color.append((i,j))
                
    draw.point(color, fill=(255,0,0))
    img.save(destinationPath)
    
def matriceToGrayImage(m, destinationPath):
    """ Save a scalar [0,1] matrix into an RGB image of size w,h with a given name 
        w is width and h height. 
        destinationPath is the name of the destination file. No directory is created in case a path is given 
        Example of use:
                matriceToImage(aMatrix, 16, 16, "myFile.png")
    """
    w = len(m)
    h = len(m[0])
    img = Image.new("RGB", (w+2, h+2))
    draw = ImageDraw.Draw(img)

    color=[]

    # Draw a gray border line around the real image data to improve clarity. 
    for i in range(1,w+1):
        draw.point((i,0), fill=(127,127,127)) 
        draw.point((i,h+1), fill=(127,127,127)) 

    for j in range(1,h+1):
        draw.point((0,j), fill=(127,127,127)) 
        draw.point((w+1,j), fill=(127,127,127)) 

    #This generate a kind of optical illusion :) 
    #draw.point((0,0), fill=(255,255,255))
    #draw.point((0,h+1), fill=(255,255,255))
    #draw.point((w+1,h+1), fill=(255,255,255))
    #draw.point((w+1,0), fill=(255,255,255))
   
    # Draw the candidate data into the image
    for i in range(1,w+1):
        for j in range(1,h+1):
                c=int(m[i-1][j-1]*255)
                if m[i-1][j-1] > -0.01 and m[i-1][j-1] < 0.01:
                      draw.point((i,j), fill=(255,0,0))
                else:
                      draw.point((i,j), fill=(c,c,c))
    img.save(destinationPath)    
