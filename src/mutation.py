import random

def swap(child, rate):
    '''swap 2 random cities in the route'''
    if(random.random() < rate):
        i,j = random.sample(range(0, len(child)), 2)
        child[i], child[j] = child[j], child[i]
    return child


def invert(child, rate):
    '''inverse a random swath in the route '''
    r = random.random()
    if(r < rate):
        l,r = sorted(random.sample(range(0, len(child)), 2))
        child[l:r] = child[l:r][::-1]
    return child


def insert(child, rate):
    ''' randomly extract a city and insert it in a randomly selected position'''
    city = child.pop(random.randrange(len(child)))
    child.insert(random.randint(0,len(child)),city)
    return child


def scramble(child, rate):
    ''' select a random swath and scramble the cities in it'''
    l,r = sorted(random.sample(range(0, len(child)), 2))
    swath = child[l:r]
    random.shuffle(swath)
    child[l:r] = swath
    return child
            
