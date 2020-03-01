from population import Population
from parent_selection import rouletteWheelSelection, tournamentSelection, elitistSelection
from crossover import PMX, ERO
from mutation import swap, invert, insert
from convergence import evolveByCount, evolveByImprovement
from visualization import plotTours, plotGA

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
    generationCount = 1
    generationLimit = 50
    
    #PLOTS
    distances = []
    tours = []
    removeLines = True      
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,15))               #create a figure with 2 subplots
    
    ax2.set_xlim([1, generationLimit])                                  #fixed length of x-axis (number of generations)
    ax2.locator_params(nbins=10, axis='x')                              # control density of axis desctiption
    
    
    #CREATE FIRST GENERATION
    routes = [random.sample(genes, len(genes)) for i in range(populationSize)]
    p = Population(routes)

    while not converged:
        print(generationCount)
        distances.append(p[0][1])
        tours.append(p[0][2])
        converged = evolveByCount(generationCount, converged, generationLimit)
        
        if converged:
            removeLines = False
        
        ##plot the best tour in each generation
        lats = []
        lons = []
        for city in p[0][2]:
            lats.append(city.latitude)
            lons.append(city.longitude)
        plotTours(lons, lats, ax1, removeLines)
        
        ##
        plotGA(distances, generationCount, ax2)

        #add the most successful individuals from the previous generation
        newRoutes = []
        if eliteSize:
            newRoutes.extend(elitistSelection(p, eliteSize))
    
        #create offspring vie crossover and mutation 
        for i in range(eliteSize, populationSize-10):
            parent1 = rouletteWheelSelection(p)
            parent2 = rouletteWheelSelection(p)
            child = ERO(parent1, parent2)
            newRoutes.append(invert(child, mutationRate))
        
        #generate 10 new random individuales
        for j in range(10):
            routes = random.sample(genes, len(genes))
            newRoutes.append(routes)

        p = Population(newRoutes)
        generationCount +=1

    print('The shortest tour is  ', tours[-1])
    print('The distance is   ', distances[-1])
    plt.show()

if __name__ == '__main__': 
	main() 
