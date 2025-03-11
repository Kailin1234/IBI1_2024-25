# What does this piece of code do?
# Answer: times of entering the loop, until first_n = second_n

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0: # it will enter a loop, because it's always true.
	progress+=1 # update the progress value as progress+1.
	first_n = randint(1,6) # 1, 2, 3, 4, 5
	second_n = randint(1,6)
	if first_n == second_n: # execute when first_n = second_n
		print(progress)
		break
# Every execution result is different.
# Possible results:
