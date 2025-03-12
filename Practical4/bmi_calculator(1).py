weight = float(input("Please enter your weight value. (kg)"))
height = float(input("Please enter your height value. (m)"))
BMI = weight/height**2
if BMI > 30:
    print("Your BMI is", BMI, "You are considered obese")
elif BMI < 18.5:
    print("Your BMI is", BMI, "You are considered underweight")
else:
    print("Your BMI is", BMI, "You are considered normal weight")

# Learned from partner in practical.
# If we need to let the user input their practical value, and we can calculate and get the result.
# We can use the function input()
# However, input content is string type, which couldn't be used in calculation.
# So, we need to also use the function float() to change the value type.
# We couldn't use int(), because the height is often not a int.