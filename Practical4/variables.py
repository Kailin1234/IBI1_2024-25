# 1.Store the time taken by bus stop as variable a.
# 2.Store the time taken by bus journey as variable b.
# 3.Define varible c as the sum of a and b, which is total time.
# 4.Store the time taken by drive as variable d.
# 5.Store the time taken by car park journey as variable e.
# 6.Define varible f as the sum of d and e, which is total time.
# 7.Output c and f, and use "if" to judge which is bigger.
# 8.Use comment to write the answer.

a = 15 # a is 15 mins.
b = 75 # b is 1 hr and 15 mins, so b is 75 mins.
c = a+b # c is the sum of a and b, which is total length of time for the bus-based.
print("c = ", c, "mins")
d = 90 # d is 1 hr and 30 mins, so d is 90 mins.
e = 5 # e is 5 mins.
f = d+e # f is the sum of d and e, which is total length of time for the car-based.
print("f = ", f, "mins") 
if c >= f:
    print("c is longer than f. Driving car is quicker.")
else:
    print("f is longer than c. Taking bus is quicker.")
# Result: c =  90 mins and f =  95 mins,so f is longer than c. Taking bus is quicker.


# 1.Create variable X and variable Y.
# 2.Create variable W as X and Y.
# 3.Use comment to write a truth table with X, Y and W, according to booleans.

X = True # X should be True.
Y = False # Y should be False.
W = X and Y # W is both X and Y.
print(W) # Output W, which should be False.
#   X    |   Y    |  W
#  True  |  True  | True
#  True  |  False | False
#  False |  True  | False
#  False |  False | False