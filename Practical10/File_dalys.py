# Import some important libraries.
import os # Act as interface to regulate operation system.
import pandas as pd # Access, process and analyze the data from like-Excel sources and create dataframe.
import matplotlib.pyplot as plt # Visualize the data.
import numpy as np # Compute and process the data.

os.chdir(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical10') # Change the dictionary to Practical 10 in this Python script.
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # Access and read the data from this Excel.

print(dalys_data.iloc[0:11,2]) # Show the year for the first 10 rows. The 10th year with DALYs data recorded in Afghanistan is 2000.
print("----------")

year = dalys_data.iloc[:,2] == 1990 # Assign True for all the 1990.
print(dalys_data.loc[year,"DALYs"]) # Show the respective DALYs.
print("----------")

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]] # Extract the data of UK.
France = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]] # Extract the data of France.
print("DALYs mean of UK is", uk["DALYs"].mean()) # Compute the mean.
print("DALYs mean of France is", France["DALYs"].mean()) # Compute the mean.
if uk["DALYs"].mean() > France["DALYs"].mean(): # Comparison
    print("DALYs mean of UK is larger than DALYs mean of France")
else:
    print("DALYs mean of UK is smaller than DALYs mean of France")
print("----------")

plt.plot(uk.Year, uk.DALYs, 'b+') # b+/r+... relates to the symbol and color of the dots
plt.xticks(uk.Year,rotation=-90) # Set the xticks.
plt.title("DALYS over time in the UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.tight_layout()
plt.show()
print("----------")

# question.txt
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]] # Extract the data of UK.
china = dalys_data.loc[dalys_data.Entity == "China", ["DALYs", "Year"]] # Extract the data of China.
fig, ax = plt.subplots() # Create a figure with both data.
ax.plot(uk.Year, uk.DALYs, 'b+', label='UK') # Set the dots of UK.
ax.plot(china.Year, china.DALYs, 'r+', label='China')  # Use red color to distinguish different symbols between China and UK.
ax.set_title("DALYs: UK vs China")
ax.set_xlabel("Year")
ax.set_ylabel("DALYs")
ax.legend()
plt.tight_layout()
plt.show()