# 1.Define a function named drug_dosage and its parameters including age, weight and strenth_of_paracetamol.
# 2.Use input function to let the user enter age.
# 3.Use input function to let the user enter weight.
# 4.Use input function to let the user enter strength_of_paracetamol.
# 5.Set the first check to permit age is ranging from 0 to 18.
# 6.Set the second check to permit weight is ranging from 10 to 100.
# 7.Set the third check to permit weight is 120/5 or 250/5.
# 8.If meeting all the requirements above, calculate the dosage.
# 9.Return the dosage.
# 10.Return strength_of_paracetamol is out of range if meeting the first and second requirements but not meeting the third one.
# 11.Return weight is out of range if meeting the first requirement but not meeting the second one.
# 12.Return age is out of range if not meeting the first requirement.

def drug_dosage (age, weight, strength_of_paracetamol): # Define the function with name and paraments.
    age = input("Please enter your age: ") # Let the user input age.
    weight = float(input("Please enter your weight(kg): ")) # Let the user input weight.
    strength_of_paracetamol = float(input("Please enter the strength of paracetamol(mg/ml): ")) # Let the user input strength_of_paracetamol.
    if age <= 18 and age > 0: # First check for age.
        if weight in range(10, 101): # Second check for weight.
            if strength_of_paracetamol == 120/5 or strength_of_paracetamol == 250/5: # Third check for strength_of_paracetamol.
                dosage = 15 * weight / strength_of_paracetamol # Dosage calculation.
                return dosage # Pass three check.
            return "The strength_of_paracetamol is out of range." # Pass the first and second checks but not pass the third.
        return "Your weight is out of range." # Pass the first but not pass the second.
    return "You age is out of range." # Not pass the first.

# Example to show the execution without user inputing.
# All the coding thoughts are the same, but the input part is replaced by data already input when using this function.

def drug_dosage_example (age, weight, strength_of_paracetamol):
    if age <= 18 and age > 0:
        if weight in range(10, 101):
            if strength_of_paracetamol == 120/5 or strength_of_paracetamol == 250/5:
                dosage = 15 * weight / strength_of_paracetamol
                return dosage
            return "The strength_of_paracetamol is out of range."
        return "Your weight is out of range."
    return "You age is out of range."

print(drug_dosage_example(8, 30, 250/5)) # Normal execution.
print(drug_dosage_example(19, 46, 250/5)) # Age is out of range.
print(drug_dosage_example(18, 45, 24)) # Normal execution.
print(drug_dosage_example(13, 120, 120/5)) # Weight is out of range.
print(drug_dosage_example(14, 40, 20)) # strength_of_paracetamol is out of range.

print(drug_dosage)