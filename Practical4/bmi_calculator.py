# 1.If we need to let the user input their practical value, and we can calculate and get the result, we can use the function input()
# 2.Because we need to further compare the value, but the input() function only can store data as string. We also need to use float() to change the data type. (We don't use int() because height value is often a float.)
# 3.Let the user input his/her weight value and height value.
# 4.Define the calculation of BMI.
# 5.Use if sentense to determine whether BMI is bigger than 30, affecting whether output the obese result.
# 6.Use elif sentense to determine whether BMI is smaller than 18.5, affecting whether determine whether BMI is smaller than 18.5.
# 7.Use else sentense to consider the condition except for 2 conditions above, and output the normal weight result.

weight = float(input("Please enter your weight value. (kg)")) # Define variable weight.
height = float(input("Please enter your height value. (m)")) # Define variable height.
BMI = weight/height**2 # Define the calculation of BMI.
if BMI > 30: # Determine whether BMI is bigger than 30.
    print("Your BMI is", BMI, "You are considered obese") # If ture, output the obese result.
elif BMI < 18.5: # Determine whether BMI is smaller than 18.5.
    print("Your BMI is", BMI, "You are considered underweight") # If true, determine whether BMI is smaller than 18.5.
else: # Consider the condition except for 2 conditions above.
    print("Your BMI is", BMI, "You are considered normal weight") # Output the normal weight result.