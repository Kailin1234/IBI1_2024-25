# 1.import necessary libraries
import numpy as np # import numpy library to process statistic
import matplotlib.pyplot as plt # import matplotlib.pyplot library to visualize the statistic

# 2.set some basic variables and original population
beta = 0.3 # infected probability
gamma = 0.05 # recovered probability
population = np.zeros((100, 100)) # original population, 0 is not infected
outbreak = np.random.choice(range(100), 2) # pick 2 values for a hundres numbers as the coordinate
population[outbreak[0], outbreak[1]] = 1 # the first infected individual
plt.figure(figsize=(6,4),dpi = 150) # the basic information of this figure
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest') # import data population, set the color and the pixel situation
plt.title("times = 0") # set the title of this figure
plt.show() # output the figure

# 3.create a for loop to simulation SIR model, typically focusing on individuals
for t in range(101): # execute for 101 times, including 100 and not including 101
    new_population = population.copy() # create a copy of population to store changes
    Infected = np.where(population == 1) # select all the infected individuals, we get a tuble but not a list
    dx = [-1, 0, 1] # -1 is the left position, 0 is the original position and 1 is the right position
    dy = [-1, 0, 1] # -1 is the upper positioin, 0 is the original position and 1 is the below position
    coordinate = list(zip(Infected[0], Infected[1])) # because we need iterable object as a list for the following loop, we need to change a tuble into a list. zip can make them into coordinate pairs, and store them into a list
    for [i, j] in coordinate: # exter a for loop with each infected individuals
        for dxi in dx: # ensure we pick a single value from dx
            for dyi in dy: # ensure we pick a single value form dy
                di = i + dxi # select the individuals surrounding infected one
                dj = j + dyi # select the individuals surrounding infected one
                if 0 <=di < 100 and 0 <=dj <100: # ensure each individual is in the population but not outside
                    if di == i and dj == j: # rule out the infected oneself
                        continue # continue select surrounding individuals
                    else: # the situation we can choose it as another infected object
                        if new_population[di,dj] == 0 and np.random.rand() < beta: # ensure it is a susceptible individual and use infected probability
                            new_population[di, dj] = 1 # 1 is infected
        if new_population[i, j] == 1 and np.random.rand() < gamma: # ensure it is an infected individual and use recovered probability
            new_population[i, j] = 2 # 2 is recovered
    population = new_population # update the population
    if t in [10, 50,100]: # create figure through iteration
        plt.figure(figsize=(6,4),dpi = 150) # the basic information of this figure
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest') # import data population, set the color and the pixel situation
        plt.title(f"times = {t}") # set the title of this figure
        plt.show() # output the figure