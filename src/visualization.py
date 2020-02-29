import matplotlib.pyplot as plt
import matplotlib.ticker as mticker



def plotTours(lons, lats, ax):
    lines = []
    ax.scatter(lons, lats, color='red')
    for i in list(range(len(lats))):
        if i == len(lats)-1:
            lo1, lo2 = lons[i], lons[0]
            la1, la2 = lats[i], lats[0]
        else:
            lo1, lo2 = lons[i], lons[i+1]
            la1, la2 = lats[i], lats[i+1]
        lines.append(ax.plot([lo1,lo2],[la1,la2],'k-'))
    plt.pause(0.01)
    for i in range(len(lines)):
        ax.lines.pop(0)
    

def plotGA(distances, generations):
    '''plot the progession of the genetic algorithm '''
    fig2 = plt.figure()
    ax = plt.plot(range(generations), distances)
    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.xlabel('Generation')
    plt.ylabel('Distance')
    plt.show()

