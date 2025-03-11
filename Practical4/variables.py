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

X = True
Y = False
W = X and Y
print(W)
# W is False.