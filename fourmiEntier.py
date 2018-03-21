# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:09:28 2018

@author: alexm
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:58:59 2018

@author: alexm
"""

import random
import math
import pants




import csv
noeuds = []
with open('open_pubs.csv', 'r') as csvfile:
    rows = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
    for row in rows:
        try:
            x = float(row[6])
            y = float(row[7])
            noeuds.append((x, y))
        except:
            continue
print("fini")

def distance(a, b):
    return math.sqrt(pow(a[1]-b[1],2) + pow(a[0]-b[0],2))

monde = pants.World(noeuds, distance)
solver = pants.Solver()
solution = solver.solve(monde)
    
print("---------------- Distance --------------")
print(solution.distance)


