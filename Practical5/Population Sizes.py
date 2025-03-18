# 1.Import matplotlib.pyplot to visualize statistic.
# 2.Creat 2 figures.

import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2)

# 3.Input the labels of the first pie chart.
# 4.Input relevant data and store it in a list.
# 5.Determine the size of piechart, using information stored.
# 6.Determine the "explode" situation, every part isn't highlighted.
# 7.Determine the pie chart is a circle.
# 8.Input the title.
labels1 = 'England', 'Wales', 'Northern Ireland', 'Scotland'
uk_countries = [57.11, 3.13, 1.91, 5.45]
sizes1 = uk_countries
explode1 = (0, 0, 0, 0)
ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%')
ax1.axis('equal')
ax1.set_title('UK')

# 9.Input the labels of the second pie chart.
# 10.Input relevant data and store it in a list.
# 11.Determine the size of piechart, using information stored.
# 12.Determine the "explode" situation, every part isn't highlighted.
# 13.Determine the pie chart is a circle.
# 14.Input the title.
labels2 = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'
China_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
sizes2 = China_provinces
explode2 = (0, 0, 0, 0, 0)
ax2.pie(sizes2, explode=explode2, labels=labels2, autopct='%1.1f%%')
ax2.axis('equal')
ax2.set_title('China')

# 15.Determine the space between 2 pie charts, preventing coverage.
# 16.Out these pie charts.
plt.subplots_adjust(wspace=1)
plt.show()