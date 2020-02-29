# TSP-GeneticAglorithm

- genetic algorithm for Travelling Salesman Problem implemented in python 3.6
- explores different selection, crossover and mutation methods 



## Getting Started

### Prerequisites

- one of the following geocoding services:
  * [Google Geocoding API](https://developers.google.com/maps/documentation/javascript/geocoding)
  * [OpenCage Geocoder](https://opencagedata.com/tutorials/geocode-in-python) (via [geopy](https://geopy.readthedocs.io/en/stable/#opencage))
- numpy
- kivy

## Basic Structure

- [Data](#data)
- [Route](#route)
- [Population](#population)
- [Parent selection](#parent-selection)
- [Crossover](#crossover)
- [Mutation](#mutation)
- [Survivor selection](#survivor-selection)
- [Convergence](#convergence)
- [Visualization](#visualization)
- [Gui](#gui)
- [Sources](#sources)

### Data

* choice and naming of places must satisfy geocoding API conditions ([naming constraints for Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro))



### Route
* represents a valid route
* methods in the class obtain latitude and longitude, calculate distance between cities and calculate the fitness function (the inverse of the total distance between the cities).


### Population
* collection of routes in one generation
* methods in the class create a population of random valid routes and rank the routes. 
* ranked routes are represented as a structured numpy array containing a total distance and a list of cities creating the route.

```
[(1117.13816146, ['Pardubice', 'Opole', 'Olomouc', 'Brno', 'Znojmo', 'Opava', 'Jihlava', 'Liberec', 'Prague'])
 (1455.81749732, ['Pardubice', 'Brno', 'Jihlava', 'Opava', 'Znojmo', 'Opole', 'Prague', 'Liberec', 'Olomouc'])
 (1463.1483717 , ['Prague', 'Pardubice', 'Opava', 'Liberec', 'Jihlava', 'Opole', 'Znojmo', 'Olomouc', 'Brno'])]
```

### Parent selection

methods to choose parents: 

* roulette wheel selection
    - fitness proportionate selection
    - fitness of each individual route is used to assign a probability of selection

* tournament selection
    - number of individuals are randomly selected from the population
    - individual with the highest fitness in the group is chosen as the first parent
    - repeated to chose the second parent.
  
* elitist selection
    - the best performing individuals from the population carry over to the next generation

### Crossover

* [PMX](https://www.youtube.com/watch?v=c2ft8AG8JKE)


* [ERO](https://en.wikipedia.org/wiki/Edge_recombination_operator)


### Mutation

* a way to introduce variation in the population
* possible to choose from:
    - swap mutation
    - inversion mutation
    - insertion mutation
    - scramble mutation

### Survivor selection





### Convergence

* Conditions under which GA will come to a stop
    - number of generations
    - time limit
    - distance improvement over a number of generations
    - value threshold



### Visualization


### Gui


### Sources

- [Genetic Algorithms Tutorial](https://www.tutorialspoint.com/genetic_algorithms/index.htm)
- Larrañaga, P., Kuijpers, C., Murga, R. H., Inza, I., & Dizdarevic, S. (1999). Genetic algorithms for the travelling salesman problem: A review of representations and operators. Artificial intelligence review: An international survey and tutorial journal, 13(2), 129-170. https://doi.org/10.1023/A:1006529012972
# TSP-GA
