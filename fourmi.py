# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:58:59 2018

@author: alexm
"""

import math
import pants
import csv
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

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


def distance(a, b):
    R = 6378 #Rayon de la terre en mètre
 
    x = (b[1] - a[1]) * math.cos( 0.5*(b[0]+a[0]) )
    y = b[0] - a[0]
    d = R * math.sqrt( x*x + y*y )
    return d;

sol = []
for i in range(len(noeuds) // 100 +1):
#for i in range(10):
    pop = noeuds[i*100:(i+1)*100]
    # On enlève les doublons
    pop = set(pop)
    pop = list(pop)
    
    G.clear()
    monde = pants.World(pop, distance)
    solver = pants.Solver()
    solution = solver.solve(monde)
    print("Distance", i, "=", solution.distance)
    
    G.add_edges_from(solution.tour)
    plt.clf()
    nx.draw(G)
    plt.pause(1)
    
    # Enregistrement fichier
    plt.title("distance = %s" % solution.distance)
    plt.savefig("./images/d_%s.png" % i, bbox_inches="tight")
    plt.show()
    

    sol.append(solution)
    
print("--------------total------------")
distance = sum([i.distance for i in sol])
sol2 = []
for i in sol:
    sol2 = [t for t in i.tour]

G.clear()
G.add_edges_from(sol2)
plt.clf()
nx.draw(G)
plt.pause(1)
print("Distance total = ", distance)
plt.title("total distance = %s" % distance)
plt.savefig("./images/total_%s.png" % distance, bbox_inches="tight")
plt.show()
    
# Graph avec networkX

