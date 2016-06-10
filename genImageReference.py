import sys

sys.path.insert(0,"..")

from imgTools import *

wd = "cheetah-Html/html-site/images/Reference/"

x=128
y=128

#circle
mat = circle(x,y)
matriceToImage(mat, x, y, wd+"circle.png")

#square
mat= square(x,y, int(x/2), int(y/2))
matriceToImage(mat, x, y, wd+"square.png")

#four Square
radius = 30 
mat = fourSquare(x, y, color=1, Rradius=15)

matriceToImage(mat, x, y, wd+"fourSquare.png")

#cross

mat= cross(x,y, int(x/2), int(y/2), Cradius=15)
matriceToImage(mat, x, y, wd+"cross.png")

