# TSP-GeneticAlgorithm

- genetic algorithm for Travelling Salesman Problem implemented in python 3.6
- explores different selection, crossover and mutation methods 



## Getting Started

### Prerequisites

- one of the following geocoding services:
  * [Google Geocoding API](https://developers.google.com/maps/documentation/javascript/geocoding)
  * [OpenCage Geocoder](https://opencagedata.com/tutorials/geocode-in-python) (via [geopy](https://geopy.readthedocs.io/en/stable/#opencage))


## Basic Structure

- [Data](#data)
- [Population](#population)
- [Parent selection](#parent-selection)
- [Crossover](#crossover)
- [Mutation](#mutation)
- [Convergence](#convergence)
- [Sources](#sources)

### Data

* choice and naming of places must satisfy geocoding API conditions 
[naming constraints for The Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro)
[request practices for The OpenCage Geocoder](https://opencagedata.com/api#bestpractices)



### Population
* to make the algorithm the least black box possible, the Population class object is a list of class Tour objects, which again is a list of class City objects (the Matryoshka doll style), thus it is possible to access different levels of data with indices
* the Population class object is a tuple consisiting of: fitness float value, distance, the Tour class object


``` print(p[0])

    print(p[0][2])
    
    print(p[0][2][3])
    
    print(p[0][2][3].longitude)

``` 


```
(0.00047625626940124924, 2099.709892023475, [Olomouc, Opava, Trnava, Bratislava, Brno, Znojmo, Most, Opole, Jihlava, Prague, Liberec, Berlin, Pardubice])

[Olomouc, Opava, Trnava, Bratislava, Brno, Znojmo, Most, Opole, Jihlava, Prague, Liberec, Berlin, Pardubice]

Bratislava

17.1093063
```


### Parent selection

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


### Convergence

* Conditions under which GA will come to a stop
    - number of generations
    - time limit
    - distance improvement over a number of generations
    - value threshold



### Sources

- [Genetic Algorithms Tutorial](https://www.tutorialspoint.com/genetic_algorithms/index.htm)
- Larrañaga, P., Kuijpers, C., Murga, R. H., Inza, I., & Dizdarevic, S. (1999). Genetic algorithms for the travelling salesman problem: A review of representations and operators. Artificial intelligence review: An international survey and tutorial journal, 13(2), 129-170. https://doi.org/10.1023/A:1006529012972
