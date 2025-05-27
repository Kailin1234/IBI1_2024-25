# 1.Import the re library to use regular expression.
# 2.Define a new function named restriction_enzyme, with paraments sequence and recognised_segment.
# 3.Check if the sequence only contains standard nucleotides (A, T, C, G) using regular expression.
# 4.If the sequence is standard, use re.finditer to find all occurrences of the recognised_segment in the sequence.
# 5.Store the start positions of each match in a list called positions.
# 6.Create an empty list called final_positions to store the final positions.
# 7.Iterate through the positions list, adding 1 to each position and appending it to final_positions.
# 8.Return the final_positions list.
# 9.If the sequence is not standard, return a message indicating that the sequence is not standard.
# 10. Use the function to find the restriction enzyme cut sites in a given sequence.

import re # Importing the re library to use regular expression

def restriction_enzyme(sequence, recognised_segment): # Defining a new function
    std_nucleotide = 'AGCT' # Defining the standard nucleotides
    for i in sequence: # Iterating through the sequence
        if i not in std_nucleotide: # Checking if the nucleotide is not standard
            return "Your sequence is not standard."
    
    matches = re.finditer(recognised_segment, sequence) # Finding the recognised segment in the sequence
    positions = [match.start() for match in matches] # Storing the start positions
    final_positions = [] # Initializing an empty list
    for num in positions: # Iterating through the positions
        final_num = num + 1 # Adding 1 to each position
        final_positions.append(final_num) # Appending the final position to the list
    return final_positions # Returning the final positions

sequence = "ACGGAATTCTGACGAATTCGATAGGAATTCCGATGAATTCAGCTAGAATTCGTA" # Example sequence
recognised_segment = "GAATTC" # Example recognised segment
print(restriction_enzyme("ACGGAATTCTGACGAATTCGATAGGAATTCCGATGAATTCAGCTAGAATTCGTA", "GAATTC")) #Output the restriction enzyme cut sites