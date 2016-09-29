def tabToString(tab, mask):
    res = ""
    for i in range(len(tab)):
        if mask[i] == 1:
            for j in tab[i]:
                res +="{0} ".format(j)
    return res

def matrixImageToMask(m, x, y):
    res = []

    for i in range(x-1,-1,-1):
        for j in range(y):
            if m[i][j] == 1:
                res.append(1)
            else:
                res.append(0)
    return res
