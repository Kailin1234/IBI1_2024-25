# 1.According to the information provided, create a new dictionary called language, containing relevant statistic.
# 2.Output the dictionary.
# 3.Use the input() function to let the user access the key in the dictionary.
# 4.If the key is in the dictionary, output the relevant value.
# 5.If the key is not in the dictionary, output another sentence.

language = {'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5} # A dictionary about language and the relevant users percentage.
print(language) # Output the dictionary.
key = input("Please enter a name of programming language: ") # Let the user to access the information in this dictionary.
if key in language: # One situation when the user inputing the languade name.
    print("The percentage of users is", {language[key]}) # Output the information stored in the dictionary.
else: # Another situation when inputing.
    print("We don't have the data of it.") # Output we don't have this information to preventing error information.

# 1.Import numpy package to process statistic.
# 2.Import mmatplotlib.pyplot to visualize statistic.
# 3.Input the quantity of the objects (5 languages).
# 4.Input relevant users percentage.
# 5.Input an index with these 5 objects, located at x-axis.
# 6.Determine the width of bars.
# 7.Use plt.bar function to create a bar chart, incuding information above(4,5,6).
# 8.Determine xticks.
# 9.Determine the title of this bar chart.
# 10.Determine the ylabel.
# 11.Output the bar chart.

import numpy as np # numpy package.
import matplotlib.pyplot as plt # matplotlib.pyplot package.
N = 5 # Number of the objects (languages).
Users_percentage = (62.3, 52.9, 51, 51, 38.5) # Relevant percentages.
ind = np.arange(N) # Create an index about N.
width = 0.35 # The width of each bar.
pl = plt.bar(ind, Users_percentage, width) # The data of the bar chart.
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript')) # The x-axis(objects quantity and relevant names).
plt.title('Programming language popularity') # The bar chart title.
plt.ylabel('Percentage') # The ylabel.
plt.show() # Output the bar chart.