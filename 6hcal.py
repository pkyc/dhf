import sys
from itertools import permutations

num = 0
g1i = int(sys.argv[1])
g2i = int(sys.argv[2])
g3i = int(sys.argv[3])
g4i = int(sys.argv[4])
g5i = int(sys.argv[5])
g6i = int(sys.argv[6])

g1 = ['11','12','1x','21','22','2x','xx','x1','x2']
g2 = ['11','12','1x','21','22','2x','xx','x1','x2']
g3 = ['11','12','1x','21','22','2x','xx','x1','x2']
g4 = ['11','12','1x','21','22','2x','xx','x1','x2']
g5 = ['11','12','1x','21','22','2x','xx','x1','x2']
g6 = ['11','12','1x','21','22','2x','xx','x1','x2']

for i in range(0,g1i):
  for j in range(0,g2i):
    for k in range(0,g3i):
      for l in range(0,g4i):
        for m in range(0,g5i):
          for n in range(0,g6i):
            glist = []
            glist.append(g1[i])
            glist.append(g2[j])
            glist.append(g3[k])
            glist.append(g4[l])
            glist.append(g5[m])
            glist.append(g6[n])
            num += 1
            print num,",",glist


#for subset in permutations(2,1):
#  print (subset)
