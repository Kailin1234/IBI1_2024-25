# 1.import necessary libraries
import numpy as np # for numerical operations
import matplotlib.pyplot as plt # for plotting

# 2.define the basic variables 
N = 10000 # population
S = 9999 # susceptible
I = 1 # infected
R = 0 # recovered
beta = 0.3 # infection probability
gamma = 0.05 # recovery probability

# 3.create arraies to store updated data
Num_S = [S] # number of susceptible individual with times
Num_I = [I] # number of infected individual with times
Num_R = [R] # number of recovered individual with times

# 4.create a for loop to simulation SIR process
for n in range(1000): # create a for loop to execute for 1000 times
    random_recovered = np.random.choice(range(2), I, p=[1-gamma,gamma]) # 0 is unrecovered, 1 is recovered
    new_recovered = sum(random_recovered) # the number of recovered individuals
    R += new_recovered # produce a new R value
    new_beta = beta*I/N # update the probability of infection, because of propotion
    random_susceptible = np.random.choice(range(2), S, p=[1-new_beta,new_beta]) # 0 is not infected, 1 is infected
    new_infected = sum(random_susceptible) # the number of infected individuals
    I = I+new_infected-new_recovered # produce a new I value
    S -= new_infected # produce a new S value
    Num_S.append(S) # update the S array for y-axis value of S curve
    Num_I.append(I) # update the I array for y-axis value of I curve
    Num_R.append(R) # update the R array for y-axis value of R curve

# 5.create a plot
y1 = Num_S # set the y-value for S curve
y2 = Num_I # set the y-value for I curve
y3 = Num_R # set the y-value for R curve
plt.figure(figsize=(6,4),dpi=150) # the size of the figure: length is 6 inches, width is 4 inched, and pixel is 150
plt.plot(y1, label='Susceptible', color='blue') # create the curve for number of susceptible individuals with times
plt.plot(y2, label='Infected', color='orange') # create the curve for number of infected individuals with times
plt.plot(y3, label='Recovered', color='green') # create the curve for number of recovered individuals with times
plt.xlabel('time') # label of x-axis
plt.ylabel('number of people') # label of y-axis
plt.title('SIR model') # title of this plot
plt.legend() # legend of this plot
plt.show() # output the complete plot
plt.savefig('SIR.png') # save the plot as a png file