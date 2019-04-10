# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:08:16 2019

@author: jhanc
"""
#ffmpeg -r 30 -i %4d.png -vcodec mpeg4 -y movie.mp4

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

matplotlib.rcParams.update({'font.size': 16, 'font.family': 'serif'})

def save():
    os.system("ffmpeg -r 60 -i %0001d.png -vcodec mpeg4 -y movie.mp4")

def getDecimalMSDPercentages(functionSpace, d):
    tally = [0,0,0,0,0,0,0,0,0,0]
    
    for x in range(0, d):
        for y in range(0, d):
            number = functionSpace[x, y]
            MSD = int(str(number)[0])
            tally[MSD] += 1
    
    for i in range(0, len(tally)):
        tally[i] /= (d*d)
        
    return tally

def xy(d):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    functionSpace = np.zeros((d,d))
    for x in range(d):
        for y in range(d):    
            functionSpace[x, y] = (x*y) % d
            
    return functionSpace

def getNextFilename(frameNumber):
    if frameNumber < 10:
        return "frames/000"+str(frameNumber)+".png"
    elif frameNumber < 100:
        return "frames/00"+str(frameNumber)+".png"
    elif frameNumber < 1000:
        return "frames/0"+str(frameNumber)+".png"
    else:
        return "frames/"+str(frameNumber)+".png"

fig = plt.figure(figsize=(10,10), dpi=100)
ax1 = plt.subplot2grid((3,2), (0,0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid((3,2), (2,0), colspan=2)

ax1.set_title("f(x,y) = xy")
ax1.get_xaxis().set_visible(False)

differentDigitsTallied = [0,1,2,3,4,5,6,7,8,9]
ax2.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
ax2.set_title("MSD Percentages")
ax2.set_xticks(differentDigitsTallied)

for d in range(1,1001):
    functionSpace = xy(d)
    ax1.clear()
    ax1.matshow(functionSpace)
    ax1.get_yaxis().set_ticks([0, d/4, d/2, d*3/4, d])
    ax1.get_xaxis().set_visible(False)
    
    ax2.clear()
    ax2.plot(differentDigitsTallied,getDecimalMSDPercentages(functionSpace, d), color="blue", lw=1, marker='s')
    plt.tight_layout()

    fig.savefig(getNextFilename(d), dpi=100)
    print(str(d) + " rendered.")

plt.show()


        
