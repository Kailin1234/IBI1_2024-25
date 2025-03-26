# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# set some necessary variables and array.
N = 10000 # population number
beta = 0.3 # infected probability
gamma = 0.05 # recovered probability
vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # an array to store data of vaccination rate

# create a firgure that can execute in a for loop for many times
plt.figure(figsize=(6,4),dpi=150) # figure information: length is 6 inches, width is 4 inches, and pixel is 150
for alpha in vaccination_rate: # every loop takes an unique alpha value
    I = 1 # initial infected number
    R = 0 # initial recovered number
    V = int(N * alpha) # initial vaccinated number relating to alpha value
    S = int(N-I-V) # initial susceptible number
    Num_I = [I] # create an array to store I value for graphing
    for _ in range(1000): # set a loop for 1000 times
        new_beta = beta*I/N # update the infected probability at each beginning of the loop
        if S>0 and new_beta<1: # when alpha is 100%, N=V, S=-1, the size of np.random.choice()function should not be negative
            random_infected = np.random.choice(range(2), S, p=[1-new_beta, new_beta]) # 0 isn't infected, 1 is infected, conduct loops for all the susceptible individuals
            new_infected = sum(random_infected) # calculate the sum of new infected individuals
            I += new_infected # update the number of the infected individuals
            S -= new_infected # update the number of the susceptible individuals
            random_recovered = np.random.choice(range(2), I, p=[1-gamma, gamma]) # 0 is not recovered, 1 is recovered,conduct loops for all the infected individuals
            new_recovered = min(sum(random_recovered), I) # calculate the sum of new recovered individuals
            R += new_recovered # update the number of the recovered individuals
            I -= new_recovered # update the number of the infected individuals
            Num_I.append(I) # update the elements stored in the array
    plt.plot(Num_I, label = f'{alpha*100}%', color=cm.viridis(alpha)) # import a curve after each loop ending
plt.xlabel("Time") # label for independent variable
plt.ylabel("Number of Infected People") # label for dependent variable
plt.title("SIR Model with Vaccination") # title of the plot
plt.legend() # output this legend
plt.show() # output the whole plot