import random

def rouletteWheelSelection(population):
    '''Choose a random number between zero and the sum of distances, then choose a candidate whose section on the section wheel includes the random number'''
    fitnesses = [population[i][0] for i in range(len(population))]
    total = sum(fitnesses)
    random_point = random.uniform(0, total)
    current = 0
    for i in range(len(fitnesses)):
        current += fitnesses[i]
        if current > random_point:
            for j in range(len(population)):
                if population[j][0] == fitnesses[i]:
                    return population[j][2]


def tournamentSelection(population):
    '''Choose the best candidate from a random sample'''
    candidates = np.random.choice(population, 3)
    return np.sort(candidates)[0]


def elitistSelection(population, size):
    '''A number of best solutions is used to build next generation'''
    return [population[i][2] for i in range(size)]
