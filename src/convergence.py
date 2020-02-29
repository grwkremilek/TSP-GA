DISTANCES = ()

def evolveByCount(generation, converged, generation_limit):
    '''terminate after a given number of generations '''
    if generation >= generation_limit:
        converged = True
    return converged


def evolveByImprovement(distance):
    '''converged if the distance in the best population does not change for more than given rate over the last five generations'''
    DISTANCES.append(distance)
    if len(DISTANCES) >= 5:
        if all((100*(b - a)/a) <= self.rate for a, b in zip(DISTANCES[::1], DISTANCES[1::1])):
            converged = True
    DISTANCES = DISTANCES[-4:]
    return converged


def evolveUntilThreshold(self):
    '''terminate when given distance reached'''
    pass
    
    
def evolveByTime(self):
    '''terminate when a time limit reached'''
    pass
