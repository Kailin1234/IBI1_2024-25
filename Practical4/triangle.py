# 1.Create a for loop to input number from 1 to 10, and store this number as n.
# 2.Create m as n-1, which will be used on accumulating addtion.
# 3.Create a while loop to set a condition as m doesn't equal to 0, which can induce addition.
# 4.Update n as n+m, which is the accumulating addtion.
# 5.Update m as m-1, which ensure the following added number is smaller step by step.
# 6.Use if to judge when m is equal to 0.
# 7.Stop the while loop.
# 8.Output the result after each while loop, not for loop.
# 9.Write the answer using comment.

for n in range(1,11): # The variable n in a for loop, ranging from 1 to 10, where 11 is not included.
    m = n-1 # Define the m value.
    while m != 0: # The while loop, judging the value of m whether m meets the need to enter loop.
        n = n+m # Update n value.
        m -= 1 # Update m value.
        if m == 0: # The if sentence, judging the value of m whether the while loop can stop.
            break # Break the while loop.
    print(n) # Output result after while loop. If output after for loop, there will be only one value. 

# Result: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55