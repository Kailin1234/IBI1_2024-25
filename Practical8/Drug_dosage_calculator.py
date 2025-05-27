# 1.Define a function named drug_dosage and its parameters including age, weight and strenth_of_paracetamol.
# 2.Use input function to let the user enter weight.
# 3.Use input function to let the user enter strength_of_paracetamol.
# 4.Set the second check to permit weight is ranging from 10 to 100.
# 5.Set the third check to permit weight is 120/5 or 250/5, which refers to strength_of_paracetamol is 24 or 50.
# 6.If meeting all the requirements above, calculate the dosage.
# 7.Return the dosage.
# 8.Return strength_of_paracetamol is out of range if meeting the first and second requirements but not meeting the third one.
# 9.Return weight is out of range if meeting the first requirement but not meeting the second one.
# 10.Return age is out of range if not meeting the first requirement.

def drug_dosage (weight, strength_of_paracetamol): # Define the function with name and paraments.
    if weight not in range(10, 101): # Second check for weight.
        return "Your weight is out of range." # Pass the first but not pass the second.
    if strength_of_paracetamol != 24 and strength_of_paracetamol != 50: # Third check for strength_of_paracetamol. 24 refers to 120/5 mg/ml and 50 refers to 250/5 mg/ml.
        return "The strength_of_paracetamol is out of range." # Pass the first and second checks but not pass the third.
    if weight in range(10, 101):
        if strength_of_paracetamol == 24 or strength_of_paracetamol == 50:
            dosage = 15 * weight / strength_of_paracetamol # Dosage calculation.
            return dosage # Pass the check.
        
    
# 11.Example to show the execution without user inputing.
print(drug_dosage(30, 50)) # Normal execution.
print(drug_dosage(120, 24)) # Weight is out of range.
print(drug_dosage(40, 20)) # strength_of_paracetamol is out of range.

# 12.Let the user input the data.
weight = float(input("Please enter your weight(kg): ")) # Let the user input weight.
strength_of_paracetamol = float(input("Please enter the strength of paracetamol (Available: 120mg/5ml, input 24, or 250mg/5ml, input 50):")) # Let the user input strength_of_paracetamol.
print(drug_dosage(weight, strength_of_paracetamol)) # Print the result of drug_dosage function.