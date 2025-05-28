# 1.Import some important libraries.
import os # Act as interface to regulate operation system.
import pandas as pd # Access, process and analyze the data from like-Excel sources and create dataframe.
import matplotlib.pyplot as plt # Visualize the data.
import numpy as np # Compute and process the data.

# 2.Set the working directory and read the data.
os.chdir(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical10') # Change the dictionary to Practical 10 in this Python script.
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # Access and read the data from this Excel.

# 3.Explore the data.
print(dalys_data.iloc[0:10,2]) # Show the year for the first 10 rows.
# The 10th year with DALYs data recorded in Afghanistan is 1999.
print("----------")

# 4.Extract the data of DALYs.
year = dalys_data.iloc[:,2] == 1990 # Assign True for all the 1990.
print(dalys_data.loc[year,"DALYs"]) # Show the respective DALYs.
print("----------")

# 5.Extract the data of DALYs in Afghanistan.
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]] # Extract the data of UK.
France = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]] # Extract the data of France.
print("DALYs mean of UK is", uk["DALYs"].mean()) # Compute the mean.
print("DALYs mean of France is", France["DALYs"].mean()) # Compute the mean.
if uk["DALYs"].mean() > France["DALYs"].mean(): # Comparison
    print("DALYs mean of UK is larger than DALYs mean of France") # Print the result.
else: # If the mean of UK is smaller than France, print the result.
    print("DALYs mean of UK is smaller than DALYs mean of France") # Print the result.
    
# DALYs mean of UK is larger than DALYs mean of France

# 6.Plot the DALYs of UK over time.
plt.plot(uk.Year, uk.DALYs, 'b+') # b+/r+... relates to the symbol and color of the dots
plt.xticks(uk.Year,rotation=-90) # Set the xticks.
plt.title("DALYS over time in the UK") # Set the title of the plot.
plt.xlabel("Year") # Set the x-axis label.
plt.ylabel("DALYs") # Set the y-axis label.
plt.tight_layout() # Adjust the layout to prevent overlap.
plt.show() # Show the plot.

# 7. Code for question.txt
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]] # Extract the data of UK.
china = dalys_data.loc[dalys_data.Entity == "China", ["DALYs", "Year"]] # Extract the data of China.
fig, ax = plt.subplots() # Create a figure with both data.
ax.plot(uk.Year, uk.DALYs, 'b+', label='UK') # Set the dots of UK.
ax.plot(china.Year, china.DALYs, 'r+', label='China')  # Use red color to distinguish different symbols between China and UK.
ax.set_title("DALYs: UK vs China") # Set the title of the plot.
ax.set_xlabel("Year") # Set the x-axis label.
ax.set_ylabel("DALYs") # Set the y-axis label.
ax.legend() # Add a legend to distinguish the two lines.
plt.tight_layout() # Adjust the layout to prevent overlap.
plt.show() # Show the plot.