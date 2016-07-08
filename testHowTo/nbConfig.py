addRate = [i/10 for i in range(1,9)]
cleanRate = [i/10 for i in range(0,9)]
crossRate = [i/10 for i in range(2,9)]

res01 = []
for i in addRate:
    for j in cleanRate:
        for k in crossRate:
            if i+j+k == 1.0:
                res01.append((i,j,k))
print("res01 {0}".format(len(res01)))

addRate = [i/100 for i in range(10,90)]
cleanRate = [i/100 for i in range(10,90)]
crossRate = [i/100 for i in range(20,90)]

res001 = []
for i in addRate:
    for j in cleanRate:
        for k in crossRate:
            if i+j+k == 1.0:
                res001.append((i,j,k))
print("res001 {0}".format(len(res001)))

print(res01)
