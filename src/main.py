from population import Population
from parent_selection import rouletteWheelSelection, tournamentSelection, elitistSelection
from crossover import PMX, ERO
from mutation import swap, invert, insert
from convergence import evolveByCount, evolveByImprovement
from visualization import plotGA

import matplotlib.pyplot as plt

import random


def main():

    #DATA
    genes = ['Prague', 'Olomouc', 'Liberec', 'Opava', 'Brno', 'Pardubice', 'Znojmo', 'Jihlava', 'Opole', 'Bratislava', 'Berlin', 'Trnava', 'Most']

    #INITIAL CONDITIONS
    populationSize = 100
    eliteSize = 4
    mutationRate = 0.4
    
    #CONVERGENCE SETTINGS
    converged = False
    generationCount = 0
    generationLimit = 150
    
    #PLOTS
    distances = []
    tours = []
    
    
    #CREATE FIRST GENERATION
    routes = [random.sample(genes, len(genes)) for i in range(populationSize)]
    p = Population(routes)

    while not converged:
        generationCount +=1
        distances.append(p[0][1])
        tours.append(p[0][2])
        converged = evolveByCount(generationCount, converged, generationLimit)
        
        ##plot the best tour in each generation
        lats = []
        lons = []
        for city in p[0][2]:
            lats.append(city.latitude)
            lons.append(city.longitude)

        ##elitism
        newRoutes = []
        if eliteSize:
            newRoutes.extend(elitistSelection(p, eliteSize))
    
        for i in range(eliteSize, populationSize):
            parent1 = rouletteWheelSelection(p)
            parent2 = rouletteWheelSelection(p)
            child = ERO(parent1, parent2)
            newRoutes.append(invert(child, mutationRate))

        p = Population(newRoutes)

    print('The shortest tour is  ', tours[-1])
    print('The distance is   ', distances[-1])
    
    plotGA(distances, generationCount)


if __name__ == '__main__': 
	main() 
