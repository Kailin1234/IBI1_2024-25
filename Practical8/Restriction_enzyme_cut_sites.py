# 1.Import the re library to use regular expression.
# 2.Define a new function named restriction_enzyme, with paraments sequence and recognised_segment.
# 3.

import re

def restriction_enzyme(sequence, recognised_segment):
    if re.search("[ATCG]"):
        sequence = str(input("Please input your DNA sequence:"))
        recognised_segment = str(input("Please input your recognised segment:"))
        matches = re.finditer(recognised_segment, sequence)
        positions = [match.start() for match in matches]
        final_positions = []
        for num in positions:
            final_num = num + 1
            final_positions.append(final_num)
        return final_positions
    return "Your sequence is not standard."

# Example
def restriction_enzyme_example(sequence, recognised_segment):
    if re.search("[ATCG]", sequence):
        matches = re.finditer(recognised_segment, sequence)
        positions = [match.start() for match in matches]
        final_positions = []
        for num in positions:
            final_num = num + 1
            final_positions.append(final_num)
        return final_positions
    return "Your sequence is not standard."

sequence = "ACGGAATTCTGACGAATTCGATAGGAATTCCGATGAATTCAGCTAGAATTCGTA"
recognised_segment = "GAATTC"
print(restriction_enzyme_example(sequence, recognised_segment))

print(recognised_segment)