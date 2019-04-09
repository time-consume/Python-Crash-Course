import matplotlib.pyplot as plt
import csv

year = []
flood_height = []

with open('nile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        year.append(int(row[0]))
        flood_height.append(float(row[1]))

plt.plot(year,flood_height, label='Nile Flooding Over Years')
plt.xlabel('Year')
plt.ylabel('Flood height')
plt.title('Nile flooding data loaded from file')
plt.legend()
plt.show()
