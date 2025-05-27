# 1.Define the class name called patients.
# 2.Initialse the parameters, including name, age, date_of_lastest_admission and medical_history. Self means the instance of class.
# 3.Assign the input name to instance name.
# 4.Assign the input age to instance age.
# 5.Assign the input date_of_lastest_admission to instance date_of_lastest_admission.
# 6.Assign the input medical_history to instance medical_history.
# 7.Define a new method called introduce, accessing to self.
# 8.Return the result including all the properties above, using f-string.

class patients: # The new class.
    def __init__(self, name, age, date_of_lastest_admission, medical_history): # Initialise the parameters.
        self.name = name # Assign name attribute.
        self.age = age # Assign age attribute.
        self.date_of_lastest_admission = date_of_lastest_admission # Assign date_of_lastest_admission attribute.
        self.medical_history = medical_history # Assign medical_history attribute.
    def introduce(self): # The new method to access self.
        return f"Name: {self.name}, Age: {self.age}, Date of lastest admission: {self.date_of_lastest_admission}, Medical history: {self.medical_history}" # Return the patient's information.

# Example
Patient1 = patients("Mark", 18, "2025/4/8", "None") # Use this class to store information of a patient.
Information1 = Patient1.introduce() # Use the method(introduce) to access the information.
print(Information1) # Output the patient's information.

# Let the user input the data.
name = input("Please enter the patient's name: ") # Let the user input the name.
age = int(input("Please enter the patient's age: ")) # Let the user input the age. 
date_of_lastest_admission = input("Please enter the date of lastest admission (YYYY/MM/DD): ") # Let the user input the date of lastest admission.
medical_history = input("Please enter the patient's medical history: ") # Let the user input the medical history.  
Patient2 = patients(name, age, date_of_lastest_admission, medical_history) # Use this class to store information of a patient.
Information2 = Patient2.introduce() # Use the method(introduce) to access the information.
print(Information2) # Output the patient's information.