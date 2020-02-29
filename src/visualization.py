import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plotGA(distances, generations):
    '''plot the progession of the genetic algorithm '''
    plt.plot(range(generations), distances)
    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.xlabel('Generation')
    plt.ylabel('Distance')
    plt.show()


def _connectpoints(x, y, p1, p2):
    '''create lines connecting the cities'''
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

