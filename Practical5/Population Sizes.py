# 1.Input the list of uk_countries.
# 2.Input the list of China_provinces.
# 3.Output the sorted version of uk_countries.
# 4.Output the sorted version of China_provinces.

uk_countries = [57.11, 3.13, 1.91, 5.45] # List of uk_countries.
China_provinces = [65.77, 41.88, 45.28, 61.27, 85.15] # List of China_provinces.
print("uk_countries after sorted is", sorted(uk_countries)) # Output the sorted version.
print("China_provinces after sorted is", sorted(China_provinces)) # Output the sorted version.

# 1.Import matplotlib.pyplot to visualize statistic.
# 2.Creat 2 figures.

import matplotlib.pyplot as plt # Import the pyplot module in matplotlib package. 
fig, (ax1, ax2) = plt.subplots(1, 2) # Determine here will present 2 figures in 1 page.

# 3.Input the labels of the first pie chart.
# 4.Input relevant data and store it in a list.
# 5.Determine the size of piechart, using information stored.
# 6.Determine the "explode" situation, every part isn't highlighted.
# 7.Determine the pie chart is a circle.
# 8.Input the title.
labels1 = 'England', 'Wales', 'Northern Ireland', 'Scotland' # Input the labels name of the first figure.
uk_countries = [57.11, 3.13, 1.91, 5.45] # Create a list to store data of uk countries.
sizes1 = uk_countries # Determine the sizes of the first figure, using the data stored.
explode1 = (0, 0, 0, 0) # Every part isn't highlighted in this figure.
ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%') # Dtermine the information of figure1, including the sizes, explode, labels and autopct.
ax1.axis('equal') # Determine the figure is a circle.
ax1.set_title('UK') # Determine the title.

# 9.Input the labels of the second pie chart.
# 10.Input relevant data and store it in a list.
# 11.Determine the size of piechart, using information stored.
# 12.Determine the "explode" situation, every part isn't highlighted.
# 13.Determine the pie chart is a circle.
# 14.Input the title.
labels2 = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu' # Input the labels name of the second figure.
China_provinces = [65.77, 41.88, 45.28, 61.27, 85.15] # Create a list to store data of China provinces.
sizes2 = China_provinces # Determine the sizes of the second figure, using the data stored.
explode2 = (0, 0, 0, 0, 0) # Every part isn't highlighted in this figure.
ax2.pie(sizes2, explode=explode2, labels=labels2, autopct='%1.1f%%') # Dtermine the information of figure2, including the sizes, explode, labels and autopct.
ax2.axis('equal') # Determine the figure is a circle.
ax2.set_title('China') # Determine the title.

# 15.Determine the space between 2 pie charts, preventing coverage.
# 16.Out these pie charts.
plt.subplots_adjust(wspace=1) # Determine the space.
plt.show() # Output the 2 figures