import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
from datetime import datetime
from matplotlib.dates import DateFormatter
import pandas as pd
import csv

df = pd.read_csv('ita.csv', delimiter = ';')
datedf = df.pop('date')
date = datedf.values.tolist()
newdf = df.pop('new_cases')
new = newdf.values.tolist()
#print(date)
#print(new)

dates=[]
for element in date:
    dates.append(datetime.strptime(element, "%d/%m/%Y").strftime("%d-%m-%Y"))
    #.strftime("%Y-%m-%d"))
#print(dates)

x = dates
y = new

fig,ax = plt.subplots()
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y')) #cambia il formato della data
#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) #cambia la distanza tra i giorni
plt.plot(x,y, color='purple')
#fig.autofmt_xdate() #plt.gcf().autofmt_xdate() #testo in diagonale così é più leggibile
#plt.xticks(rotation=90) #curva il testo
ax.set_xticks(x[::20])
ax.set_xticklabels(x[::20], rotation=90)

ax.get_yaxis().get_major_formatter().set_scientific(False)

plt.ylabel('Nuovi Casi')
plt.xlabel('Data')
plt.title('Italia', fontdict=None, loc='center', pad=None)

plt.grid(b=None, which='major', axis='both', in_layout=True)

plt.tight_layout()

plt.savefig('italy_new.png', bbox_inches = "tight", dpi=1024)

plt.show()
