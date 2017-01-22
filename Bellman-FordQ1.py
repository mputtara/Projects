DistanceMatrix = [[0 for i in range(6)] for j in range(6)]

DistanceMatrix[0][0] = 0
DistanceMatrix[0][1] = 4
DistanceMatrix[0][2] = 6
DistanceMatrix[0][3] = 999
DistanceMatrix[0][4] = 999
DistanceMatrix[0][5] = 999
DistanceMatrix[1][0] = 999
DistanceMatrix[1][1] = 0
DistanceMatrix[1][2] = 999
DistanceMatrix[1][3] = 2
DistanceMatrix[1][4] = 1
DistanceMatrix[1][5] = 999
DistanceMatrix[2][0] = 999
DistanceMatrix[2][1] = 2
DistanceMatrix[2][2] = 0
DistanceMatrix[2][3] = 999
DistanceMatrix[2][4] = 2
DistanceMatrix[2][5] = 999
DistanceMatrix[3][0] = 999
DistanceMatrix[3][1] = 999
DistanceMatrix[3][2] = 999
DistanceMatrix[3][3] = 0
DistanceMatrix[3][4] = 1
DistanceMatrix[3][5] = 3
DistanceMatrix[4][0] = 999
DistanceMatrix[4][1] = 999
DistanceMatrix[4][2] = 999
DistanceMatrix[4][3] = 999
DistanceMatrix[4][4] = 0
DistanceMatrix[4][5] = 7
DistanceMatrix[5][0] = 999
DistanceMatrix[5][1] = 999
DistanceMatrix[5][2] = 999
DistanceMatrix[5][3] = 999
DistanceMatrix[5][4] = 999
DistanceMatrix[5][5] = 0

#print(DistanceMatrix)

prevcost = [0, 999, 999, 999, 999, 999]
curcost = [0, 999, 999, 999, 999, 999]
parent = [-1, -1, -1, -1, -1, -1]

for k in range(0,6):
    i = 0
    while (i < 6):
        j = 0
        while (j < 6):
            if ( (i != j) and (DistanceMatrix[i][j] != 999 ) ):
                if ((k>0) and (i>0)):
                    curcost[j] = min((DistanceMatrix[i][j] + prevcost[i]), (prevcost[j]))

                    if(((curcost[j] != prevcost[j]) )):
                        parent[j] = i
                        prevcost[j] = curcost[j]

                elif((k==0) and (i==0)):
                    curcost[j] = DistanceMatrix[i][j]
                    parent[j] = i
                    prevcost[j] = curcost[j]


            j += 1


        i += 1




print("Cost Matrix of the Graph:", curcost)

ParentNode = [-1, -1, -1, -1, -1, -1]
e = 0

for g in range(0, 6):
    if (parent[g] == -1):
        ParentNode[e] = -1
        e += 1
    if (parent[g] == 0):
        ParentNode[e] = 'S'
        e += 1
    if (parent[g] == 1):
        ParentNode[e] = 'A'
        e += 1
    if (parent[g] == 3):
        ParentNode[e] = 'C'
        e += 1

print("Parent Matrix of the Graph:", ParentNode)









