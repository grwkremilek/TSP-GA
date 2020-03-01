import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plotTours(lons, lats, ax1, removeLines):
    lines = []
    ax1.scatter(lons, lats, color='black')
    ax1.set_xlabel("Longitude")
    ax1.set_ylabel("Latitude")
    
    for i in list(range(len(lats))):
        if i == len(lats)-1:
            lo1, lo2 = lons[i], lons[0]
            la1, la2 = lats[i], lats[0]
        else:
            lo1, lo2 = lons[i], lons[i+1]
            la1, la2 = lats[i], lats[i+1]
        lines.append(ax1.plot([lo1,lo2],[la1,la2],'k-'))
    plt.pause(0.01)
    if removeLines:
        for i in range(len(lines)):
            l = ax1.lines.pop(0)
    

def plotGA(distances, generationCount, ax2):
    '''plot the progession of the genetic algorithm '''
    ax2.plot(range(generationCount), distances)
    plt.xlabel('Number of Generations')
    plt.ylabel('Distance')
    

