# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 18:43:42 2016

@author: Matias
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []
y1 = []
#y2 = []
#y3 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('CS_CD_MK_50ohm_line_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['x']))
        y1.append(float(row['y1']))
#        y2.append(float(row['y2']))
#        y3.append(float(row['y3']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, '-r', label="y1 Data") #plot y1 vs. x, solid-blue, add lable for legend
ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=1) #add legend at location #1 (top-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Frequency vs Phase Plot') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Phase [deg]') #add y-axis title
plt.plot(x, np.poly1d(np.polyfit(x, y1, 1))(x))
regression = np.polyfit(x, y1, 1)
ax1.annotate('f(x)='+str(regression[0])+'x + '+str(regression[1]), xy=(1, 0), xycoords='axes fraction', fontsize=16,
                horizontalalignment='right', verticalalignment='bottom')

plt.show() #required to display plots