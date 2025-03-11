# define the variables: weight, height, BMI
# if the BMI value is greater than 30, the person is obese.
# if the value is less than 18.5, the person is underweight.
# if both not, the person is normal weight.
# output the result

weight = 46 # kg
height = 1.63 # m
BMI = weight/ height**2
if BMI > 30:
    print("Your BMI is", BMI, "You are considered obese")
elif BMI < 18.5:
    print("Your BMI is", BMI, "You are considered underweight")
else:
    print("Your BMI is", BMI, "You are considered normal weight")