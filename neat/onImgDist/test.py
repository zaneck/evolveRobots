import math
from PIL import Image

# i1 = Image.open("1.png")
# i2 = Image.open("circle.png")
# assert i1.mode == i2.mode, "Different kinds of images."
# assert i1.size == i2.size, "Different sizes."

# pairs = zip(i1.getdata(), i2.getdata())
# if len(i1.getbands()) == 1:
#         # for gray-scale jpegs
#         dif = sum(abs(p1-p2) for p1,p2 in pairs)
# else:
#         dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

#         ncomponents = i1.size[0] * i1.size[1] * 3
#         print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)


def dist(a,b):
        return math.sqrt(math.pow((a[0]-b[0]) ,2)+pow((a[1]-b[1]) ,2))

        
def hausdorff(A,B):
        h1 = max(min(dist(a, b) for b in B) for a in A)
        h2 = max(min(dist(a, b) for a in A) for b in B)

        return max(h1,h2)


def matriceTocouple(m, x, y):
        res = []
        for i in range(x):
                for j in range(y):
                        if m[i][j] == 1:
                                res.append((i,j))
        return res
