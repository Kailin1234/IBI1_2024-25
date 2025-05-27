# 1.Import the re library to use regular expression.
# 2.Define a new function named largest_intron, with paraments sequence.
# 3.Use re.findall to find all occurrences of the pattern 'GT.+AG' in the sequence.
# 4.Store the matches in a list called largest_intron.
# 5.Print the largest intron found in the sequence.

import re # Import the library
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' # Exaple sequence
largest_intron = re.findall(r'GT.+AG', seq) # Find the longest pattern 'GT.+AG' in the sequence
print(largest_intron) # Output the largest intron
lenth = len(largest_intron[0]) # Calculate the length of the largest intron
print(lenth) # Output the length of the largest intron