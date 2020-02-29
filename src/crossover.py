import random
from collections import defaultdict


def PMX(parent1, parent2):
    '''partially-matched crossover'''
    l,r = sorted(random.sample(range(0, len(parent1)), 2))
    child = []
    count = 0
    for i in parent1:
        if count == l: break
        if i not in parent2[l:r]:
            child.append(i)
            count= count+1         
    child.extend(parent2[l:r])
    child.extend([g for g in parent1 if g not in child])
    return child


def ERO(parent1, parent2):
    '''edge recombination crossover '''
    parents = [parent1, parent2]
    size = len(parent1)
    for i in range(len(parents)):
        #create adjacency matrix
        neighbours = defaultdict(list)
        for parent in parents:
            for i in range(0, size):
                if i-1 >= 0 and parent[i-1] and parent[i-1] not in neighbours[parent[i]]:
                    neighbours[parent[i]].append(parent[i-1])
                if i+1 < size and parent[i+1] not in neighbours[parent[i]]:
                    neighbours[parent[i]].append(parent[i+1])
        #use the first chromozome from a random parent
        N = random.choice([parents[0][0], parents[1][0]])
        child = []
        while len(child) < size:
            child.append(N)
            for vals in neighbours.values():
                try:
                    vals.remove(N)
                except ValueError:
                    pass
            #find the neighbor of N with the fewest neighbors in its list
            if neighbours[N] != []:
                _N = _find_lowest(neighbours, N, size)
            elif len(child) != size:
                _N = random.choice([k for k, v in neighbours.items() if k not in child])
            N = _N
    return child


#### HELPER FUNCTIONS ####

def _find_lowest(neighbours, N, size):
    low, temp = '', size
    for k, v in neighbours.items():
        if k in neighbours[N] and len(v) < temp:
            low, temp = k, len(v)
    return low
    




