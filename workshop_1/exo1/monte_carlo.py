"""
Le but de cet exercice est d'approximer la valeur de π (pi) avec la méthode de Monte Carlo : 
nous utiliserons deux modules pour cela : random math
random : module qui met à disposition des méthodes liées à l'aléatoire, comment la génération de nombres aléatoires
    (1) random.random() : génére un nombre aléatoire entre 0 et 1
math : module qui met à disposition des méthodes liées aux mathématiques
    (1) math.sqrt(<nombre positif>) : renvoie la racine carré du nombre

Voir le fichier 'monte_carlo_explication.md' pour les étape de l'exercice
"""
import random, math

def montecarl(n):
    l1 = [[random.random(), random.random()] for _ in range(n)]
    l2 = [ l1[i] for i in range(n) if math.sqrt(l1[i][0]**2 + l1[i][1]**2)<=1]
    return 4*len(l2)/n
print(montecarl(10000))
