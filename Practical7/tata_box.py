# 1.Import the re library to use regular expression.
# 2.Open the input file and output file.
# 3.Initialize empty strings for gene_name and gene_sequence.
# 4.Iterate through each line in the input file.
# 5.Check if the line starts with '>', indicating a header line.
# 6.If it is a header line, check if the previous gene sequence contains a TATA box.
# 7.If it does, write the gene name and sequence to the output file.
# 8.Extract the gene name from the header line and reset the gene sequence.
# 9.If the line is not a header line, append the line to the current gene sequence.
# 10.After the loop, check if the last gene sequence contains a TATA box and write it to the output file if it does.

import re # Import the re library to use regular expression

input = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') # Open the input file containing gene sequences
output = open(r"c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\tata_genes.fa", 'w') # Open the output file to write the filtered gene sequences
gene_name = "" # Initialize an empty string to store the current gene name
gene_sequence = "" # Initialize an empty string to store the current gene sequence

for line in input: # Iterate through each line in the input file
    if re.search('^>', line): # Check if the line starts with '>', which is the header line
        if gene_name and re.search("TATA[AT]A[AT]", gene_sequence): # Search for the TATA box
                output.write(f">{gene_name}\n{gene_sequence}\n") # Write the gene name and sequence, when meet the next header line
        gene_name = line.strip().split(' ')[0].split('_')[0][1:] # Extract the gene name from the header line
        gene_sequence = "" # Reset the gene sequence for the new gene
    else: # If the line is not a header line, it contains part of the gene sequence
        gene_sequence += line.strip() # Append the line to the current gene sequence
# Because the gene name and sequence will be written when reading the next header line, we need to store the last gene name and sequence after the loop

if gene_name and re.search("TATA[AT]A[AT]", gene_sequence): # Check if the last gene sequence contains a TATA box
    output.write(f">{gene_name}\n{gene_sequence}\n") # Write the last gene name and sequence to the output file