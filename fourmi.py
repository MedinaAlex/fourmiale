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

# Calcul de la variance
def variance(liste): 
    m=moyenne(liste)
    return moyenne([(x-m)**2 for x in liste])

# Calcul de l'écart type
def ecartype(liste):
    return variance(liste)**0.5

# Calcul de la moyenne
def moyenne(liste): 
    return sum(liste) / len(liste)
    
G=nx.Graph()

noeuds = []
distances = []
# Nombre d'iteration
iter = 10
# Nombre de bars dans la liste à résoudre
nbBars = 100

# On récupère les coordonnées 
with open('open_pubs.csv', 'r') as csvfile:
    rows = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
    for row in rows:
        try:
            # Longitude et Latitude
            x = float(row[6])
            y = float(row[7])
            noeuds.append((x, y))
        # On continue si coordonées vide
        except:
            continue

# Fonction de Fitness, distance entre coordonnées 
def distance(a, b):
    R = 6378 #Rayon de la terre en Kmètre
    # On transforme en radian
    x = (b[1] - a[1]) * math.cos( 0.5*(b[0]+a[0]) )
    y = b[0] - a[0]
    # Calcul de distance
    d = R * math.sqrt( x*x + y*y )
    return d;


# On vient diviser la liste pour limiter les données
for i in range(iter):
    pop = noeuds[i*nbBars:(i+1)*nbBars]
    # On enlève les doublons
    pop = set(pop)
    pop = list(pop)
    
    G.clear()
    monde = pants.World(pop, distance)
    solver = pants.Solver()
    solution = solver.solve(monde)
    print("Distance", i, "=", solution.distance)
    distances.append(solution.distance)

    # On ajoute les noeuds au graph
    G.add_edges_from([(edge.start, edge.end) for edge in solution.path])
    plt.clf()
    nx.draw(G)
    plt.pause(1)
    
    # Enregistrement fichier
    plt.title("distance = %s" % solution.distance)
    plt.savefig("./images/d_%s.png" % i, bbox_inches="tight")
    plt.show()
    
print("Distance Moyenne = " + str(moyenne(distances)) + "Km")
print("Variance = " + str(variance(distances)))
print("ecart type = " + str(ecartype(distances)))



