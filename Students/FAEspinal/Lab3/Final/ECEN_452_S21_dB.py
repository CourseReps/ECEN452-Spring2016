import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for Freq, S21
Freq = []
S21 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('TRL_Demo_Line_S21_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        Freq.append(float(row['Freq']))
        S21.append(float(row['S21']))


##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(Freq, S21, '-b', label="S21 Data") #plot y1 vs. x, solid-blue, add lable for legend

ax1.set_xlim(min(Freq), max(Freq)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('S21 db Plot') #add plot title
plt.xlabel('Freq [Hz]') #add x-axis title
plt.ylabel('S21 Log Mag[dB]') #add y-axis title
plt.ylim([-5,0])

plt.show() #required to display plots